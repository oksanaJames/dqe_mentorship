from company import *


def check_yourself():
    """ Now let's operate on objects """

    # create first company
    fruits_company = Company('Fruits', address='Ocean street, 1')
    print(fruits_company)

    # add some employees
    alex = Engineer('Alex', 55)
    alex.join_company(fruits_company)
    alex.do_work()
    alex.show_money()

    # add second company
    doors_company = Company('Windows and doors', address='Mountain ave. 10')
    print(doors_company)

    # Alex wants to work for doors
    alex.join_company(doors_company)
    # ups, already haired
    alex.become_unemployed()
    alex.join_company(doors_company)
    alex.do_work()

    # Bill also wants to work for doors
    bill = Engineer('Bill', 20)
    bill.join_company(doors_company)
    bill.do_work()

    # Jane is a very good manager. She wants to work for fruits
    jane = Manager('Jane', 30)
    jane.join_company(fruits_company)
    # Jane works pretty hard. She writes lots of reports
    jane.do_work()
    jane.do_work()

    # Bill wants Jane to be his manager, he leaves doors and joins fruits
    bill.become_unemployed()
    bill.join_company(fruits_company)

    # doors becomes a bankrupt
    doors_company.go_bankrupt()

    # alex becomes unemployed and goes to fruits
    alex.join_company(fruits_company)

    # fruits company has a celebration party
    fruits_company.make_a_party()

    # results
    fruits_company.show_money()
    doors_company.show_money()
    alex.show_money()
    bill.show_money()
    jane.show_money()


if __name__ == '__main__':
    check_yourself()