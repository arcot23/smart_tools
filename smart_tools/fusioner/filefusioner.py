import re

import pandas as pd

def filefusion(file, fusion_set, sep):
    df = pd.read_csv(file, sep = sep, dtype=str)

    df = fusion(df, fusion_set)
    return df


def fusion(df, set, sep='='):
    for d in set:
        column = d['column']
        type = d['type']
        source = d['source']

        if type == 'braces':
            matches = re.findall('{(.*?)}', source)
        else:
            source = source.replace("'", "")
            matches = source.split(",")
            matches = [m.strip() for m in matches]

        df[column] = df[matches].apply(lambda r: sep.join(r.values.astype(str)), axis = 1)

    return df