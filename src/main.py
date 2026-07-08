from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
import httpx

from agent_workforce.super_agent import SuperAgent
from config import BOTFATHER_API_KEY
from database import init_tables
from telegram.client import TelegramClient
from telegram.webhook import handle_webhook


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_tables()
    async with httpx.AsyncClient() as http_client:
        app.state.telegram_client = TelegramClient(
            api_key=BOTFATHER_API_KEY, http_client=http_client
        )
        app.state.super_agent = SuperAgent()
        yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def home():
    return FileResponse("src/index.html")


@app.post(path="/telegram/webhook")
async def chat(request: Request):
    await handle_webhook(
        request_body=await request.json(),
        request_headers=request.headers,
        agent=request.app.state.super_agent,
        telegram_client=request.app.state.telegram_client,
    )
    return
