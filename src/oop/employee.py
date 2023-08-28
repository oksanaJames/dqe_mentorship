from src.oop.person import *


class Employee(Person):
    __metaclass__ = abc.ABCMeta

    def __init__(self, name, age, sex=None, address=None):
        super(Employee, self).__init__(name, age, sex, address)
        self.company = None
        self.__money = 0

    def join_company(self, company):
        # make sure that this person is not employed already
        if not self.is_employed:
            self.company = company
            self.company.add_employee(self)
        else:
            print(f"Employee '{self.name}' already hired!")

    def become_unemployed(self):
        """ Leave current company """
        self.company.dismiss_employee(self)
        self.company = None

    def notify_dismissed(self):
        """ Company should call this method when dismissing an employee """
        print(f"Employee '{self.name}' left company '{self.company.name}'!")

    def bonus_to_salary(self, company, reward=5):
        """
        Company should call this method on each employee when having a party
        """
        # make sure person is employed to same company
        # money + 5
        if self.company == company:
            self.__money += reward
            company.withdraw_money(reward)
        else:
            print("Employee doesn't work in this company!")

    @property
    def is_employed(self):
        """ returns True or False """
        return self.company is not None

    def put_money_into_my_wallet(self, amount):
        """ Adds the indicated amount of money to persons budget """
        # Engineer and Manager will have to use this method to store their
        # salary, because __money is a private attribute
        self.__money += amount

    def show_money(self):
        """ Shows how much money person has earned """
        if self.is_employed:
            print(f"{self.name} earned {self.__money}")
        return self.__money

    @abc.abstractmethod
    def do_work(self):
        """ This method requires re-implementation """
        raise NotImplemented('This method requires re-implementation')

    def __repr__(self):
        if self.is_employed:
            return '%s works at %s' % (self.name, self.company)
        return '%s, unemployed'