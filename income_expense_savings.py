"""
Write a program that takes user income and a series of expenses, then calculates:
- Total income
- Total expenses
- Total savings
- Breakdown of expenses by category

Input:
Enter income: 1000$
Enter expense and type or done: food
Enter price of expense: 200$
Enter expense and type or done: transport
Enter price of expense: 150$
Enter expense and type or done: done

Output:
Summary of expenses:
Total income: 1000$
Total expenses: 350$
Total savings: 650$

Analysis:
Expenses and price:
- Food: 200$
- Transport: 150$
"""

def budget_tracker():
    income = int(input("Enter income: ").strip("$"))

    categories = []  # List to store expense categories
    amounts = []  # List to store expense amounts
    total_expenses = 0

    while True:
        expense_type = input("Enter expense and type or done: ").strip().lower()
        if expense_type == "done":
            break

        price = int(input("Enter price of expense: ").strip("$"))
        
        categories.append(expense_type)  # Store category
        amounts.append(price)  # Store amount
        total_expenses += price  # Update total expenses

    total_savings = income - total_expenses

    print("\nSummary of expenses:")
    print(f"Total income: {income}$")
    print(f"Total expenses: {total_expenses}$")
    print(f"Total savings: {total_savings}$\n")

    print("Analysis:\nExpenses and price:")
    for i in range(len(categories)):
        print(f"- {categories[i].capitalize()}: {amounts[i]}$")

budget_tracker()
