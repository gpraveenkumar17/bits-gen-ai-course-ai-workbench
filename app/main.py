from fastapi import FastAPI
from .models import TaskRequest, TaskResponse
from .service import execute_task

app = FastAPI(
    title="AI Workbench REST API",
    description="Modular REST service for text processing using OpenAI",
    version="1.0.0"
)

@app.get("/health", tags=["Health"])
def health():
    return {"status": "healthy"}

@app.post("/tasks/summarize", response_model=TaskResponse, tags=["Tasks"])
def summarize(request: TaskRequest):
    return execute_task("summarize", request.text)

@app.post("/tasks/rewrite", response_model=TaskResponse, tags=["Tasks"])
def rewrite(request: TaskRequest):
    return execute_task("rewrite", request.text)

@app.post("/tasks/key-points", response_model=TaskResponse, tags=["Tasks"])
def key_points(request: TaskRequest):
    return execute_task("key_points", request.text)

@app.post("/tasks/explain", response_model=TaskResponse, tags=["Tasks"])
def explain(request: TaskRequest):
    return execute_task("explain", request.text)

@app.post("/tasks/generate-questions", response_model=TaskResponse, tags=["Tasks"])
def generate_questions(request: TaskRequest):
    return execute_task("generate_questions", request.text)

@app.post("/tasks/translate-tamil", response_model=TaskResponse, tags=["Tasks"])
def translate_tamil(request: TaskRequest):
    return execute_task("translate_tamil", request.text)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)