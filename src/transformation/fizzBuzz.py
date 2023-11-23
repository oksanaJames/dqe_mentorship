"""FizzBuzz task
Write a program which prints numbers from 1 to 100 with the following replacements:
- if a number is divisible by 3 then 'Fizz' should be printed instead of number
- if a number is divisible by 5 then 'Buzz' should be printed instead of number
- if a number is divisible by 3 and 5 then 'FizzBuzz' should be printed instead of number
"""


def result(boundary: int) -> list:
    fizzBuzz = []
    for number in range(1, boundary, 1):
        if number % 3 == 0 and not number % 5 == 0:
            fizzBuzz.append("Fizz")
            # print(number, "Fizz")
            continue
        if number % 5 == 0 and not number % 3 == 0:
            fizzBuzz.append("Buzz")
            # print(number, "Buzz")
            continue
        if number % 3 == 0 and number % 5 == 0:
            fizzBuzz.append("fizzBuzz")
            # print(number, "fizzBuzz")
            continue
        else:
            fizzBuzz.append(number)
            # print(number)
    return fizzBuzz


if __name__ == "__main__":

    FizzBuzz = result(100)
    print(FizzBuzz)


