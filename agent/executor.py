

import time
import asyncio

from agent.planner import ExecutionPlanner
from chains.bussiness_chain import BusinessChain


class AgentExecutor:
    def __init__(self, tone: str = "Professional", depth:
                 str = "normal"):
        self.tone = tone
        self.depth = depth

    async def run_stream(self, business_task: str):
            
            #Planning
            planner = ExecutionPlanner(tone=self.tone, depth=self.depth)
            plan = await asyncio.to_thread(planner.generate_plan, business_task)

            steps = plan.get("steps", [])

            yield {
                "type": "log",
                "content": {    
                    "step": "START",
                    "message": f"Agent started with tone: {self.tone} and depth: {self.depth}",
                    "timestamp": time.time()
                }
            }
            yield {
                "type": "log",
                "content": {    
                    "step": "EXECUTION",
                    "message": "Running Business Chain...",
                    "timestamp": time.time()
                }
            }


            chain = BusinessChain(tone=self.tone)
            #little twiak 
            
            #result = chain.run(business_task)
            result = await asyncio.to_thread(chain.run, business_task)

            yield {
                "type": "result",
                "content": {    
                    
                    "business_overview": result,
                }
            }


            
           