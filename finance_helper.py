class FinanceHelper:
    def __init__(self):
        self.budgeting_apps = {
            'Mint': {
                'description': 'Popular free budgeting app that connects to your bank accounts and automatically categorizes transactions',
                'features': ['Automatic transaction categorization', 'Bill tracking', 'Credit score monitoring', 'Investment tracking'],
                'url': 'https://mint.intuit.com/'
            },
            'Personal Capital': {
                'description': 'Free financial management tool focusing on investment tracking and retirement planning',
                'features': ['Investment analysis', 'Retirement planning', 'Net worth tracking', 'Cash flow monitoring'],
                'url': 'https://www.personalcapital.com/'
            },
            'YNAB': {
                'description': 'Zero-based budgeting app that helps you give every dollar a job',
                'features': ['Detailed budget planning', 'Goal tracking', 'Debt payoff planning', 'Real-time updates'],
                'url': 'https://www.ynab.com/'
            }
        }
        
        self.budget_categories = [
            'Housing', 'Transportation', 'Food', 'Utilities', 
            'Insurance', 'Healthcare', 'Savings', 'Debt Payments',
            'Entertainment', 'Personal Care', 'Education'
        ]

    def get_budgeting_app_recommendation(self, user_needs=None):
        if not user_needs:
            return {
                'message': 'Here are some popular free budgeting apps you can try:',
                'apps': self.budgeting_apps
            }
        # We'll add personalized recommendations based on user needs later

    def create_basic_budget_plan(self, monthly_income):
        try:
            income = float(monthly_income)
            budget_plan = {
                'Housing': income * 0.30,  # 30% for housing
                'Transportation': income * 0.15,  # 15% for transportation
                'Food': income * 0.15,  # 15% for food
                'Utilities': income * 0.10,  # 10% for utilities
                'Savings': income * 0.10,  # 10% for savings
                'Entertainment': income * 0.05,  # 5% for entertainment
                'Insurance': income * 0.05,  # 5% for insurance
                'Healthcare': income * 0.05,  # 5% for healthcare
                'Miscellaneous': income * 0.05  # 5% for miscellaneous
            }
            return {
                'message': 'Here\'s a suggested monthly budget based on your income:',
                'budget': budget_plan,
                'tips': [
                    'Try to keep housing costs under 30% of your income',
                    'Aim to save at least 10% of your income',
                    'Track your spending for a month to refine these categories',
                    'Consider using one of the recommended budgeting apps for better tracking'
                ]
            }
        except ValueError:
            return {
                'error': 'Please provide a valid monthly income amount'
            }

    def get_budgeting_tips(self):
        return {
            'general_tips': [
                'Track all your expenses for at least a month',
                'Use the 50/30/20 rule: 50% needs, 30% wants, 20% savings',
                'Set up automatic savings transfers',
                'Create an emergency fund with 3-6 months of expenses',
                'Review and adjust your budget monthly'
            ],
            'recommended_tools': list(self.budgeting_apps.keys()),
            'categories': self.budget_categories
        } 