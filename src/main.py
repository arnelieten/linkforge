from fastapi import FastAPI, Request
from agent_workforce.chat_agent import ChatAgent
from utils.webhook_auth import authenticate_user_id, authenticate_header_secret

app: FastAPI = FastAPI()

# TODO implement singleton pattern
chat_agent = ChatAgent()

@app.get("/")
def root():
    return {"Home Page"}


@app.post(path="/telegram/webhook")
async def chat(request: Request):
    request_body = await request.json()
    request_header = request.headers
    if authenticate_user_id(request_body=request_body) and authenticate_header_secret(request_header=request_header):
        message = request_body.get("message")
        text = message.get("text")
        response = await chat_agent.chat(text)
        print(response)


# add more endpoints if needed
