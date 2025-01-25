import pandas as pd
from smart_tools.dissector import dfdissector

file = r"C:\Users\prabhuramv\Downloads\uszips.csv"

df = pd.read_csv(file, sep = ",", dtype = str, quotechar='"', keep_default_na = False)
print(df.dtypes)
dissected_df = dfdissector.dissect_dataframe(df)
df.apply(lambda x: x.apply(str).str)

print(dissected_df.to_markdown())