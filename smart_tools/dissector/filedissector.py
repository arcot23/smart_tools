import hashlib
import os
import time
import warnings

import pandas as pd

from smart_tools.dissector.dfdissector import dissect_from_frame


def dissect_from_file(file, filetype='csv', sep=';', slicers=[''], nsample=5, skiprows=0, skipfooter=0,
                      encoding='utf-8', names = None):
    if filetype.lower().strip() == 'csv':
        df = pd.read_csv(file, sep=sep, keep_default_na=False, skiprows=skiprows, skipfooter=skipfooter,
                         engine='python', names=names, encoding=encoding, quotechar='"', on_bad_lines='warn', dtype='str')
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

        result = dissect_from_frame(df_sliced, nsample)
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