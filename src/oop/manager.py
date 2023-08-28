from src.oop.employee import *


class Manager(Employee):

    def do_work(self):
        paid_salary = self.company.write_reports(self)
        self.put_money_into_my_wallet(paid_salary)
