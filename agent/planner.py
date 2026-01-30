

#Planner shcemas
import os
from langchain_openai import ChatOpenAI

from langchain_core.prompts import ChatPromptTemplate
from config import MODEL_NAME, OPEN_API_KEY, PROMPTS_DIR 
from schemas.output_schema import BussinessOverview  
from pydantic import BaseModel, Field

class ExectutionPlan(BaseModel):
    steps: list[str] = Field(description="List of steps to execute the business plan.")

class ExecutionPlanner:
    def __init__(self, tone: str = "professional", depth: str = "normal"):
        self.tone = tone
        self.depth = depth

        self.llm = ChatOpenAI(
            model = MODEL_NAME,
            temperature=0.02,
            openai_api_key = OPEN_API_KEY
        )


    def generate_plan(self, business_task: str) -> dict:
        prompt_path = os.path.join(PROMPTS_DIR, "planner_prompt.txt")
        system_prompt_path = os.path.join(PROMPTS_DIR, "system_prompt.txt")

        with open(prompt_path, 'r') as file:
            user_prompt_text = file.read()

        with open(system_prompt_path, 'r') as file:
            system_prompt_text = file.read()

        prompt= ChatPromptTemplate.from_messages([
            ("system", system_prompt_text),
            ("user", user_prompt_text)
        ])  

        planner_chain = prompt | self.llm.with_structured_output(ExectutionPlan)

        context_enhanced_task = f"{business_task}\n\n[Context:Tone=${self.tone}, Depth={self.depth} depth]."
        result = planner_chain.invoke({"business_task": context_enhanced_task})
        return result.model_dump()