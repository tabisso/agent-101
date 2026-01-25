

import time
import asyncio

from chains.bussiness_chain import BusinessChain


class AgentExecutor:
    def __init__(self, tone: str = "Professional", depth:
                 str = "normal"):
        self.tone = tone
        self.depth = depth

    async def run_stream(self, business_task: str):

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


            
           