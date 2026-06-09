from agent_workforce.chat_agent import ChatAgent
from utils.webhook import handle_webhook

from fastapi import FastAPI, Request
import httpx

app: FastAPI = FastAPI()

# TODO implement singleton pattern
chat_agent = ChatAgent()

@app.get("/")
def root():
    return {"Home Page"}


@app.post(path="/telegram/webhook")
async def chat(request: Request):
    await handle_webhook(
        request_body=await request.json(),
        request_headers=request.headers,
        agent=chat_agent,
    )
    return


# add more endpoints if needed
