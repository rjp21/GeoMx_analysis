import pandas as pd
from pathlib import Path

base = Path(__file__).parent
rename = pd.read_excel(base / "file_renaming.xlsx")
old_filenames = pd.read_csv(base / "old_filenames", names=["OldFilename"])

old_filenames[["Lib", "BPF_name", "Suffix"]] = old_filenames["OldFilename"].str.split('_', 2, expand=True)
files = pd.merge(rename, old_filenames, on="BPF_name")
files["Suffix"] = files["Suffix"].str.replace("fast", "fastq")

files["Command"] = "mv -v " + files["OldFilename"] + " " + files["GeoMx_name"] + "_" + files["Suffix"]
out_filename = base / "rename.sh"
files["Command"].to_csv(out_filename, index=False, header=False)
print(f"wrote commands to {out_filename}")
