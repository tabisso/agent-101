
#embedding functions

from langchain_openai import OpenAIEmbeddings

from config import OPEN_API_KEY



class Embedder:
    _instance = None

    @staticmethod
    def get_instance():
        if Embedder._instance is None:
            Embedder._instace = OpenAIEmbeddings( 
                model = "text-embedding-3-small",
                openai_api_key = OPEN_API_KEY
            )
            

        
        return  Embedder._instace
        
