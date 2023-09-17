import pytest
from src.oop.decorator_pattern import *
import sys
import io

exp_msg_calc = 'Function calculate_something Took'
exp_msg_print = 'Function print_hello Took'


@pytest.mark.parametrize('input_number, output_msg',
                         [(10, ''), (100, ''), (1000, ''), (5000, exp_msg_calc), (10000, exp_msg_calc)])
def test_calculate_something(input_number, output_msg):
    calc = Calculator()
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    calc.calculate_something(input_number)
    sys.stdout = sys.__stdout__
    assert output_msg in capturedOutput.getvalue()


def test_print_hello():
    text_to_print = 'from SHERLOCK'
    result_message = f"Hello, it's timeit without threshold - {text_to_print}!"
    calc = Calculator()
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    calc.print_hello(text_to_print)
    sys.stdout = sys.__stdout__
    assert exp_msg_print in capturedOutput.getvalue() and result_message in capturedOutput.getvalue()
