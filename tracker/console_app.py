# tracker/console_app.py

from tracker.expense_tracker import (
    add_expense,
    view_expenses,
    set_budget,
    compare_budget,
    save_expenses_to_csv,
    load_expenses_from_csv,
)


def menu():
    while True:
        print("Welcome to the Personal Expense Tracker!")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Track Budget")
        print("4. Save Expenses")
        print("5. Save Expenses and Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            print(
                f"Adding expense: {amount} in {category} on {date} with description '{description}'"
            )
            try:
                add_expense(amount, category, description, date)
            except ValueError as e:
                print(f"Error adding expense: {e}")
                # print("Invalid entry. Please enter valid data.")
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            budget = input("Enter your budget: ")
            try:
                set_budget(budget)
                compare_budget()
            except ValueError as e:
                print(f"Error setting budget: {e}")
                # print("Invalid entry. Please enter valid data.")
        elif choice == "4":
            save_expenses_to_csv()
        elif choice == "5":
            save_expenses_to_csv()
            print("Exiting...")
            exit(0)
        else:
            print("Invalid choice. Please try again.")


def main():
    load_expenses_from_csv()
    menu()


if __name__ == "__main__":
    main()
