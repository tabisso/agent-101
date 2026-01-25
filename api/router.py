
# import json
# import asyncio  
# from fastapi import APIRouter, Form
# from fastapi.responses import StreamingResponse
# from agent.executor import AgentExecutor    

# router = APIRouter()


# @router.post("/run-agent")
# async def run_agent(
#     business_task: str = Form(...),
#     tone: str = Form(...),
#     depth: str = Form(...),
# ):  
#     executor = AgentExecutor(tone=tone, depth=depth)

#     async def event_generator():
#         async for event in executor.run_stream(business_task):
#             yield f"data: {json.dumps(event)}\n\n"  

#     return StreamingResponse(event_generator(), media_type="text/event-stream")



import json
import asyncio
from fastapi import APIRouter, Form
from fastapi.responses import StreamingResponse
from agent.executor import AgentExecutor

router = APIRouter()

@router.post("/run-agent")
async def run_agent(
    business_task: str = Form(...),
    tone: str = Form(...),
    depth: str = Form(...),
):
    executor = AgentExecutor(tone=tone, depth=depth)

    async def event_generator():
        try:
            # quick ping so browser knows stream started
            yield f"data: {json.dumps({'type':'log','content':{'step':'SYSTEM','message':'Stream started'}})}\n\n"
            await asyncio.sleep(0.05)

            async for event in executor.run_stream(business_task):
                yield f"data: {json.dumps(event, default=str)}\n\n"

            yield f"data: {json.dumps({'type':'log','content':{'step':'SYSTEM','message':'Stream finished'}})}\n\n"

        except Exception as e:
            yield f"data: {json.dumps({'type':'log','content':{'step':'ERROR','message': str(e)}})}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        },
    )
