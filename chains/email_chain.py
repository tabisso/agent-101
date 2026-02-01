
import os
from typing import List
from langchain_openai import ChatOpenAI

from langchain_core.prompts import ChatPromptTemplate
from config import MODEL_NAME, OPEN_API_KEY, PROMPTS_DIR 
from schemas.output_schema import BussinessOverview, EmailList 


class EmailChain:
    def __init__(self,tone:str = "Professional", count:int =3):
        self.tone = tone
        self.count = count
        self.llm = ChatOpenAI(
            model = MODEL_NAME,
            temperature=0.5,
            openai_api_key = OPEN_API_KEY
        )

    def run(self,business_task: str) -> List[dict]:

        prompt_path = os.path.join(PROMPTS_DIR, "email_prompt.txt")
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

        chain = prompt | self.llm.with_structured_output(EmailList)
#   calling the chain
        print(f"[CHIAIN] Draffting {self.count} Emails in tone {self.tone}")

        enhanced_task = f"{business_task}\n\n Write {self.count} emails. Use a {self.tone} tone."
        result = chain.invoke({"business_task": enhanced_task})
       
        return [email.model_dump() for email in result.emails] 
    