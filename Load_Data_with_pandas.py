import pandas as pd


def init_data_to_budget(data_type, data_list, budget):
    if data_type == 'inc':
        for i in range(len(data_list['Incomes:'])):
            if data_list['Amount:'][i] == data_list['Amount:'][i]:
                budget.set_inc([data_list['Incomes:'][i], data_list['Amount:'][i]])
    else:
        for i in range(len(data_list['Expenses:'])):
            if data_list['Amount:.1'][i] == data_list['Amount:.1'][i]:
                budget.set_exp([data_list['Expenses:'][i], data_list['Amount:.1'][i]])


def read_data(file_name, budget_month_list, month_list):
    file_name = file_name + ".xlsx"
    try:
        i = 0
        for month in month_list:
            data = pd.read_excel(file_name, sheet_name=month, skipfooter=2)
            inc_data = pd.DataFrame(data, columns={'Incomes:', 'Amount:'})
            exp_data = pd.DataFrame(data, columns={'Expenses:', 'Amount:.1'})
            init_data_to_budget('inc', inc_data, budget_month_list[i])
            init_data_to_budget('exp', exp_data, budget_month_list[i])
            i += 1
        return True

    except FileNotFoundError:
        print(f'This file is not exist!\n')
        return False
