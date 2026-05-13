from fastapi import FastAPI
from agent_workforce.agent import chat as chat_completion

app: FastAPI = FastAPI()


@app.get("/")
def root():
    return {"Home Page"}


@app.post(path="/chat/{message}")
async def chat(message: str):
    return await chat_completion(message)


# add more endpoints if needed
