import os
from fastapi import FastAPI
from .models import TaskRequest, TaskResponse, HealthResponse
from .service import process_task

app = FastAPI(
    title="AI Workbench REST API",
    description="Modular REST service for text processing using OpenAI",
    version="1.0.0"
)

@app.get("/health", tags=["Health"])
def health():
    health_response = HealthResponse(
        model=os.getenv("OPENAI_MODEL"),
        provider=os.getenv("LLM_PROVIDER")
    )
    return health_response

@app.post("/tasks/summarize", response_model=TaskResponse, tags=["Tasks"])
def summarize(request: TaskRequest):
    return process_task("summarize", request.text)

@app.post("/tasks/rewrite", response_model=TaskResponse, tags=["Tasks"])
def rewrite(request: TaskRequest):
    return process_task("rewrite", request.text)

@app.post("/tasks/key-points", response_model=TaskResponse, tags=["Tasks"])
def key_points(request: TaskRequest):
    return process_task("key_points", request.text)

@app.post("/tasks/explain", response_model=TaskResponse, tags=["Tasks"])
def explain(request: TaskRequest):
    return process_task("explain", request.text)

@app.post("/tasks/generate-questions", response_model=TaskResponse, tags=["Tasks"])
def generate_questions(request: TaskRequest):
    return process_task("generate_questions", request.text)

@app.post("/tasks/translate-tamil", response_model=TaskResponse, tags=["Tasks"])
def translate_tamil(request: TaskRequest):
    return process_task("translate_tamil", request.text)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)