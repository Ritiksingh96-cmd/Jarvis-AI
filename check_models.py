import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=KEY, base_url="https://openrouter.ai/api/v1")

try:
    print("Testing gpt-4...")
    client.chat.completions.create(model="openai/gpt-4", messages=[{"role":"user","content":"hi"}])
    print("✅ GPT-4 Works")
except Exception as e:
    print(f"❌ GPT-4 Failed: {e}")

try:
    print("Testing gpt-3.5-turbo...")
    client.chat.completions.create(model="openai/gpt-3.5-turbo", messages=[{"role":"user","content":"hi"}])
    print("✅ GPT-3.5 Works")
except Exception as e:
    print(f"❌ GPT-3.5 Failed: {e}")
