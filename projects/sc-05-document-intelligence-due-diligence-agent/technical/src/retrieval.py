from qdrant_client import QdrantClient
from qdrant_client.models import Filter

def search(client: QdrantClient, collection: str, vector: list[float], limit: int=5):
    return client.query_points(collection_name=collection,query=vector,query_filter=Filter(must=[]),limit=limit).points
