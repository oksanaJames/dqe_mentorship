import re

"""
Multiply numbers on 2 with regexp and return replaced text
"""

football_text = """
Із 35 футболістів, які забили як мінімум 7 голів на чемпіонатах світу, тільки у трьох з них середній показник
перевищує 2 гола за гру. Ці 35 гравців представляють 14 футбольних збірних.
"""


def multiply_numbers(text, multiplier=2):
    if text.group(0).isdigit():
        return str(int(text.group(0)) * multiplier)
    else:
        return text.group(0)


if __name__ == '__main__':
    print(f"Original text is: {football_text}")
    res = re.sub(r'\d+', multiply_numbers, football_text)
    print(res)