from employee import *


class Engineer(Employee):

    def do_work(self):
        """ This method requires re-implementation """
        paid_salary = self.company.do_tasks(self)
        self.put_money_into_my_wallet(paid_salary)
