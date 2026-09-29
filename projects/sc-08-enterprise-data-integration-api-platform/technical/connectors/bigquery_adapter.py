from google.cloud import bigquery

def client(project: str) -> bigquery.Client:
    return bigquery.Client(project=project)

def query_dataframe(project: str, sql: str):
    return client(project).query(sql).result().to_dataframe()
