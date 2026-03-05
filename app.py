from fastapi import FastAPI
from langchain_openai import ChatOpenAI

app = FastAPI()

llm = ChatOpenAI(model="gpt-4o-mini")

@app.get("/ask")
def ask(question: str):

    response = llm.invoke(question)

    return {"answer": response.content}
