from src.oop.singleton_pattern import *


def test_singlton_pattern():
    s1 = Alex('Mary', 55)
    s2 = Alex('Den', 45)

    assert id(s1) == id(s2)
