"""
API KEY CHECKER
"""
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv("OPENAI_API_KEY")

print(f"Testing Key: {KEY[:15]}...")

try:
    client = OpenAI(api_key=KEY)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Test"}],
        max_tokens=5
    )
    print("\n✅ SUCCESS! The key is working.")
    print(f"Response: {response.choices[0].message.content}")
except Exception as e:
    print("\n❌ FAILURE! The key is invalid.")
    print(f"Error Message: {str(e)}")
