import warnings
import os
import pandas as pd
from smart_tools.comparator import dfcomparator


def compare(file1, file2, sep=',', skiprows=0, skipfooter=0, encoding='utf-8'):

    short_name1 = os.path.basename(file1)
    short_name2 = os.path.basename(file2)

    df1 = pd.read_csv(file1, sep=sep, keep_default_na=False, skiprows=skiprows, skipfooter=skipfooter,
                     engine='python', encoding=encoding, quotechar='"', on_bad_lines='warn', dtype='str')

    df2 = pd.read_csv(file2, sep=sep, keep_default_na=False, skiprows=skiprows, skipfooter=skipfooter,
                     engine='python', encoding=encoding, quotechar='"', on_bad_lines='warn', dtype='str')

    return dfcomparator.compare(df1, df2, (short_name1, short_name2))
