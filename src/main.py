from fastapi import FastAPI

app: FastAPI = FastAPI()


@app.get("/")
def root():
    return {"Home Page"}


@app.post(path="/chat/{message}")
def chat(message: str):
    return message

# add more endpoints if needed
