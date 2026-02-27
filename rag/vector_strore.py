# creating vector store for agent context
#import os and embedder
import os

import chromadb
from config import BASE_DIR

from langchain_chroma import Chroma 
from langchain_core.documents import Document
from typing import List

from rag.embedder import Embedder


class VectorStore:
    
    
    VECTOR_DB_DIR = os.path.join(BASE_DIR, "vector_db_chroma")

    def __init__(self):
        self.embedding_function = Embedder.get_instance()
        self.db = Chroma(
             persist_directory=self.VECTOR_DB_DIR,
             embedding_function=self.embedding_function 
        )


        #add doc to vector store
    def add_documents(self, documents: list[Document]):
        if not documents:
            return
        self.db.add_documents(documents)
        print(f"Added {len(documents)} documents to vector store")
    

    #search doc in db vector store
    def similarity_search(self, query: str, k: int = 5) -> List[Document]:
        results = self.db.similarity_search(query, k=k)
        #print(f"Retrieved {len(results)} documents from vector store for query: {query}")
        return results
