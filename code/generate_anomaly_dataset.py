

# ======================================================================# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

# Use the kagglehub client library to attach Kaggle resources like competitions, datasets, and models to your session
# Learn more about kagglehub: https://github.com/Kaggle/kagglehub/blob/main/README.md

import kagglehub
# kagglehub.dataset_download('<owner>/<dataset-slug>')

import os, glob
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

CH = ["avgcpu", "avgmem"]
TRACES = [
    "gc11", "gc19_a", "gc19_b", "gc19_c", "gc19_d",
    "gc19_e", "gc19_f", "gc19_g", "gc19_h", "ali20_c", "ali20_g"
]
TRAIN_FRAC = 0.70
W = 36
K_Z, K_J, K_E = 3.0, 3.0, 3.0
IF_Q = 0.95
MIN_VOTES = 2
SPIKE_Q = 0.95
SEED = 42

ROOT = next(
    (p for p in ["/kaggle/input", "."] if glob.glob(p + "/**/*.csv", recursive=True)),
    "."
)
OUT = "/kaggle/working/anomaly_out" if os.path.isdir("/kaggle/working") else "anomaly_out"
os.makedirs(OUT, exist_ok=True)


def rmad(s, w):
    return s.rolling(w).apply(
        lambda v: np.median(np.abs(v - np.median(v))), raw=True
    )


def comps(x, n_tr):
    floor = 0.25 * x.iloc[:n_tr].std() + 1e-6
    d = x.diff()

    # All rolling references are shifted so time t is compared only with history.
    med = x.rolling(W).median().shift(1)
    sc = (1.4826 * rmad(x, W)).shift(1).clip(lower=floor)
    rz = (x - med) / sc

    dsc = (1.4826 * rmad(d, W)).shift(1).clip(lower=floor * 0.5)
    jz = d / dsc

    ew = x.ewm(span=12, adjust=False).mean().shift(1)
    res = x - ew
    esc = res.ewm(span=W, adjust=False).std().shift(1).clip(lower=floor * 0.5)
    ez = res / esc

    vr = (x.rolling(6).std() / (x.rolling(W).std() + 1e-6)).shift(1)
    return pd.DataFrame({"rz": rz, "jz": jz, "ez": ez, "vr": vr, "x": x, "d": d}).fillna(0.0)


def detect(x, n_tr):
    F = comps(x, n_tr)
    iso = IsolationForest(
        n_estimators=300, contamination="auto",
        random_state=SEED, n_jobs=-1
    )
    iso.fit(F.iloc[W:n_tr].values)
    s_if = -iso.score_samples(F.values)
    thr_if = np.quantile(s_if[W:n_tr], IF_Q)

    v = np.vstack([
        (F["rz"] > K_Z).values,
        (F["jz"] > K_J).values,
        (F["ez"] > K_E).values,
        (s_if > thr_if) & (F["rz"].values > 0),
    ]).astype(float)

    votes = v.sum(0)
    flag = ((votes >= MIN_VOTES) & (F["rz"].values > 0)).astype(float)

    train_max = max(float(s_if[W:n_tr].max()), float(thr_if) + 1e-6)
    if_scale = np.clip(
        (s_if - thr_if) / (train_max - thr_if + 1e-9) + 0.5, 0, 1
    )
    soft = np.vstack([
        np.clip(F["rz"].values / (2 * K_Z), 0, 1),
        np.clip(F["jz"].values / (2 * K_J), 0, 1),
        np.clip(F["ez"].values / (2 * K_E), 0, 1),
        if_scale * (F["rz"].values > 0),
    ]).mean(0)

    flag[:W] = 0.0
    soft[:W] = 0.0

    jthr = np.quantile(F["d"].iloc[W:n_tr].clip(lower=0), SPIKE_Q)
    spike_eval = (F["d"].values > jthr).astype(float)
    spike_eval[:W] = 0.0
    return flag, soft, spike_eval


files = {}
for p in glob.glob(ROOT + "/**/*.csv", recursive=True):
    stem = Path(p).stem
    if stem in TRACES and stem not in files:
        files[stem] = p

missing = [t for t in TRACES if t not in files]
if missing:
    raise FileNotFoundError(
        f"Missing raw trace CSVs: {missing}. Add the original workload dataset as Kaggle input."
    )

rows = []
for name in TRACES:
    df = pd.read_csv(files[name])
    df = df.drop(columns=[c for c in df.columns if c.startswith("Unnamed")])
    missing_cols = [c for c in CH if c not in df.columns]
    if missing_cols:
        raise ValueError(f"{name}: missing required columns {missing_cols}")

    n = len(df)
    n_tr = int(n * TRAIN_FRAC)

    # Avoid backward filling from future observations.
    for c in CH:
        df[c] = pd.to_numeric(df[c], errors="coerce").ffill()
        train_median = df[c].iloc[:n_tr].median()
        df[c] = df[c].fillna(train_median)

    for c in CH:
        flag, soft, spk = detect(df[c], n_tr)
        df[c + "_flag"] = flag
        df[c + "_score"] = soft
        df[c + "_spike_eval"] = spk

        next_rise = df[c].diff().shift(-1).clip(lower=0).abs().values
        m = flag.astype(bool)
        ok = ~np.isnan(next_rise)
        lift = (
            next_rise[m & ok].mean() / (next_rise[~m & ok].mean() + 1e-9)
            if (m & ok).any() else np.nan
        )
        rows.append({
            "trace": name,
            "channel": c,
            "n": n,
            "flag_rate_train": flag[:n_tr].mean(),
            "flag_rate_after_train": flag[n_tr:].mean(),
            "next_rise_lift": lift,
            "spike_cover": (flag.astype(bool) & (spk > 0)).sum() / max(1, (spk > 0).sum()),
        })

    out_path = os.path.join(OUT, f"{name}_flags.csv")
    df.to_csv(out_path, index=False)
    print(f"Saved {out_path}", flush=True)

summary = pd.DataFrame(rows)
summary.to_csv(os.path.join(OUT, "summary.csv"), index=False)
print("\nAnomaly summary:")
print(summary.round(3).to_string(index=False))
print("\nMean by resource:")
print(
    summary.groupby("channel")[
        ["flag_rate_train", "flag_rate_after_train", "next_rise_lift", "spike_cover"]
    ].mean().round(3)
)
