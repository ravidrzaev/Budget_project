import re
import User_File
from Monthly_Budget import MonthBudget
from Load_Data import read_data

month_list = ['January', "February", 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
budget_month_list = []


def init_list_of_budget_months():
    for month in month_list:
        budget_month_list.append(MonthBudget(month))


def is_valid(choose):
    if choose.isdigit():
        choose = int(choose)
        if (choose >= 0) and (choose <= 12):
            return True
    return False


def delete_item(item_list, i, list_type):
    if len(item_list) < 1:
        print("No items to delete!")
        return
    for name, value in item_list:
        print(f"Name: {name}     Amount: {value}")
    item_to_delete = input("\nPlease enter the name of the item you want to delete: ")
    deleted = 0
    for item in item_list:
        if item_to_delete == item[0]:
            if list_type == 'inc':
                budget_month_list[i].delete_inc(item)
            elif list_type == 'exp':
                budget_month_list[i].delete_exp(item)
            print("\nThe item deleted successfully!")
            deleted = 1
    if not deleted:
        print("This name does not exist")


def do_action(act, i, file_name):
    if act == 0:
        User_File.create_new_user_file(file_name, month_list, budget_month_list)
        exit('Thank you and good bye!')
    elif act == 1:
        name = input("Income name: ")
        try:
            amount = float(input("income amount: "))
            budget_month_list[i].set_inc([name, amount])
        except ValueError:
            print("ERROR: wrong input!!")
            return True
    elif act == 2:
        name = input("Expense name: ")
        try:
            amount = float(input("Expense amount: "))
            budget_month_list[i].set_exp([name, amount])
        except ValueError:
            print("ERROR: wrong input!!")
            return True
    elif act == 3:
        print("\nall Incomes: ")
        incomes = budget_month_list[i].get_inc()
        delete_item(incomes, i, 'inc')
    elif act == 4:
        print("\nall Expenses: ")
        expenses = budget_month_list[i].get_exp()
        delete_item(expenses, i, 'exp')
    elif act == 5:
        budget_month_list[i].get_full_report()
    elif act == 6:  # return to the main menu
        return False
    else:
        print("There is not such option, please try again")
    return True


def select_new_or_existing_file():
    select = input(
        """- To new file - Please press 1 
- To update an existing file - Please press 2 \nPlease enter your choice: """)
    while select != '1' and select != '2':
        select = input("Error! There is not such option.\nPlease enter one of the options(1 / 2): ")
    return select


def print_month_list():
    print("MONTHS LIST:")
    for i in range(len(month_list)):
        print(f"{i + 1}. {month_list[i]}")


def monthly_edit_menu(month, file_name):
    stay_in_monthly_menu = True
    print(f"\nYou chose {month_list[month]} budget.")
    while stay_in_monthly_menu:
        try:
            act = int(input(
                f"""\nPlease enter one of the options:\n1. add income \n2. add expense \n3. Delete income
4. Delete expense \n5. print {month_list[month]} budget report\n6. Return to main menu\nYour choose: """))
            stay_in_monthly_menu = do_action(act, month, file_name)
        except ValueError:
            print("ERROR: wrong input!!")
    main_menu(file_name)


def main_menu(file_name):
    while True:
        print_month_list()
        month = input(f"Please enter the number of month you want to edit or 0 to save and exit: ")
        while not is_valid(month):
            month = input("ERROR: wrong input!! \nPlease enter the month number or 0 to save and exit: ")
        month = int(month) - 1
        if month == -1:
            do_action(0, month, file_name)  # save and exit
        else:
            monthly_edit_menu(month, file_name)


def valid_file_name(file_name):
    if len(file_name) < 1:
        return False
    x = re.search("[*?:<|>/\"]", file_name)
    if x or ('\\' in file_name):
        return False
    return True


def main():
    init_list_of_budget_months()
    print("Hello, \nWould you like to create a new budget file or update existing file?")
    file_name = ""
    while True:
        select = select_new_or_existing_file()
        if select == '1':
            file_name = input(
                "Please enter name for your budget file (this name will be the name of your budget file): ")
            while not valid_file_name(file_name):
                file_name = input("""The file name is not valid.
Please enter name for your budget file (without any of the following characters: [ * ? : < > | \ / ]: """)
            break
        elif select == '2':
            file_name = input("Please enter the file name you want to update (without the extension): ")
            if not read_data(file_name, budget_month_list, month_list):  # if the file is not exist
                continue
            else:
                break
    main_menu(file_name)


if __name__ == "__main__":
    main()
