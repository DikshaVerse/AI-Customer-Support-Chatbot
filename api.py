from fastapi import FastAPI
from pydantic import BaseModel
from model import chat

app=FastAPI()


# request schema
class Query(BaseModel):
    text: str

# API endpoint
@app.post("/chat")
def chat_api(query: Query):
    return chat(query.text)