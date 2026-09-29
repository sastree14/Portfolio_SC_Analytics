from databricks import sql

def connect(server_hostname: str, http_path: str, access_token: str):
    return sql.connect(
        server_hostname=server_hostname,
        http_path=http_path,
        access_token=access_token,
    )
