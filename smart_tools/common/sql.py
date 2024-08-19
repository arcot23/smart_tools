

def build_sql_from_df(df, quote=",", table_name='TABLE', join_by="UNION ALL", indent_length=4):
    indent = "  "
    def s(x):
        columns = ""
        for k in x.index.values:
            columns += f'{quote}{x[k]}{quote} {k}, '
        return f'{indent}SELECT {columns[:-2]} FROM DUAL'

    result = f'\n{indent}{join_by}\n'.join(df.apply(lambda r: x(r), axis=1).values)

    return f"WITH {table_name} AS {{ \n{result}\n }}\n SELECT * FROM {table_name}"


