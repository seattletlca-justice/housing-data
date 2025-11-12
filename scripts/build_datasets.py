import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
parts = sorted(ROOT.glob("RowLevel_With_TimeBuckets_AND*.csv"))

dfs = [pd.read_csv(p, dtype=str, low_memory=False) for p in parts]
master = pd.concat(dfs, ignore_index=True)

out_master = ROOT / "RowLevel_With_TimeBuckets_ALL.csv"
master.to_csv(out_master, index=False)

for d in list("1234567"):
    df_d = master[master["CouncilDistrict"].astype(str).str.strip() == d]
    (ROOT / "district").mkdir(exist_ok=True)
    df_d.to_csv(ROOT / f"district/RowLevel_With_TimeBuckets_D{d}.csv", index=False)

keep = ["RecordNum","RecordType","RecordTypeDesc","Description","OpenDate_dt","LastInspDate_dt","LastInspResult","StatusCurrent","CouncilDistrict"]
master[keep].to_csv(ROOT / "views/RowLevel_Lean_ALL.csv", index=False)

print("Done.")
