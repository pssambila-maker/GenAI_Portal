# functions/main.py
from firebase_admin import initialize_app, firestore
import functions_framework
import openai
import anthropic
import os
import json
from flask import jsonify

# Initialize Firebase Admin
initialize_app()
db = firestore.client()

# API Configuration - loaded from Firebase Secrets
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")

# Content filtering keywords
RESTRICTED_KEYWORDS = ["password", "ssn", "api key", "credit card", "private key"]

def validate_content(text):
    """Check for sensitive content"""
    text_lower = text.lower()
    for keyword in RESTRICTED_KEYWORDS:
        if keyword in text_lower:
            return False, f"Content contains restricted keyword: {keyword}"
    return True, ""

@functions_framework.http
def generate_response(request):
    """
    Main AI generation endpoint
    Supports both OpenAI and Anthropic models
    """

    # Enable CORS
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    headers = {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json'
    }

    # Verify authentication
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return (jsonify({"error": "Unauthorized"}), 401, headers)

    # Parse request
    try:
        data = request.get_json()
        user_id = data.get("userId")
        prompt = data.get("prompt")
        model = data.get("model", "gpt-4")
        conversation_id = data.get("conversationId")

        if not prompt or not user_id:
            return (jsonify({"error": "Missing required fields"}), 400, headers)

    except Exception as e:
        return (jsonify({"error": f"Invalid request: {str(e)}"}), 400, headers)

    # Content validation
    is_valid, reason = validate_content(prompt)
    if not is_valid:
        log_usage(user_id, model, prompt, None, False, reason)
        return (jsonify({"error": reason, "blocked": True}), 403, headers)

    # Route to appropriate AI service
    try:
        if model.startswith("gpt"):
            response = call_openai(prompt, model)
        elif model.startswith("claude"):
            response = call_anthropic(prompt, model)
        else:
            return (jsonify({"error": "Unsupported model"}), 400, headers)

        # Save to conversation history
        if conversation_id:
            save_message(user_id, conversation_id, "user", prompt)
            save_message(user_id, conversation_id, "assistant", response)

        # Log usage
        log_usage(user_id, model, prompt, response, True)

        return (jsonify({"response": response, "success": True}), 200, headers)

    except Exception as e:
        log_usage(user_id, model, prompt, None, False, str(e))
        return (jsonify({"error": f"AI Error: {str(e)}", "success": False}), 500, headers)

def call_openai(prompt, model):
    """Call OpenAI API"""
    client = openai.OpenAI(api_key=OPENAI_API_KEY)

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant for healthcare professionals. Be concise, accurate, and professional."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,
        temperature=0.7
    )

    return completion.choices[0].message.content

def call_anthropic(prompt, model):
    """Call Anthropic Claude API"""
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    message = client.messages.create(
        model=model if model.startswith("claude-") else "claude-3-5-sonnet-20241022",
        max_tokens=1000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return message.content[0].text

def save_message(user_id, conversation_id, role, content):
    """Save message to Firestore"""
    try:
        db.collection('users').document(user_id) \
            .collection('conversations').document(conversation_id) \
            .collection('messages').add({
                'role': role,
                'content': content,
                'timestamp': firestore.SERVER_TIMESTAMP
            })
    except Exception as e:
        print(f"Error saving message: {str(e)}")

def log_usage(user_id, model, prompt, response, success, error=None):
    """Log usage to Firestore for analytics"""
    try:
        db.collection('usage_logs').add({
            'userId': user_id,
            'model': model,
            'promptLength': len(prompt),
            'responseLength': len(response) if response else 0,
            'success': success,
            'error': error,
            'timestamp': firestore.SERVER_TIMESTAMP
        })
    except Exception as e:
        print(f"Error logging usage: {str(e)}")

@functions_framework.http
def get_chat_history(request):
    """Retrieve user's chat history"""

    # Enable CORS
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    headers = {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json'
    }

    # Verify authentication
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return (jsonify({"error": "Unauthorized"}), 401, headers)

    user_id = request.args.get('userId')
    if not user_id:
        return (jsonify({"error": "Missing userId"}), 400, headers)

    try:
        # Get last 10 conversations
        conversations = db.collection('users').document(user_id) \
            .collection('conversations') \
            .order_by('timestamp', direction=firestore.Query.DESCENDING) \
            .limit(10) \
            .stream()

        result = []
        for conv in conversations:
            conv_data = conv.to_dict()
            conv_data['id'] = conv.id
            result.append(conv_data)

        return (jsonify({"conversations": result}), 200, headers)

    except Exception as e:
        return (jsonify({"error": f"Error: {str(e)}"}), 500, headers)
