
import json
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
        async for event in executor.run_stream(business_task):
            yield f"data: {json.dumps(event)}\n\n"  

    return StreamingResponse(event_generator(), media_type="text/event-stream")



