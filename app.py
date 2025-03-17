from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-pro')

# Initialize chat
chat = model.start_chat(history=[])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def process_chat():
    try:
        user_message = request.json.get('message', '')
        
        # Get response from Gemini
        response = chat.send_message(user_message)
        
        # Prepare the response
        chat_response = {
            'message': response.text,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return jsonify(chat_response)
    
    except Exception as e:
        return jsonify({
            'message': f"I apologize, but I encountered an error: {str(e)}",
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }), 500

@app.route('/_vercel_health_check', methods=['GET'])
def health_check():
    return 'ok'

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Vercel, 
    # Vercel will serve the app through WSGI
    app.run(host='0.0.0.0', debug=True) 