def budget_tracker():
    income = int(input("Enter income: ").strip("$"))

    categories = []  
    amounts = []  
    total_expenses = 0

    while True:
        expense_type = input("Enter expense and type or done: ").strip().lower()
        if expense_type == "done":
            break

        price = int(input("Enter price of expense: ").strip("$"))
        
        categories.append(expense_type)  
        amounts.append(price)  
        total_expenses += price  

    total_savings = income - total_expenses

    print("\nSummary of expenses:")
    print(f"Total income: {income}$")
    print(f"Total expenses: {total_expenses}$")
    print(f"Total savings: {total_savings}$\n")

    print("Analysis:\nExpenses and price:")
    for i in range(len(categories)):
        print(f"- {categories[i].capitalize()}: {amounts[i]}$")

budget_tracker()
