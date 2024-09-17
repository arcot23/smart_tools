from smart_tools.common import database

conn = {
    'host': 'abc.net',
    'port': '1521',
    'service_name': None,
    'sid': 'DEV',
    'user': 'ro_user',
    'password': 'abc123'
}

database.run("select * from table", **conn)