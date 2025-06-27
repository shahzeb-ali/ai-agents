# agent_memory.py

import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from typing import List, Optional

class AgentMemory:
    def __init__(self, user_id="default", persist_path="./chroma_data"):
        self.collection_name = f"agent_memory_{user_id}"
        self.client = chromadb.PersistentClient(path=persist_path)
        self.embedding_fn = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
        self.collection = self.client.get_or_create_collection(
            name=self.collection_name,
            embedding_function=self.embedding_fn
        )

    def add(self, content: str, metadata: Optional[dict] = None, uid: Optional[str] = None):
        uid = uid or str(hash(content))
        self.collection.add(
            documents=[content],
            metadatas=[metadata or {}],
            ids=[uid]
        )

    def search(self, query: str, n_results: int = 5) -> List[dict]:
        try:
            results = self.collection.query(query_texts=[query], n_results=n_results)
            return [
                {
                    "id": id_,
                    "document": doc,
                    "metadata": meta,
                    "distance": dist
                }
                for id_, doc, meta, dist in zip(
                    results["ids"][0],
                    results["documents"][0],
                    results["metadatas"][0],
                    results["distances"][0]
                )
            ]
        except Exception as e:
            print(f"[Search error]: {e}")
            return []

    def clear(self):
        self.client.delete_collection(name=self.collection_name)
