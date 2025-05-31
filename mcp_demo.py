import os
from dotenv import load_dotenv
import openai

# Remove system environment variable if present and load it from .env file (not uploaded to GitHub for security)
os.environ.pop("OPENAI_API_KEY", None)
load_dotenv(override=True)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("No se ha encontrado OPENAI_API_KEY en el entorno o en .env")

# Initialize OpenAI client
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# 1. Define the context
CONTEXT = """
You are a business assistant for Ahead Labs, S.L. 
You help users with IT, cloud, and automation questions.
Respond always in a clear and professional tone, in Spanish.
"""

# 2. Get the user input
user_input = input("What is your question? ")

# 3. Build the MCP prompt
def build_prompt(context, user_message):
    return f"""[CONTEXT]\n{context}\n\n[USER]\n{user_message}\n\n[INSTRUCTION]\nAnswer concisely."""

# 4. Call the LLM
prompt = build_prompt(CONTEXT, user_input)
print(f"\nPrompt sent to LLM: {prompt}")
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": CONTEXT},
        {"role": "user", "content": prompt}
    ]
)

print("\nResponse from LLM:")
print(response.choices[0].message.content)
