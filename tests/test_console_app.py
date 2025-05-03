import unittest
from unittest.mock import patch
import io
import sys
import tracker.console_app as console_app
import tracker.expense_tracker as expense_tracker


class TestConsoleApp(unittest.TestCase):
    def setUp(self):
        expense_tracker.expenses = []
        expense_tracker.budget = 0.0

    @patch("builtins.input", side_effect=["100"])
    def test_set_budget(self, mock_input):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        console_app.set_budget_flow()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn("Monthly budget set to: 100.00", output)

    @patch("builtins.input", side_effect=["2023-10-10", "25.5", "Food", "Lunch"])
    def test_add_expense_valid(self, mock_input):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        console_app.add_expense_flow()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn(
            "Added expense: 25.50 in Food on 2023-10-10 with description 'Lunch'",
            output,
        )

    @patch("builtins.input", side_effect=["abc", "-20", "100.50"])
    def test_get_valid_amount_with_invalid_then_valid_input(self, mock_input):
        # This test simulates entering "abc" (invalid), "-20" (negative), then "100.50" (valid)
        result = console_app.get_valid_amount()
        self.assertEqual(result, 100.50)


if __name__ == "__main__":
    unittest.main()
