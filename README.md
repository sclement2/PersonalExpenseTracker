# 📊 Personal Expense Tracker

A lightweight, console-based expense tracking tool written in Python. It allows users to record expenses, view them, set a monthly budget, and compare their total spending to the budget.

---

## 🚀 Features

- Add, view, and save expenses (with description, amount, category, and date).
  - Validation for amount, date, category. description, and budget input for adding expenses and displaying expenses.
  - Each expense is represented as a dictionary with keys: date, category, amount, and description.
- Set a personal budget.
- Compare current expenses against a user's monthly budget.
  - Display warning if expenses exceed the budget.
  - Display remaining budget.
- Simple text-based UI interface.
- Data saved as a CSV file in `data/expenses.csv`.
- Data loaded from CSV file on startup (if it exists) so users can view past expenses and add new ones.

---

## 📦 Installation

Cloning the repository is not necessary if you only want to use the app. You can use the provided `.whl` file in the `dist` folder of the Github repository: <https://github.com/sclement2/PersonalExpenseTracker>.

### Installation using the `.whl` file (provided in dist folder in the github repository)

- Download the wheel file from the `dist` folder of the repository. See the links below in the File Locations section for the repository and wheel file URLs.

- Create and activate a virtual environment (optional but recommended):

```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
```

- Install the app using pip:

```bash
  pip install expense_tracker-0.1.0-py3-none-any.whl
```

- Once installed, launch the app from the command line:

```bash
  tracker-console
```

- You’ll be presented with a simple menu:

```bash
  1. Add Expense
  2. View Expenses
  3. Track Budget
  4. Save Expenses
  5. Save Expenses and Exit
```

- Follow the prompts to interact with the tracker.

---

## 📜 Usage

- Program functionality is divided into modules:
  - `expense_tracker.py`: Main program logic.
  - `console_app.py`: User's console interface.
- Both the `expense_tracker.py` and `console_app.py` files are highly documented with comments.
- The app is designed to be user-friendly and provides clear prompts for user input.
- To use the app, run the command `tracker-console` in your terminal.
- If you have downloaded the repository, you can run the app from the `tracker` directory using:

```bash
  python -m tracker.console_app
```

---

## 🗂️ File Locations

- Program functionality is divided into modules:
  - `expense_tracker.py`: Main program logic.
  - `console_app.py`: User's console interface.
  - Files are located in the `tracker` directory of the repository.
- Complete project is located in a Github repository.
  - <https://github.com/sclement2/PersonalExpenseTracker>
- Wheel file is located in the `dist` folder of the repository.
  - <https://github.com/sclement2/PersonalExpenseTracker/blob/main/dist/expense_tracker-0.1.0-py3-none-any.whl>
- Markdown versions of the python files are located in the `tests/documentation` folder of the repository.
- Data is saved to `data/expenses.csv` relative to your working directory (tracker)
- If the file or directory does not exist, it will be created automatically on save.

---

## 🧪 Testing

- If only want to use the app, you do not need to run tests.
- If you want to run tests, you can do so using the built-in `unittest` framework.
- To run tests you will need to clone the repository and then run tests using:

```bash

  python -m unittest discover -s tests
```

- This will run all tests in the `tests` directory.

## 📎 Requirements

- Python 3.10+
- No external dependencies (standard library only)

## 🔒 License

MIT License
