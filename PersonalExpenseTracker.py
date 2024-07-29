import csv

# Specify the location of your CSV file containing expenses.
src = "C:\\Users\\HP\\Desktop\\New folder\\Expenses.csv"  # Replace single \ with \\


def addExpense(exp):
    """
    Adds a new expense to the CSV file.

    Args:
        exp (str): A string containing the expense details separated by commas.
    """
    with open(src, "a") as file1:
        writer = csv.writer(file1)
        writer.writerow(exp.split(","))


def viewExpense():
    """
    Prints all expenses from the CSV file.
    """
    with open(src, "r") as file1:
        reader = csv.reader(file1)
        for row in reader:
            print(row)


def viewExpenseByCategory(cat):
    """
    Prints expenses filtered by a specific category.

    Args:
        cat (str): The category to filter expenses by.
    """
    with open(src, "r") as file1:
        x = 0
        flag = False
        value = ""
        reader_obj = csv.reader(file1)
        for row in reader_obj:
            try:
                if row[3].strip().lower() == cat:
                    flag = True
                    value = ",".join(row)
                    print(value)
            except IndexError:
                print(f"Not enough columns in row number {x}")
            x = x + 1

        if not flag:
            print("Category not found")


def searchExpense(exp):
    """
    Searches for an expense by name and prints the matching record.

    Args:
        exp (str): The name of the expense to search for.
    """
    with open(src, "r") as file1:
        value = ""
        flag = False
        reader_obj = csv.reader(file1)
        for row in reader_obj:
            try:
                if row[1].strip().lower() == exp:
                    flag = True
                    value = ",".join(row)
                    print(value)
            except IndexError:
                print("Not enough columns in the original file found")
        if not flag:
            print(f'No expense called "{exp}" found')


operation = input(
    "Select the operation you want to perform: \n 1) Add Expense (add) \n 2) View Expense (view) \n 3) Search Expense (search) \n 4) Generate Report (Report) \n \n"
)
if operation == "1":
    exp = input("Enter your expenses:")
    addExpense(exp)

elif operation == "2":
    option = input(
        "Select your desired view: \n 1)View all Expenses \n 2)View by category "
    )
    if option == "1":
        viewExpense()
    elif option == "2":
        categoryOption = input("Enter your Category")
        categoryOption = categoryOption.lower()
        viewExpenseByCategory(categoryOption)

elif operation == "3":
    option = input("Enter the name of expense you want to search")
    option = option.lower()
    searchExpense(option)
