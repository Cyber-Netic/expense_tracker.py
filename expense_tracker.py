import sqlite3
from tabulate import tabulate

# Initialize Database
def init_db():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Add an expense
def add_expense(description, amount, category, date):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (description, amount, category, date) VALUES (?, ?, ?, ?)", 
                   (description, amount, category, date))
    conn.commit()
    conn.close()
    print("✅ Expense added successfully!")

# View all expenses
def view_expenses():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    conn.close()

    if expenses:
        print(tabulate(expenses, headers=["ID", "Description", "Amount", "Category", "Date"], tablefmt="grid"))
    else:
        print("❌ No expenses found!")

# Update an expense
def update_expense(expense_id, description, amount, category, date):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE expenses SET description=?, amount=?, category=?, date=? WHERE id=?", 
                   (description, amount, category, date, expense_id))
    conn.commit()
    conn.close()
    print("✏️ Expense updated successfully!")

# Delete an expense
def delete_expense(expense_id):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
    conn.commit()
    conn.close()
    print("🗑️ Expense deleted successfully!")

# Main function
def main():
    init_db()
    while True:
        print("\n💰 Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            desc = input("Enter description: ")
            amt = float(input("Enter amount: "))
            cat = input("Enter category (e.g., Food, Travel, Rent): ")
            date = input("Enter date (YYYY-MM-DD): ")
            add_expense(desc, amt, cat, date)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_expenses()
            exp_id = int(input("Enter Expense ID to update: "))
            desc = input("Enter new description: ")
            amt = float(input("Enter new amount: "))
            cat = input("Enter new category: ")
            date = input("Enter new date (YYYY-MM-DD): ")
            update_expense(exp_id, desc, amt, cat, date)
        elif choice == "4":
            view_expenses()
            exp_id = int(input("Enter Expense ID to delete: "))
            delete_expense(exp_id)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
