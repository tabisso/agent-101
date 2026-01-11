import os
from dotenv import load_dotenv

load_dotenv()
OPEN_API_KEY = os.getenv("open_api_key")

if not OPEN_API_KEY:
    raise ValueError("OPEN_API_KEY is not set in the environment variables.")   

MODEL_NAME = "gpt-4o-mini"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROMPTS_DIR = os.path.join(BASE_DIR, "prompts")
DATA_DIR = os.path.join(BASE_DIR, "data")