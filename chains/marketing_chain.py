
import os
from langchain_openai import ChatOpenAI

from langchain_core.prompts import ChatPromptTemplate
from config import MODEL_NAME, OPEN_API_KEY, PROMPTS_DIR 

from schemas.output_schema import   MarketingStrategy



class MarketingChain:
    def __init__(self,tone:str = "Professional"):
        self.tone = tone
        self.llm = ChatOpenAI(
            model = MODEL_NAME,
            temperature=0.2,
            openai_api_key = OPEN_API_KEY
        )

    def run(self,business_task: str) -> dict:

        prompt_path = os.path.join(PROMPTS_DIR, "marketing_prompt.txt")
        system_prompt_path = os.path.join(PROMPTS_DIR, "system_prompt.txt")

        with open(prompt_path, 'r') as file:
            user_prompt_text = file.read()

        with open(system_prompt_path, 'r') as file:
            system_prompt_text = file.read()

        prompt= ChatPromptTemplate.from_messages([
            ("system", system_prompt_text),
            ("user", user_prompt_text)
        ])  
       # cancel prompt print from output terminal
       # print('prompt', prompt)

        chain = prompt | self.llm.with_structured_output(MarketingStrategy)
#   calling the chain
        print(f"[CHIAIN] Running marketing chain  with Tone:{self.tone}")

        enhanced_task = f"{business_task}\n\n Ensure the strategy reflects a {self.tone} brand voice."
        result = chain.invoke({"business_task": enhanced_task})
        # cancel result print
       # print(f"result: {result}")
        return result.model_dump()
    