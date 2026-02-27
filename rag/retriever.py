


from rag.vector_strore import VectorStore


class RagRetriever:

    def __init__(self):
        self.vector_store = VectorStore()


    def retrieve(self, query: str, k: int = 5):
        """Retrieve relevant documents from the vector store based on the query."""

        docs = self.vector_store.similarity_search(query, k=k)
        
        if not docs:
            return ""
        #fromat chunks to string
        formatted_docs = []
        for i, doc in enumerate(docs):
            source = doc.metadata.get("source", "unknown")
            page = doc.metadata.get("page", "?")
            formatted_docs.append(
                f"---CHUNK {i+1} (Source: {source}, Page: {page})---\n{doc.page_content}\n"
            )

        return "\n\n".join(formatted_docs)
          
        




    