from src.oop.engineer import Engineer
from src.oop.manager import Manager
import pytest

# This test verify add_employee() and do_tasks() methods from Company class


@pytest.mark.parametrize('employee', [Engineer('Johnny Cash', 55), Manager('Johnny English', 39)])
def test_add_engineer(employee, define_company):
    fruits_company = define_company
    fruits_company.add_employee(employee)
    assert employee in fruits_company.employees


@pytest.mark.parametrize('employee', [Engineer('Johnny Cash', 55), Manager('Johnny English', 39)])
def test_add_employee_already_employed_exception(employee, define_company):
    fruits_company = define_company

    # manually adding an employee to the company list
    fruits_company.employees.append(employee)

    with pytest.raises(Exception) as e_info:
        fruits_company.add_employee(employee)


def test_add_wrong_type_employee_error(define_company):
    fruits_company = define_company

    with pytest.raises(TypeError) as e_info:
        fruits_company.add_employee(fruits_company)


@pytest.mark.parametrize('employee', [Engineer('Johnny Cash', 55)])
def test_do_tasks_engineer(employee, define_company):
    fruits_company = define_company
    fruits_company.add_employee(employee)
    assert fruits_company.do_tasks(employee) == 10 and fruits_company.show_money() == 990


@pytest.mark.parametrize('employee', [Engineer('Johnny Cash', 55)])
def test_do_tasks_not_employed_engineer(employee, define_company):
    fruits_company = define_company

    with pytest.raises(RuntimeError) as e_info:
        fruits_company.do_tasks(employee)


@pytest.mark.parametrize('employee', [Manager('Johnny English', 39)])
def test_do_tasks_manager(employee, define_company):
    fruits_company = define_company
    fruits_company.add_employee(employee)

    with pytest.raises(RuntimeError) as e_info:
        fruits_company.do_tasks(employee)
