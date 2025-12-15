# functions/main.py
from firebase_functions import https_fn, options
from firebase_admin import initialize_app
import openai
import os

# Initialize Firebase Admin (for database/auth checks if needed later)
initialize_app()

# API Configuration
# In production, use: firebase functions:secrets:set OPENAI_API_KEY
# For local testing, you can hardcode temporarily or use .env files
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY") 

@https_fn.on_request(
    cors=options.CorsOptions(cors_origins="*", cors_methods=["post"]),
    region="us-central1",
    secrets=["OPENAI_API_KEY"] # This automatically loads the key from Firebase Secrets
)
def generate_response(req: https_fn.Request) -> https_fn.Response:
    """
    This function acts as the 'Gatekeeper'.
    1. It receives the prompt from the frontend.
    2. It calls OpenAI securely.
    3. It returns the answer.
    """
    
    # 1. Parse the request
    try:
        data = req.get_json()
        user_prompt = data.get("prompt")
        
        if not user_prompt:
            return https_fn.Response("Missing 'prompt' in request body", status=400)

    except Exception as e:
        return https_fn.Response(f"Error parsing JSON: {str(e)}", status=400)

    # 2. Call OpenAI (The "Brain")
    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    
    try:
        completion = client.chat.completions.create(
            model="gpt-4", # or gpt-3.5-turbo
            messages=[
                {"role": "system", "content": "You are a helpful corporate AI assistant. Answer concisely."},
                {"role": "user", "content": user_prompt}
            ]
        )
        
        ai_answer = completion.choices[0].message.content
        
        # 3. Return the answer
        return https_fn.Response(ai_answer, status=200)

    except Exception as e:
        return https_fn.Response(f"OpenAI Error: {str(e)}", status=500)