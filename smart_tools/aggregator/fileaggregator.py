import glob
import os

import pandas as pd


def aggregate_files(dir, file_wildcard, sep, include_filename = True, **kwargs):
    files = glob.glob(os.path.join(dir, file_wildcard))

    df_all = []
    print(f'files: {len(files)}')
    for file in files:
        df = pd.read_csv(file, sep=sep, **kwargs)
        if include_filename == True:
            df['file_name'] = file
        df_all.append(df)

    df_all = pd.concat(df_all)
    return df_all
