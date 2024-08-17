import pandas as pd
from smart_tools.fusioner import dffusioner

def fusion(file, fusion_set, sep):
    df = pd.read_csv(file, sep = sep, dtype=str)

    df = dffusioner.fusion(df,fusion_set)
    return df
