from src.oop.engineer import Engineer
from src.oop.manager import Manager


class Company:
    """ Represents a company """
    ENGINEER_PAYMENT = 10
    MANAGER_PAYMENT = 12

    def __init__(self, name, address=None):
        self.name = name
        self.address = address
        self.employees = list()
        self.__money = 1000

    def add_employee(self, employee):
        # make sure employee is an instance of Engineer or Manager
        # make sure he is not employed already
        if employee not in self.employees:
            if isinstance(employee, Engineer) or isinstance(employee, Manager):
                self.employees.append(employee)
            else:
                raise TypeError("Unknown employee")
        else:
            raise Exception("Already employed employee!")
        return employee

    def dismiss_employee(self, employee):
        """
        Dismisses an employee. Employee must be a company member.
        Company should notify employee that he/she was dismissed
        """
        if employee in self.employees:
            employee.notify_dismissed()
            self.employees.remove(employee)
        else:
            raise RuntimeError("Employee doesn't work in this company!")

    def do_tasks(self, employee):
        """
        Engineer should call this method when he is working.
        Company should withdraw 10 money from a personal account and returns
        them to engineer. That will be a payment
        :rtype: int
        """
        # make sure engineer is employed to this company
        # check employee is Engineer
        if isinstance(employee, Engineer):
            if employee in self.employees:
                self.__money -= self.ENGINEER_PAYMENT
                return self.ENGINEER_PAYMENT
            else:
                raise RuntimeError("Employee doesn't work in this company!")
        else:
            raise RuntimeError("Employee isn't an Engineer!")

    def write_reports(self, employee):
        """
        Manager should call this method when he is working.
        Company should withdraw 12 money from a personal account and return
        them to manager. That will be a payment
        :rtype: int
        """
        # make sure manager is employed to this company
        # check employee is Manager
        if isinstance(employee, Manager):
            if employee in self.employees:
                self.__money -= self.MANAGER_PAYMENT
                return self.MANAGER_PAYMENT
            else:
                raise RuntimeError("Manager doesn't work in this company!")
        else:
            raise RuntimeError("Manager isn't an Engineer!")

    def make_a_party(self):
        """ Party time! All employees get 5 money """
        # make sure a company is not a bankrupt before and after the party
        # call employee.bonus_to_salary()
        if not self.is_bankrupt:
            for empl in self.employees:
                empl.bonus_to_salary(self)
        else:
            raise RuntimeError("Sorry, company is bankrupt!")

    def withdraw_money(self, amount):
        self.__money -= amount

    def show_money(self):
        """ Displays amount of money that company has """
        print(f"Company {self.name} budget: {self.__money}")
        return self.__money

    def go_bankrupt(self):
        """
        Declare bankruptcy. Company money are drop to 0.
        All employees become unemployed.
        """
        for element in self.employees:
            self.dismiss_employee(element)
        self.__money = 0
        print(f"Company '{self.name}' is bankrupt!")

    @property
    def is_bankrupt(self):
        """ returns True or False """
        return self.__money <= 0

    def __repr__(self):
        return 'Company (%s)' % self.name