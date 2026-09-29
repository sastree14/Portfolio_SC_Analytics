import oracledb

def connect(user: str, password: str, dsn: str):
    return oracledb.connect(user=user, password=password, dsn=dsn)
