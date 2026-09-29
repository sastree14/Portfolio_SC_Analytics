from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

def build_index(texts: list[str]):
    model=SentenceTransformer("all-MiniLM-L6-v2")
    vectors=model.encode(texts,normalize_embeddings=True).astype("float32")
    index=faiss.IndexFlatIP(vectors.shape[1]); index.add(vectors)
    return model,index,vectors
