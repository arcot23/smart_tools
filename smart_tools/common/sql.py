

def build_sql_from_df(df, quote="'", table_name='TABLE', join_by="UNION ALL", indent_length=4):
    """
    Builds a SELECT query with the columns in a dataframe.
    :param df: A dataframe.
    :param quote: Quote char to surround the values with. For Oracle, it is '.
    :param table_name: Name of the `TABLE` to use the SELECT query.
    :param join_by: Join each row in the dataframe using UNION or UNION ALL.
    :param indent_length: Indent length in the SQL.
    :return: A SQL query string.

    """
    indent = "  "
    def s(x):
        columns = ""
        for k in x.index.values:
            columns += f'{quote}{x[k]}{quote} {k}, '
        return f'{indent}SELECT {columns[:-2]} FROM DUAL'

    result = f'\n{indent}{join_by}\n'.join(df.apply(lambda r: s(r), axis=1).values)

    return f"WITH {table_name} AS {{ \n{result}\n }}\n SELECT * FROM {table_name}"


