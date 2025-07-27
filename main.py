import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types





def main():
    
    user_prompt = sys.argv[1]

    
    try:
            
        load_dotenv()

        api_key = os.environ.get("GEMINI_API_KEY")    

        client = genai.Client(api_key=api_key)
        # Define the prompt chain of messages
        messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

        response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages)


        prompt_token_count = response.usage_metadata.prompt_token_count
        response_token_count = response.usage_metadata.candidates_token_count
        
        if len(sys.argv) == 3:
            print(f"User prompt: {user_prompt}")
            print(response.text)
            print(f"Prompt tokens: {prompt_token_count}")
            print(f"Response tokens: {response_token_count}")
        else:
            print(response.text)

    except ValueError as e:
        print("Prompt not present, exiting the program...")
        sys.exit(1)

if __name__ == "__main__":
    main()
