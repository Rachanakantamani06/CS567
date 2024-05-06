import unittest
from personalfinance import *

class TestPersonalFinanceTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = PersonalFinanceTracker()

    def test_add_income(self):
        self.tracker.add_income("Salary", 3000)
        self.assertIn({"source": "Salary", "amount": 3000}, self.tracker.incomes)

    def test_add_expense(self):
        self.tracker.add_expense("Groceries", 200)
        self.assertIn({"category": "Groceries", "amount": 200}, self.tracker.expenses)

    def test_set_budget(self):
        self.tracker.set_budget("Entertainment", 150)
        self.assertEqual(self.tracker.budgets["Entertainment"], 150)

    def test_add_financial_goal(self):
        self.tracker.add_financial_goal("Vacation", 2000)
        self.assertIn({"goal": "Vacation", "amount": 2000}, self.tracker.financial_goals)

    def test_remove_income(self):
        self.tracker.add_income("Bonus", 500)
        self.tracker.remove_income("Bonus")
        self.assertNotIn({"source": "Bonus", "amount": 500}, self.tracker.incomes)

    def test_remove_expense(self):
        self.tracker.add_expense("Utilities", 100)
        self.tracker.remove_expense("Utilities")
        self.assertNotIn({"category": "Utilities", "amount": 100}, self.tracker.expenses)

    def test_update_income(self):
        self.tracker.add_income("Dividends", 0)
        self.tracker.update_income("Dividends", 200)
        self.assertIn({"source": "Dividends", "amount": 200}, self.tracker.incomes)

    def test_update_expense(self):
        self.tracker.add_expense("Travel", 300)
        self.tracker.update_expense("Travel", 350)
        self.assertIn({"category": "Travel", "amount": 350}, self.tracker.expenses)

    def test_get_total_income(self):
        self.tracker.add_income("Salary", 3000)
        self.tracker.add_income("Bonus", 500)
        self.assertEqual(self.tracker.get_total_income(), 3500)

    def test_get_total_expense(self):
        self.tracker.add_expense("Groceries", 150)
        self.tracker.add_expense("Rent", 800)
        self.assertEqual(self.tracker.get_total_expense(), 950)

    def test_get_balance(self):
        self.tracker.add_income("Salary", 3000)
        self.tracker.add_expense("Rent", 800)
        self.assertEqual(self.tracker.get_balance(), 2200)

    def test_check_budgets(self):
        self.tracker.set_budget("Groceries", 200)
        self.tracker.add_expense("Groceries", 150)
        self.tracker.check_budgets()
        remaining = self.tracker.budgets["Groceries"] - 150
        self.assertEqual(remaining, 50)

    def test_add_savings_goal(self):
        self.tracker.add_savings_goal("New Car", 10000)
        self.assertIn({"goal": "New Car", "target_amount": 10000, "current_amount": 0}, self.tracker.financial_goals)

    def test_update_savings_goal(self):
        self.tracker.add_savings_goal("New Car", 10000)
        self.tracker.update_savings_goal("New Car", 1500)
        goal = next((g for g in self.tracker.financial_goals if g["goal"] == "New Car"), None)
        self.assertEqual(goal["current_amount"], 1500)

    def test_remove_savings_goal(self):
        self.tracker.add_savings_goal("New Car", 10000)
        self.tracker.remove_savings_goal("New Car")
        self.assertNotIn("New Car", [goal["goal"] for goal in self.tracker.financial_goals])

if __name__ == '__main__':
    unittest.main()
