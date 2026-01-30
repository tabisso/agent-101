

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
            
            def create_log(step, message):
                return {
                    "type": "log",
                    "content": {
                        "step": step,
                        "message": message,
                        "timestamp": time.time()
                    }
                }
            
            #Planning
            planner = ExecutionPlanner(tone=self.tone, depth=self.depth)
            plan = await asyncio.to_thread(planner.generate_plan, business_task)

            steps = plan.get("steps", [])
            yield create_log("PLANNING", f"Decided steps: {steps}")

            #2. Execution
            final_output_data = {}
            #Business chain
            if "business_analysis" in steps:
                yield create_log("EXECUTION", "Starting Business Analysis...")
                chain = BusinessChain(tone=self.tone)
                final_output_data["business_overview"] = await asyncio.to_thread(chain.run, business_task);
        

          


           
            #little twiak 
            
            # result = chain.run(business_task)
           
            # yield {
            #     "type": "result",
            #     "content": {    
                    
            #         "business_overview": result,
            #     }
            # }


            
           