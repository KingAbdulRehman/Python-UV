from dotenv import load_dotenv
import os
from litellm import completion

load_dotenv()

def main():
    messages = [{"role": "user", "content": "Hello, how are you?"}]
    # api_key = os.getenv("GEMINI_API_KEY")
    response = completion(model="gemini/gemini-1.5-pro", messages=messages)
    print(response['choices'][0]['message']['content'])

if __name__ == "__main__":
    main()
