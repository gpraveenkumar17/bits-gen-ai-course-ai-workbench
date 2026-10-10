from .models import TaskResponse
from .llm_client import generate_output

PROMPTS = {
    "summarize": (
        "Summarize",
        "You are a concise summarizer. Summarize the user's text in 3-5 clear bullet points. Focus on the most important information."
    ),
    "rewrite": (
        "Rewrite",
        "You are a professional editor. Rewrite the user's text in a clear, professional tone. Maintain the original meaning but improve clarity and readability."
    ),
    "key_points": (
        "Key Points",
        "You are an analyst. Extract the key points from the user's text as a numbered list. Each point should be one clear sentence."
    ),
    "explain": (
        "Explain",
        "You are a patient teacher. Explain the user's text in simple terms that a non-expert can understand. Use analogies where helpful."
    ),
    "generate_questions": (
        "Question Generation",
        "You are a helpful assistant. Generate 3 insightful questions about the user's text."
    ),
    "translate_tamil": (
        "Translator (English → Tamil)",
        "You are a skilled translator. Translate the user's text from English to Tamil."
    ),
}

def process_task(task_key: str, text: str) -> TaskResponse:
    if task_key not in PROMPTS:
        raise ValueError(f"Invalid task key: {task_key}. Valid keys are: {list(PROMPTS.keys())}")
    task_name, system_prompt = PROMPTS[task_key]
    result = generate_output(system_prompt=system_prompt, user_text=text)
    
    return TaskResponse(
        task=task_name,
        content=result["content"],
        tokens=result["tokens"],
        model=result["model"]
    )