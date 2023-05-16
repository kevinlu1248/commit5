# fastapi app that generates a commit message based on a diff
from fastapi import FastAPI
from generator import CommitMessageGenerator
from pydantic import BaseModel

app = FastAPI()
generator = CommitMessageGenerator()

@app.get("/")
def read_root():
    return "Hello, World! Please enter a diff to generate a commit message via POST."

class CommitMessageGeneratorRequest(BaseModel):
    diff: str

@app.post("/")
def generate_commit_message(request: CommitMessageGeneratorRequest):
    return generator(request.diff)
