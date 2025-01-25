import pandas as pd
from smart_tools.dissector import filedissector

dir = r"C:\Users\prabhuramv\Downloads"

df = filedissector.dissect_dir_files(dir, '*.parquet', ',')

print(df.to_markdown())
