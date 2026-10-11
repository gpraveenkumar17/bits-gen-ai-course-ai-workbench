import os
import sys
from dotenv import load_dotenv
from openai import OpenAI, AuthenticationError, APIError, APIConnectionError

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Error: OPENAI_API_KEY environment variable is not set.")
    sys.exit(1)

client = OpenAI(api_key=api_key)
MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

print("Sending prompt: Explain the concept of theory of relative in simple terms?")
try:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Be concise and clear in your explanations."},
            {"role": "user", "content": "Explain the concept of theory of relative in simple terms."}], 
        max_tokens=100,
        temperature=0.7)
    
    print("Response:", response.choices[0].message.content)
    print("Tokens used:", response.usage.total_tokens)

except AuthenticationError:
    print("Authentication failed. Please check your API key.")
except APIError as e:
    print(f"API error occurred: {e}")
except APIConnectionError:
    print("Failed to connect to the API. Please check your network connection.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
