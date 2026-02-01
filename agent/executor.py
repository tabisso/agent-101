

import time
import asyncio

from agent.planner import ExecutionPlanner

from chains.business_chain import BusinessChain
from chains.marketing_chain import MarketingChain
from schemas.output_schema import FinalOutput
from chains.task_chain import TaskChain
from chains.email_chain import EmailChain


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
                yield create_log("EXECUTION", "Running Business Analysis...")
                chain = BusinessChain(tone=self.tone)
                final_output_data["business_overview"] = await asyncio.to_thread(chain.run, business_task);



            # Marketing chain
            if "marketing_strategy" in steps:
                yield create_log("EXECUTION", "Running Marketing Strategy...")
                
                chain = MarketingChain(tone=self.tone)
                final_output_data["marketing_strategy"] = await asyncio.to_thread(chain.run, business_task);
            

            # Email chain
            if "email_campaign" in steps:
                yield create_log("EXECUTION", "Running Email Campaign Chain...")

                count = 3


                chain = EmailChain(tone=self.tone, count=count)
                final_output_data["email_campaign"] = await asyncio.to_thread(chain.run, business_task);
            # Task chain
            if "task_breakdown" in steps:
                yield create_log("EXECUTION", "Running Task Breakdown Chain...")
                chain = TaskChain(tone=self.tone)
                final_output_data["task_breakdown"] = await asyncio.to_thread(chain.run, business_task);

                




            #Review the output -- TO DO


            #4 Validaton -- TO DO



            try:
                 final_output_obj= FinalOutput(**final_output_data)

                 validated_data = final_output_obj.model_dump()
                 yield create_log("SUCCESS", "Final output validated successfully.")
                 yield {
                     "type": "result",
                     "content": validated_data
                 }
            except Exception as e:
                    yield create_log("ERROR", f"Validation error: {str(e)}")
                    raise e

    

        

          


           
            #little twiak 
            
            # result = chain.run(business_task)
           
            # yield {
            #     "type": "result",
            #     "content": {    
                    
            #         "business_overview": result,
            #     }
            # }


            
           