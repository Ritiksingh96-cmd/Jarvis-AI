"""
OPENROUTER KEY CHECKER
"""
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv("OPENAI_API_KEY")

print(f"Testing OpenRouter Key: {KEY[:15]}...")

try:
    client = OpenAI(
        api_key=KEY,
        base_url="https://openrouter.ai/api/v1"
    )
    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Test"}],
        max_tokens=5
    )
    print("\n✅ SUCCESS! It is an OpenRouter key.")
    print(f"Response: {response.choices[0].message.content}")
except Exception as e:
    print("\n❌ FAILURE! Not working with OpenRouter either.")
    print(f"Error Message: {str(e)}")
