from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    
    # Simple response for now - we'll enhance this later
    response = {
        'message': "I'm your personal finance assistant. I can help you with budgeting and financial advice.",
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    return jsonify(response)

# Vercel requires this
@app.route('/_vercel_health_check', methods=['GET'])
def health_check():
    return 'ok'

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Vercel, 
    # Vercel will serve the app through WSGI
    app.run(host='0.0.0.0', debug=True) 