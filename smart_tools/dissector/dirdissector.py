import glob
import os

import pandas as pd

from smart_tools.dissector.filedissector import dissect_from_file


def dissect_from_dir(dir, file, sep, nsample=10, slicers=[''], skiprows=0, skipfooter=0, colnames=None):
    files = glob.glob(os.path.join(dir, file))
    df_all = []
    print(f'files: {len(files)}')
    for file in files:
        for d in dissect_from_file(file, sep=sep, nsample=nsample, slicers=slicers,
                                   skiprows=skiprows, skipfooter=skipfooter, names=colnames):
            df_all.append(d)
    df_all = concat_dfs(df_all)
    return df_all


def concat_dfs(dfs):
    return pd.concat(dfs)