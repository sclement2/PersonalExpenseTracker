import unittest
from tracker import expense_tracker
from datetime import datetime
import io
import sys


class TestExpenseTracker(unittest.TestCase):
    def setUp(self):
        # Clear the expenses list before each test
        expense_tracker.expenses.clear()
        expense_tracker.budget = 0

    def test_add_expense_valid(self):
        expense_tracker.add_expense(100, "Food", "Lunch", "2023-10-01")
        self.assertEqual(len(expense_tracker.expenses), 1)
        self.assertEqual(expense_tracker.expenses[0]["amount"], 100)
        self.assertEqual(expense_tracker.expenses[0]["category"], "Food")
        self.assertEqual(expense_tracker.expenses[0]["description"], "Lunch")
        self.assertEqual(expense_tracker.expenses[0]["date"], "2023-10-01")

    def test_add_expense_invalid_amount(self):
        with self.assertRaises(ValueError):
            expense_tracker.add_expense(-10, "Food", "Lunch")

    def test_add_expense_without_date(self):
        expense_tracker.add_expense(50, "Transport", "Bus fare")
        self.assertEqual(len(expense_tracker.expenses), 1)
        self.assertEqual(expense_tracker.expenses[0]["amount"], 50)
        self.assertEqual(expense_tracker.expenses[0]["category"], "Transport")
        self.assertEqual(expense_tracker.expenses[0]["description"], "Bus fare")
        self.assertEqual(
            expense_tracker.expenses[0]["date"],
            datetime.now().strftime("%Y-%m-%d"),
        )

    def test_validate_expense_data(self):
        valid = expense_tracker.validate_expense_data(
            10, "Groceries", "Milk and bread", "2024-04-01"
        )
        self.assertTrue(valid)

    def test_validate_invalid_date(self):
        with self.assertRaises(ValueError):
            expense_tracker.validate_expense_data(10, "Food", "Test", "04-01-2024")

    def test_view_expenses(self):
        expense_tracker.add_expense(200, "Entertainment", "Movie", "2023-10-02")

        # Capture print output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        expense_tracker.view_expenses()

        sys.stdout = sys.__stdout__  # Reset redirect.
        output = captured_output.getvalue()

        # Check if the output contains the added expense
        self.assertIn(
            "200.00 in Entertainment on 2023-10-02 with description 'Movie'", output
        )

    def test_set_budget_valid(self):
        expense_tracker.set_budget(500)
        self.assertEqual(expense_tracker.budget, 500)

    def test_set_budget_invalid(self):
        with self.assertRaises(ValueError):
            expense_tracker.set_budget("-100")

    def test_compare_budget_valid(self):
        expense_tracker.set_budget("100")
        expense_tracker.add_expense(50, "Food", "Lunch")

        # Capture print output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        expense_tracker.compare_budget()

        sys.stdout = sys.__stdout__  # Reset redirect.
        output = captured_output.getvalue()

        self.assertIn("Expenses are within the budget.", output)

    def test_compare_budget_exceed(self):
        expense_tracker.set_budget("100")
        expense_tracker.add_expense(150, "Food", "Lunch")

        # Capture print output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        expense_tracker.compare_budget()

        sys.stdout = sys.__stdout__  # Reset redirect.
        output = captured_output.getvalue()

        self.assertIn("Expenses exceeded the budget by: 50.00", output)

    def test_get_expenses_for_month(self):
        date_str = datetime.now().strftime("%Y-%m-%d")
        expense_tracker.add_expense(100, "Utilities", "Electricity", date_str)
        expense_tracker.add_expense(100, "Utilities", "Electricity", "2023-10-01")
        total = expense_tracker.get_current_month_expenses()
        self.assertEqual(total, 100)

    def test_save_and_load_expenses(self):
        expense_tracker.add_expense(25, "Travel", "Taxi")
        expense_tracker.save_expenses_to_csv()
        expense_tracker.expenses.clear()
        self.assertEqual(len(expense_tracker.expenses), 0)
        expense_tracker.load_expenses_from_csv()
        self.assertGreater(len(expense_tracker.expenses), 0)


if __name__ == "__main__":
    unittest.main()
