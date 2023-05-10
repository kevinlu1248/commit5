# fastapi app that generates a commit message based on a diff
from fastapi import FastAPI
from core.generator import CommitMessageGenerator

app = FastAPI()
generator = CommitMessageGenerator()

@app.get("/")
def read_root():
    return "Hello, World! Please enter a diff to generate a commit message via POST."

@app.post("/")
def generate_commit_message(diff: str):
    return generator(diff)
