from functools import wraps
import time


def timeit(threshold=None):
    def inner_func(func):
        @wraps(func)
        def timeit_wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            total_time = end_time - start_time
            if (threshold is None) or (total_time > threshold):
                print(f'Function {func.__name__} Took {total_time:.4f} seconds')
            return result
        return timeit_wrapper
    return inner_func


class Calculator:
    @timeit(threshold=0.5)
    def calculate_something(self, num):
        """
        an example function that returns sum of all numbers up to the square of num
        """
        total = sum((x for x in range(0, num**2)))
        return total

    @timeit()
    def print_hello(self, message):
        print(f"Hello, it's timeit without threshold - {message}!")

    def __repr__(self):
        return f'calc_object:{id(self)}'


if __name__ == '__main__':
    calc = Calculator()
    calc.calculate_something(10)
    calc.calculate_something(100)
    calc.calculate_something(1000)
    calc.calculate_something(5000)
    calc.calculate_something(10000)
    calc.print_hello("TEST")