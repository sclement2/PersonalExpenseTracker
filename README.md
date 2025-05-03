# 📊 Personal Expense Tracker

A lightweight, console-based expense tracking tool written in Python. It allows users to record expenses, view them, set a monthly budget, and compare their total spending to the budget.

---

## 🚀 Features

- Add, view, and save expenses (with description, amount, and category).
- Set a personal budget.
- Compare current expenses against the budget.
- Simple text-based UI interface.
- Data saved as a CSV file in `data/expenses.csv`.

---

## 📦 Installation

### Using the `.whl` file (provided in dist folder)

Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install the app using pip:

```bash
pip install dist/expense_tracker-0.1.0-py3-none-any.whl
```

Once installed, launch the app from the command line:

```bash
tracker-console
```

You’ll be presented with a simple menu:

```bash
1. Add Expense
2. View Expenses
3. Track Budget
4. Save Expenses
5. Save Expenses and Exit
```

Follow the prompts to interact with the tracker.

## 🗂️ File Locations

- Data is saved to `data/expenses.csv` relative to your working directory.
- If the file or directory does not exist, it will be created automatically on save.

## 🧪 Running Tests (Optional, for Developers)

- If you clone or develop the project and want to run tests (not needed for running the app), you can do so using the built-in `unittest` framework.
- Ensure you have the `tests` directory with test files.

    ```bash
    python -m unittest discover -s tests
    ```

- This will run all tests in the `tests` directory.

## 📎 Requirements

- Python 3.10+
- No external dependencies (standard library only)

## 🔒 License

MIT License
