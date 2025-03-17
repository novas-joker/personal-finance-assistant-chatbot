from flask import Flask, render_template, request, jsonify
from datetime import datetime
from finance_helper import FinanceHelper  # Import the FinanceHelper class

app = Flask(__name__)
finance_helper = FinanceHelper()  # Create an instance of FinanceHelper

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '').lower()  # Convert to lowercase for easier matching
    
    if "budgeting apps" in user_message or "recommend" in user_message:
        response = finance_helper.get_budgeting_app_recommendation()
    elif "create budget" in user_message:
        # Extract income from the message (this is a simple example, you may want to improve this)
        income = user_message.split('$')[-1].strip()  # Get the income value after '$'
        response = finance_helper.create_basic_budget_plan(income)
    else:
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