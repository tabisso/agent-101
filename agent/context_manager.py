# create class ContextManager:


import io

from fastapi import UploadFile
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader

from rag.vector_strore import VectorStore 



class ContextManager:

    MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
    ALLOWED_TYPES = {'application/pdf', 'text/plain'} 

    def __init__(self):
        self.vector_store = VectorStore()

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=800, 
            chunk_overlap=150
            )


    async def ingest_file(self, file: UploadFile):

        #1 validation of file 
        if file.content_type not in self.ALLOWED_TYPES:
            raise ValueError(f"Unsupported file type")
        content = await file.read()
        if len(content) > self.MAX_FILE_SIZE:
            raise ValueError(f"File size exceeds the maximum limit of 5MB") 
        
        #2 text extraction
        raw_text = "" 
        try:
            if file.content_type == 'application/pdf':
                reader=PdfReader(io.BytesIO(content))

                for i, page in enumerate(reader.pages):
                    text = page.extract_text()
                    if text:
                        raw_text += f"\n--- Page {i+1} ---\n{text}"
                    
            else:
                raw_text = content.decode('utf-8')
           


        except:
            raise ValueError(f"Failed to extract text from file of type")
        

        #3 text splitting
        chunks = self.splitter.create_documents([raw_text], 
         metadatas=[{"source": file.filename, "page": i +1}]
         
         )

        #4 add to vector store
        #self.vector_store.clear()  # Clear existing context before adding new documents
        self.vector_store.add_documents(chunks)

        #optional return 
        return len(chunks)