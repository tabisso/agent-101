
#embedding functions

from langchain_openai import OpenAIEmbeddings
from config import OPENAI_API_KEY


class Embedder:
    _instace = None

    @staticmethod
    def get_instance():
        if Embedder.isinstancece is None:
            Embedder._instace = OpenAIEmbeddings( 
                model = "text-embedding-3-small",
                openai_api_key = OPENAI_API_KEY
            )
            

        
        return  Embedder._instace
        
