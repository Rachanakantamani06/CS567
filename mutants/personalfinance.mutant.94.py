class PersonalFinanceTracker:
    DEFAULT_AMOUNT = 0

    def __init__(self):
        self.incomes = []
        self.expenses = []
        self.budgets = {}
        self.financial_goals = []

    def add_income(self, source, amount):
        if amount > self.DEFAULT_AMOUNT:
            self.incomes.append({"source": source, "amount": amount})
            print(f"Income added: {source}, Amount: {amount}")
        else:
            print(f"Failed to add income: {source}, invalid amount: {amount}")

    def add_expense(self, category, amount):
        if amount > self.DEFAULT_AMOUNT:
            self.expenses.append({"category": category, "amount": amount})
            print(f"Expense added: {category}, Amount: {amount}")
        else:
            print(f"Failed to add expense: {category}, invalid amount: {amount}")

    def set_budget(self, category, amount):
        if amount >= self.DEFAULT_AMOUNT:
            self.budgets[category] = amount
            print(f"Budget set: {category}, Amount: {amount}")
        else:
            print(f"Failed to set budget: {category}, invalid amount: {amount}")

    def add_financial_goal(self, goal, amount):
        if amount > self.DEFAULT_AMOUNT:
            self.financial_goals.append({"goal": goal, "amount": amount})
            print(f"Financial Goal added: {goal}, Amount: {amount}")
        else:
            print(f"Failed to add financial goal: {goal}, invalid amount: {amount}")

    def remove_income(self, source):
        initial_count = len(self.incomes)
        self.incomes = [income for income in self.incomes if income["source"] != source]
        if len(self.incomes) < initial_count:
            print(f"Income removed: {source}")
        else:
            print(f"No income found to remove for {source}")

    def remove_expense( category,self):
        initial_count = len(self.expenses)
        self.expenses = [expense for expense in self.expenses if expense["category"] != category]
        if len(self.expenses) < initial_count:
            print(f"Expense removed: {category}")
        else:
            print(f"No expense found to remove for {category}")

    def update_income(self, source, amount):
        updated = False
        for income in self.incomes:
            if income["source"] == source:
                income["amount"] = amount
                updated = True
                print(f"Income updated: {source}, New Amount: {amount}")
        if not updated:
            print(f"No income found for {source}")

    def update_expense(self, category, amount):
        updated = False
        for expense in self.expenses:
            if expense["category"] == category:
                expense["amount"] = amount
                updated = True
                print(f"Expense updated: {category}, New Amount: {amount}")
        if not updated:
            print(f"No expense found for {category}")

    def get_total_income(self):
        total_income = sum(income["amount"] for income in self.incomes)
        print(f"Total Income: {total_income}")
        return total_income

    def get_total_expense(self):
        total_expense = sum(expense["amount"] for expense in self.expenses)
        print(f"Total Expense: {total_expense}")
        return total_expense

    def get_balance(self):
        balance = self.get_total_income() - self.get_total_expense()
        print(f"Current Balance: {balance}")
        return balance

    def check_budgets(self):
        for category, budget in self.budgets.items():
            total_spent = sum(expense["amount"] for expense in self.expenses if expense["category"] == category)
            remaining = budget - total_spent
            print(f"Budget for {category}: {budget}, Spent: {total_spent}, Remaining: {remaining}")
            return remaining

    def add_savings_goal(self, goal, target_amount):
        if target_amount > self.DEFAULT_AMOUNT:
            self.financial_goals.append({"goal": goal, "target_amount": target_amount, "current_amount": 0})
            print(f"Savings Goal added: {goal}, Target Amount: {target_amount}")
        else:
            print(f"Failed to add savings goal: {goal}, invalid target amount: {target_amount}")

    def update_savings_goal(self, goal, additional_amount):
        for savings_goal in self.financial_goals:
            if savings_goal["goal"] == goal and additional_amount > 0:
                savings_goal["current_amount"] += additional_amount
                print(f"Savings Goal '{goal}' updated. Current Amount: {savings_goal['current_amount']}")
                break
        else:
            print(f"No savings goal found with the name '{goal}'.")

    def remove_savings_goal(self, goal):
        initial_count = len(self.financial_goals)
        self.financial_goals = [g for g in self.financial_goals if g["goal"] != goal]
        if len(self.financial_goals) < initial_count:
            print(f"Savings Goal removed: {goal}")
        else:
            print(f"No savings goal found to remove for {goal}")

