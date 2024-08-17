import os
import pandas as pd


def filecompare(file1, file2, sep=',', skiprows=0, skipfooter=0, encoding='utf-8'):

    short_name1 = os.path.basename(file1)
    short_name2 = os.path.basename(file2)

    df1 = pd.read_csv(file1, sep=sep, keep_default_na=False, skiprows=skiprows, skipfooter=skipfooter,
                     engine='python', encoding=encoding, quotechar='"', on_bad_lines='warn', dtype='str')

    df2 = pd.read_csv(file2, sep=sep, keep_default_na=False, skiprows=skiprows, skipfooter=skipfooter,
                     engine='python', encoding=encoding, quotechar='"', on_bad_lines='warn', dtype='str')

    return compare(df1, df2, (short_name1, short_name2))


def compare(df1, df2, names=('df1', 'df2')):
    df1 = pd.DataFrame(df1)
    df2 = pd.DataFrame(df2)

    is_same_shape = df1.shape == df2.shape
    has_same_columns = list(df1.columns) == list(df2.columns)
    is_equal = df1.equals(df2)
    diff_summary = None

    if is_same_shape and has_same_columns:
        if not is_equal:
            df_col_differences = df1.compare(df2, result_names=names, align_axis=0)
            df_merged = pd.merge(df1, df2, on=list(df1.columns), how='outer', indicator=True)
            df_row_differences = df_merged[(df_merged['_merge'] == 'left_only') | (df_merged['_merge'] == 'right_only')]
            diff_summary = {'ndiffcols': df_col_differences.shape[1], 'diffcols': list(df_col_differences.columns),
                            'ndiffrows': df_row_differences.shape[0]}

    return {'is_same_shape': is_same_shape, 'has_same_columns': has_same_columns, 'is_equal': is_equal,
            'diff_summary': diff_summary}