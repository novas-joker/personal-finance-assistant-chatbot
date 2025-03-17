from flask import Flask, render_template, request, jsonify, session
import google.generativeai as genai
from datetime import datetime
import os
from dotenv import load_dotenv
import traceback

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Required for session management

# Configure Gemini API
try:
    genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    print(f"Error configuring Gemini API: {str(e)}")

def get_chat_session():
    """Get or create a chat session for the current user"""
    if 'chat' not in session:
        try:
            session['chat'] = model.start_chat(history=[])
        except Exception as e:
            print(f"Error creating chat session: {str(e)}")
            return None
    return session['chat']

@app.route('/')
def home():
    # Clear existing chat session when loading home page
    session.pop('chat', None)
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def process_chat():
    try:
        user_message = request.json.get('message', '')
        if not user_message.strip():
            return jsonify({
                'message': 'Please enter a message.',
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })

        # Get chat session
        chat = get_chat_session()
        if not chat:
            raise Exception("Failed to initialize chat session")

        # Get response from Gemini
        response = chat.send_message(user_message)
        
        if not response or not response.text:
            raise Exception("No response received from AI")

        # Prepare the response
        chat_response = {
            'message': response.text,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return jsonify(chat_response)
    
    except Exception as e:
        error_details = traceback.format_exc()
        print(f"Error in chat processing: {error_details}")
        
        return jsonify({
            'message': f"I apologize, but I encountered an error. Please try again or refresh the page if the issue persists.",
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }), 500

@app.route('/_vercel_health_check', methods=['GET'])
def health_check():
    return 'ok'

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Vercel, 
    # Vercel will serve the app through WSGI
    app.run(host='0.0.0.0', debug=True) 