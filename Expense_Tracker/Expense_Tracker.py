import csv
from ctypes.wintypes import FILETIME
from datetime import datetime

File_name = "expense.csv"

def add_expense():
    date = datetime.now().strftime("%y-%m-%d")
    category = input("Enter expense catgory(food, transport, shopping, etc.):")
    amount = input("Enter the amount(₹):")

    with open(File_name, mode="a", newline="") as file:
        writer =csv.writer(file)
        writer.writerow([date, category, amount])
    print('Expense created successfully')    
add_expense()   



def show_expense():
    try:
        with open(File_name, mode='r') as file:
            reader =csv.reader(file)
            print('/n your expenses:')
            for row in reader:
                print(f"{row[0]}|{row[1]}|{row[2]}")
    except FileNotFoundError:
        print("No Expense recorded yet")
show_expense()

def category_summary():
    category_totals = {}
    try:
        with open(File_name, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                category = row[1]
                try:
                   amount = float(row[2].replace(",", "").strip()) 
                except ValueError:
                   print(f" Skipping invalid entry: {row[2]}")
                continue
                category_totals[category] = category_totals.get(category, 0) + amount

        print("\n Expense Summary by Category:")
        for category, total in category_totals.items():
            print(f" {category}: ₹{total}")

    except FileNotFoundError:
        print(" No expenses recorded yet!")

def new_func(row):
    amount = float(row[2])
    return amount
category_summary()




while True:
    print("\n Expense Tracker Menu:")
    print("1 Add Expense")
    print("2 Show All Expenses")
    print("3 Show Expense Summary by Category")
    print("4 Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        show_expense()

    elif choice == "3":
        category_summary()

    elif choice == "4":
        print("Exiting Expense Tracker. Have a great day!")
        break

    else:
        print(" Invalid choice! Please select a valid option.")

