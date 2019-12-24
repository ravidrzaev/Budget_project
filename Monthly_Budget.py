

class MonthBudget:

    def __init__(self, month):
        self.expenses = []
        self.incomes = []
        self.month = month

    def set_exp(self, exp):
        self.expenses.append(exp)

    def set_inc(self, inc):
        self.incomes.append(inc)

    def get_exp(self):
        return self.expenses

    def get_inc(self):
        return self.incomes

    def delete_inc(self, item):
        self.incomes.remove(item)

    def delete_exp(self, item):
        self.expenses.remove(item)

    def expenses_calc(self):
        total_exp = 0
        for exp in self.expenses:
            total_exp += float(exp[1])
        return float(total_exp)

    def income_calc(self):
        total_inc = 0
        for inc in self.incomes:
            total_inc += float(inc[1])
        return float(total_inc)

    def balance_calc(self):
        balance = self.income_calc() - self.expenses_calc()
        return float(balance)

    def get_full_report(self):
        index = 0
        print(f"""{self.month} Report:\nIncomes:\t\t\t\t\t\t\tExpenses:\n""")
        if len(self.incomes) < len(self.expenses):
            list_len = len(self.incomes)
            longest = 'expenses'
        else:
            list_len = len(self.expenses)
            longest = 'income'
        for i in range(list_len):
            print(
                f"""{i + 1}. {self.incomes[i][0]}: {self.incomes[i][1]}\t\t\t\t\t\t{i + 1}. {self.expenses[i][0]}: {self.expenses[i][1]}""")
            index = i + 1
        if longest == 'income':
            for index in range(index, len(self.incomes)):
                print(f"""{index + 1}. {self.incomes[index][0]}: {self.incomes[index][1]}""")
        else:
            for index in range(index, len(self.expenses)):
                print(f"""\t\t\t\t\t\t\t\t\t{index + 1}. {self.expenses[index][0]}: {self.expenses[index][1]}""")
        print(
            f"""\nTotal income: {self.income_calc()} \t\t\t\tTotal expenses: {self.expenses_calc()} \n\nMonthly balance:\t{self.balance_calc()}\n """)

    def __repr__(self):
        return f"""{self.month} report: \nTotal income:  {self.income_calc()} \t\t\tTotal expenses:  {self.expenses_calc()} \n\nMonthly balance:\t {self.balance_calc()}\n"""
