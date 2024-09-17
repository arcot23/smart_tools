
def run(sql, host, port, service_name, sid, user, password):

    """
    Runs a sql using the connection params.
    :param sql: Sql query to run.
    :param host: Host. e.g., abc.net
    :param port: Port. e.g., 1521
    :param service_name: Service name. If passed, param `sid` will not be used. e.g., PROD
    :param sid: SID. e.g., PROD
    :param user: User name. e.g., ro_user
    :param password: Password. e.g., A+b2><Xg
    :return: Pandas dataframe containing the resultset of the sql query.
    """

    import sqlalchemy
    import oracledb
    import pandas as pd

    if service_name is not None:
        driver = "oracle+oracledb"
        cp = oracledb.ConnectParams(
            host= host,
            port= int(port),
            service_name= service_name
        )
    elif sid is not None:
        driver = "oracle+cx_oracle"
        cp = oracledb.ConnectParams(
            host= host,
            port= int(port),
            sid= sid
        )

    connection_url = sqlalchemy.URL.create(
        driver,
        host= cp.get_connect_string(),
        username= user,
        password= password
    )

    _conn = sqlalchemy.create_engine(connection_url)

    df = pd.read_sql(sql, _conn)

    return df