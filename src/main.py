from fastapi import FastAPI
from agent_workforce.chat_agent import ChatAgent

app: FastAPI = FastAPI()

# TODO implement singleton pattern
chat_agent = ChatAgent()

@app.get("/")
def root():
    return {"Home Page"}


@app.post(path="/chat/{message}")
async def chat(message: str):
    return await chat_agent.chat(message)


# add more endpoints if needed
