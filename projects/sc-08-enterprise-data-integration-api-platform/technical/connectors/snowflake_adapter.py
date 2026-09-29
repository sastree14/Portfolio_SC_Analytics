from __future__ import annotations
import snowflake.connector

def connect(account: str, user: str, password: str, warehouse: str, database: str, schema: str):
    return snowflake.connector.connect(
        account=account,
        user=user,
        password=password,
        warehouse=warehouse,
        database=database,
        schema=schema,
    )
