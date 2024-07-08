import csv

src="C:\\Users\\HP\\Desktop\\New folder\\Expenses.csv" #place the location of your file here. Make sure to replace single \ with \\

def addExpense(exp):
    with open(src, 'a') as file1:
        writer=csv.writer(file1)  
        writer.writerow(exp.split(","))

def viewExpense():
    with open(src, 'r') as file1:
        reader = csv.reader(file1)
        for row in reader:
            print(row)

def viewExpenseByCategory(cat):
    with open(src, 'r') as file1:
        x=0
        flag=False
        value=""
        reader_obj=csv.reader(file1)
        for row  in reader_obj:
            try:
                if row[3].strip().lower()==cat:
                    flag=True
                    value = ",".join(row)
                    print(value)
            except IndexError:  #Indexerror exception is thrown if the number of columns in the source file is less than 4
                print(f"Not enough columns in row number {x}")
            x=x+1
        
        if (flag==False):
            print("Category not found")


def searchExpense(exp):
    with open(src, 'r') as file1:
        value=""
        flag=False
        reader_obj=csv.reader(file1)
        for row in reader_obj:
            try:
                if row[1].strip().lower()==exp:
                    flag-=True
                    value=",".join(row)
                    print(value)
            except IndexError:
                print("Not enough columns in the original file found")        
        if flag==False:
            print(f"No expense called \"{exp}\" found")
    

operation=input("Select the operation you want to perform: \n 1) Add Expense (add) \n 2) View Expense (view) \n 3) Search Expense (search) \n 4) Generate Report (Report) \n \n")
if(operation=="1"):
    exp=input("Enter your expenses:")
    addExpense(exp)

elif(operation=="2"):
    option= input("Select your desired view: \n 1)View all Expenses \n 2)View by category ")
    if(option=="1"):
        viewExpense()
    elif(option=="2"):
        categoryOption=input("Enter your Category")
        categoryOption=categoryOption.lower()
        viewExpenseByCategory(categoryOption)

elif(operation=="3"):
    option=input("Enter the name of expense you want to search")
    option=option.lower()
    searchExpense(option)




    




