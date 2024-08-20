import pandas as pd

def first_valid(df, columns, prefix = "column_", coerce_empty = [r'^\s*$']):
    """
    Returns the first valid index, value and the number of `None` in a series.
    :param df: Dataframe to process.
    :param columns: Columns in `df` to process.
    :param prefix: Prefix for the returned columns `index`, `value` and `non_null`.
    :param coerce_empty: Treats the list of regex patterns as `None`.
    :return: A dictionary `{'index': {}, 'value': {}, 'non_null': {}}`.
    """
    def d(row, coerce_empty):
        if coerce_empty is not None:
            for val in coerce_empty:
                row = row.replace(val, None, regex = True).infer_objects(copy = False)
        t = {
            'index': None,
            'value': None,
            'non_nulls': None
        }

        first_index = row.first_valid_index()
        if first_index is None: return t

        return {
            'index': first_index,
            'value': row[first_index],
            'non_nulls': row.count().item()
        }

    print(prefix)

    tag_simplified = df[columns].apply(lambda row: d(row, coerce_empty), axis= 1)
    tag_results = pd.json_normalize(tag_simplified).add_prefix(prefix)

    return tag_results
