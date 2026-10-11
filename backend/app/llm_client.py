import os
from dotenv import load_dotenv
from openai import OpenAI, AuthenticationError, APIError, APIConnectionError, RateLimitError
from fastapi import HTTPException

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY environment variable is not set in .env")

client = OpenAI(api_key=api_key)

LLM_PROVIER = os.getenv("LLM_PROVIDER", "openai")  # Default to OpenAI if not specified

def generate_output(system_prompt: str, user_text: str) -> dict:
    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
    if LLM_PROVIER == "openai":
        return _execute_chat_completion(system_prompt, user_text, model)
    else:
        raise HTTPException(status_code=400, detail=f"Unsupported LLM provider: {LLM_PROVIER}")

def _execute_chat_completion(system_prompt: str, user_text: str, model) -> dict:
    try:
        response = client.chat.completions.create(
            model = model,
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_text},
            ],
            temperature=0.7,
            max_tokens=100,
        )
        return {
            "content": response.choices[0].message.content,
            "tokens": response.usage.total_tokens,
            "model": response.model,
        }
    except AuthenticationError as e:
        raise HTTPException(status_code=401, detail=f"Authentication failed: {e}")
    except RateLimitError as e:
        raise HTTPException(status_code=429, detail=f"Rate limit exceeded: {e}")
    except APIConnectionError as e:
        raise HTTPException(status_code=503, detail=f"Cannot reach OpenAI API: {e}")
    except APIError as e:
        raise HTTPException(status_code=502, detail=f"OpenAI service error: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")