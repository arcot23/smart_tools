import re

import pandas as pd


def dissect_dataframe(frame, nsample=5):

    """
    Dissects a pandas dataframe
    :param frame: Dataframe.
    :param nsample: Number of top samples to pick.
    :return: Dissected results as a pandas dataframe.
    """
    def non_alpanumeric(data):
        vals = pd.Series(data).value_counts().sort_values(ascending=True)
        y = dict(zip(vals.index, vals))
        return y

    def val_length(data):
        minl = int(min(data[data.apply(str).str.len() > 0].apply(str).str.len(), default=0))
        maxl = int(max(data[data.apply(str).str.len() > 0].apply(str).str.len(), default=0))
        return {'min': minl, 'max': maxl}

    def not_a_val(data):
        nan = int(data[data.isna()].count())
        # emptystr = int(data[data == ''].count())
        # emptystr = len(data[data == ''])
        emptystr = (data == '').sum()
        return {'nan': nan, 'emptystr': emptystr}

    def top(data, head):
        # values = data.value_counts().sort_values(ascending=False)[:head]
        values = data.value_counts().nlargest(head)
        d = dict(zip(values.index, values))
        return d

    def isn(data):
        return pd.to_numeric(data, errors='coerce').notnull().all()

    isnum = frame.apply(lambda x: isn(x))
    strlen = frame.apply(lambda x: val_length(x))
    nnull = frame.apply(lambda x: not_a_val(x))
    nrow = frame.apply(lambda x: len(x))
    nunique = frame.apply(lambda x: len(x[x.apply(str).str.len() > 0].drop_duplicates().dropna()))
    nvalue = frame.apply(lambda x: len(x[x.apply(str).str.len() > 0].dropna()))
    freq = frame.apply(lambda x: top(x[x.apply(str).str.len() > 0], nsample))
    # sample = frame.apply(lambda x: str(x[x != ''].value_counts().sort_values(ascending=False)[:nsample].index.tolist()))
    sample = frame.apply(lambda x: str(x[x != ''].value_counts().nlargest(nsample).index.tolist()))
    symbols = frame.apply(lambda x: non_alpanumeric(list(re.sub('[a-zA-Z0-9]', '', ''.join(x[x.notna()].astype(str))))))

    cols = ['isnum', 'strlen', 'nnull', 'nrow', 'nunique', 'nvalue', 'freq', 'sample', 'symbols']

    result = pd.concat([isnum, strlen, nnull, nrow, nunique, nvalue, freq, sample, symbols], axis=1)
    result.columns = cols
    result = result.reset_index().rename(columns={'index': 'column'})
    result['n'] = result.reset_index().index + 1

    return result