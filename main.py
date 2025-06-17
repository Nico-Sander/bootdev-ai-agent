import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

# Get API Key
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# Generate client
client = genai.Client(api_key=api_key)

# Get prompt from command line
try:
    user_prompt = sys.argv[1]
except:
    print("Please provide the prompt as a CLI argument!")
    sys.exit(1)

# Check if verbose output was requested
verbose = False
if "--verbose" in sys.argv[2:]:
    verbose = True

# Store user prompts in a list
messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

# Get the response from the model
response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
)

# Print the response and metadata
if verbose:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

print(f"Answer: {response.text}")

