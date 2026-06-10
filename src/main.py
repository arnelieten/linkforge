from contextlib import asynccontextmanager

import httpx
from agent_workforce.chat_agent import ChatAgent
from config import BOTFATHER_API_KEY
from database import init_tables
from telegram.client import TelegramClient
from telegram.webhook import handle_webhook

from fastapi import FastAPI, Request


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_tables()
    async with httpx.AsyncClient() as http_client:
        app.state.telegram_client = TelegramClient(api_key=BOTFATHER_API_KEY, http_client=http_client)
        app.state.chat_agent = ChatAgent()
        yield


app = FastAPI(lifespan=lifespan)


@app.post(path="/telegram/webhook")
async def chat(request: Request):
    await handle_webhook(
        request_body=await request.json(),
        request_headers=request.headers,
        agent=request.app.state.chat_agent,
        telegram_client=request.app.state.telegram_client,
    )
    return
