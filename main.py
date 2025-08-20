import os
import sys
from dotenv import load_dotenv
from google import genai 
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():
    if len(sys.argv) == 1:
        print("Must provide one argument")
        sys.exit(-1)
    
    if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
        verbose = True
    else:
        verbose = False

    user_prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )

    print(response.text)
    if verbose:
        print("User prompt:", user_prompt)
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    

if __name__ == "__main__":
    main()
