import xlsxwriter as xl


def details_to_file(budget, sheet):
    sheet.write('A1', 'Incomes:')
    sheet.write('B1', 'Amount:')
    sheet.write('D1', 'Expenses:')
    sheet.write('E1', 'Amount:')
    inc_row = write_inc_and_exp(1, 0, budget.get_inc(), sheet)
    exp_row = write_inc_and_exp(1, 3, budget.get_exp(), sheet)
    total_row = exp_row + 2 if exp_row > inc_row else inc_row + 2
    sheet.write(total_row, 0, f'Total Income: ')
    sheet.write(total_row, 1, float(budget.income_calc()))
    sheet.write(total_row, 3, f'Total Expense: ')
    sheet.write(total_row, 4, float(budget.expenses_calc()))

    sheet.write('G3', 'Monthly Balance: ')
    sheet.write('H3', float(budget.balance_calc()))


def write_inc_and_exp(row, col, items, sheet):
    for name, value in items:
        sheet.write(row, col, name)
        sheet.write(row, col + 1, float(value))
        row += 1

    return row


def create_new_user_file(file_name, month_list, budget_month_list):
    file_name = file_name + '.xlsx'
    wb = xl.Workbook(file_name)
    sheet_list = list()
    for month in month_list:
        sheet_list.append(wb.add_worksheet(month))
    print(f"\nHere are all the details copied to an Excel file named '{file_name}': \n")
    for i in range(len(sheet_list)):
        print(budget_month_list[i])
        details_to_file(budget_month_list[i], sheet_list[i])

    wb.close()
