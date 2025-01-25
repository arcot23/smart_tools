import glob
import hashlib
import os
import time
import warnings

import pandas as pd

from smart_tools.dissector.dfdissector import dissect_dataframe


def dissect_file(file, filetype='csv', sep=';', slicers=[''], nsample=5, **kwargs):
    if filetype.lower().strip() == 'csv':
        df = pd.read_csv(file, sep=sep, **kwargs)
    elif filetype.lower().strip() == 'xlsx' or filetype.lower().strip() == 'xlsx':
        df = pd.read_excel(file, dtype = str)
    elif filetype.lower().strip() in ['parquet', 'pqt']:
        df = pd.read_parquet(file)
    filename = os.path.basename(file)

    for slice in slicers:
        df_sliced = df.copy()
        if len(slice) > 0:
            try:
                df_sliced.query(slice, inplace=True)
            except Exception as err:
                msg = f"{type(err).__name__}: Error occurred while slicing. {err}. Skipped slice `{slice}` in file `{filename}`"
                warnings.warn(msg, Warning)
                continue

        print_msg = f"- {df_sliced.shape} rows & columns in `{filename}` for slice `{slice}`."
        print(print_msg)

        if df_sliced.shape[0] == 0: continue

        result = dissect_dataframe(df_sliced, nsample)
        result[['filename', 'filetype', 'slice']] = filename, filetype, slice

        file_properties = get_file_property(file)
        result[list(file_properties)] = list(file_properties.values())

        yield result


def get_file_hash(path, hash_type='md5'):
    m = hashlib.new(hash_type)
    with open(path, 'rb') as f:
        m.update(f.read())
        return m.hexdigest()


def get_file_property(path, date_time_format='%Y%m%d'):
    filename = os.path.basename(path)

    timestamp = time.gmtime(os.path.getmtime(path))
    timestamp = time.strftime(date_time_format, timestamp)

    hash = get_file_hash(path)

    size = os.path.getsize(path)

    return {'filename': filename, 'timestamp': timestamp, 'hash': hash, 'size': size}


def dissect_dir_files(dir, file_wildcard, sep=';', nsample=10, slicers=[''], **kwargs):
    files = glob.glob(os.path.join(dir, file_wildcard))
    df_all = []
    print(f'files: {len(files)}')
    for file in files:
        if file.endswith(".xlsx"):
            filetype = "xlsx"
        elif file.endswith(".parquet"):
            filetype = "parquet"
        else:
            filetype = "csv"
        for d in dissect_file(file, filetype=filetype, sep=sep, nsample=nsample, slicers=slicers, **kwargs):
            df_all.append(d)
    df_all = concat_dfs(df_all)
    return df_all


def concat_dfs(dfs):
    return pd.concat(dfs)