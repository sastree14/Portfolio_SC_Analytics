from urllib.parse import quote_plus
from sqlalchemy import create_engine

def engine(server: str, database: str, username: str, password: str):
    params = quote_plus(
        f"DRIVER={{ODBC Driver 18 for SQL Server}};"
        f"SERVER={server};DATABASE={database};UID={username};PWD={password};"
        "Encrypt=yes;TrustServerCertificate=no"
    )
    return create_engine(f"mssql+pyodbc:///?odbc_connect={params}", pool_pre_ping=True)
