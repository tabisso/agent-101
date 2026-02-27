from fastapi import FastAPI 
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

from api.middleware import RateLimitMiddleware
from api.router import router

app = FastAPI(title="Business AI Agent", version='1.0.0')

#Include routers
app.include_router(router)

# Include middleware
# Tip: 60 is a sane starting point; tune later.
app.add_middleware(RateLimitMiddleware, requests_per_minute=1)


#Mount UI
app.mount("/app",StaticFiles(directory="ui", html=True), name="ui")


@app.get("/")
async def root():
    return RedirectResponse(url= "/app")

if __name__== "__main__":
    print("Starting AI Server...")
    print("Open http://localhost:8000/app in your browser")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
