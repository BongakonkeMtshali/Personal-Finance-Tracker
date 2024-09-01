import json
import matplotlib.pyplot as plt

# Global Variables
categories = {}
income = 0.0
expenses = 0.0
savings = 0.0

# Functions

def print_welcome_message():
    """Prints a welcome message and instructions for the user."""
    print("Welcome to the Personal Finance Tracker!")
    print("You can add income, record expenses, and view your savings.")
    print("Select an option from the menu below to get started.")

def safe_float_input(prompt):
    """Safely takes a float input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def safe_input(prompt, choices):
    """Safely takes an input from the user with specified choices."""
    while True:
        choice = input(prompt).strip()
        if choice in choices:
            return choice
        else:
            print(f"Invalid choice. Please choose from {choices}.")

def input_transaction():
    """Prompts the user to input a transaction's details."""
    description = input("Enter the description of the transaction: ")
    amount = safe_float_input("Enter the amount: ")
    category = input("Enter the category: ")
    return description, amount, category

def add_income(amount):
    """Adds an income amount to the total."""
    global income
    income += amount
    print(f"Income added: ${amount:.2f}")

def add_expense(amount, category):
    """Adds an expense amount to the total and updates the category."""
    global expenses
    global categories
    expenses += amount
    if category in categories:
        categories[category] += amount
    else:
        categories[category] = amount
    print(f"Expense added: ${amount:.2f} under category {category}")

def update_savings():
    """Updates the savings based on income and expenses."""
    global savings
    savings = income - expenses

def display_report():
    """Displays a financial report including income, expenses, and savings."""
    print("\n--- Financial Report ---")
    print(f"Total Income: ${income:.2f}")
    print(f"Total Expenses: ${expenses:.2f}")
    print(f"Total Savings: ${savings:.2f}")
    print("\nExpenses by Category:")
    for category, amount in categories.items():
        print(f"{category}: ${amount:.2f}")

def plot_financial_data():
    """Plots a pie chart of expenses by category."""
    if categories:
        labels = list(categories.keys())
        sizes = list(categories.values())
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.title('Expense Distribution by Category')
        plt.show()
    else:
        print("No expense data available to plot.")

def save_data():
    """Saves transaction data to a JSON file."""
    with open('finance_data.json', 'w') as file:
        data = {
            'income': income,
            'expenses': expenses,
            'savings': savings,
            'categories': categories
        }
        json.dump(data, file)

def load_data():
    """Loads transaction data from a JSON file."""
    global income, expenses, savings, categories
    try:
        with open('finance_data.json', 'r') as file:
            data = json.load(file)
            income = data['income']
            expenses = data['expenses']
            savings = data['savings']
            categories = data['categories']
    except FileNotFoundError:
        pass

def main_menu():
    """Displays the main menu and processes user choices."""
    while True:
        print("\n--- Main Menu ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Report")
        print("4. Plot Expense Data")
        print("5. Exit")
        
        choice = safe_input("Choose an option: ", ['1', '2', '3', '4', '5'])
        
        if choice == '1':
            amount = safe_float_input("Enter income amount: ")
            add_income(amount)
            update_savings()
        elif choice == '2':
            description, amount, category = input_transaction()
            add_expense(amount, category)
            update_savings()
        elif choice == '3':
            display_report()
        elif choice == '4':
            plot_financial_data()
        elif choice == '5':
            print("Thank you for using the Personal Finance Tracker!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    print_welcome_message()
    load_data()
    main_menu()
    save_data()
