import re

import pandas as pd

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