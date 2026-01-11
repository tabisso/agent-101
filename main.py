from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn

app = FastAPI(title="Business AI Agent", version='1.0.0')

@app.get("/")
async def root():
    return RedirectResponse(url= "/app")

if __name__== "__main__":
    print("Starting AI Server...")
    print("Open http://localhost:8000/app in your browser")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
