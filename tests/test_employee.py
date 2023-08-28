import pytest


@pytest.mark.parametrize('amount', [10, 20, 30])
def test_put_money_into_my_wallet(amount, define_company, define_employee):
    fruits_company = define_company
    employee = define_employee
    fruits_company.add_employee(employee)

    employee.put_money_into_my_wallet(amount)
    assert employee.show_money() == amount
