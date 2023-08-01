from datetime import date
from package_progs.application.salary import calculate_salary as c_s
from package_progs.application.db.people import get_employees as g_e


class AccountingDepartment:
    def __init__(self, name_company):
        self.name_company = name_company
        print(f'Текущая дата: {date.today()}')

    def calculate_salary(self):
        print('Start execute of calculate_salary function by class methods')

    def get_employees(self):
        print('Start execute of get_employees function by class methods')


def main():
    name_company = 'XYZ'
    accounting_department = AccountingDepartment(name_company)
    print(f'Наименование компании: {accounting_department.name_company}')
    accounting_department.calculate_salary()
    accounting_department.get_employees()
    c_s()
    g_e()


if __name__ == '__main__':
    main()
