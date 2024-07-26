import glob
import os

import pandas as pd

from smart_tools.dissector.filedissector import dissect_from_file


def dissect_from_dir(args, configs):
    files = glob.glob(os.path.join(args['dir'], args['file']))
    df_all = []
    print(f'files: {len(files)}')
    for file in files:
        for d in dissect_from_file(file, sep=args['sep'], nsample=configs['nsample'], slicers=args['slicers'],
                                   skiprows=0, skipfooter=0, names=args['cols']):
            df_all.append(d)
    df_all = concat_dfs(df_all)
    return df_all


def concat_dfs(dfs):
    return pd.concat(dfs)