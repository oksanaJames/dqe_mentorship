from src.transformation.geometry import Geometry
import pytest


@pytest.mark.parametrize('side', [[6, 6, 6], [4, 4, 6], [4, 5, 6]])
def test_is_a_triangle(side):
    """Ensure that given a valid set of equilateral/isosceles/scalene triangle sides, is_triangle will return True."""
    assert Geometry.is_triangle(side[0], side[1], side[2])


def test_is_not_a_triangle():
    """Ensure that given an invalid set of triangle sides the is_triangle method will return False."""
    assert not Geometry.is_triangle(0, 1, 2)


@pytest.fixture
def dimension() -> list[float]:
    return [1.0, 2.0, 3.0]


def test_volume_rectangular_prism(dimension):
    """Ensure that the rectangular_prism function calculates the volume correctly."""
    assert Geometry.volume_rectangular_prism(dimension[0], dimension[1], dimension[2]) == 6.0


def test_volume_rhombic_prism(dimension):
    """Ensure that the rhombic_prism function calculates the volume correctly."""
    assert Geometry.volume_rhombic_prism(dimension[0], dimension[1], dimension[2]) == 3.0


def test_volume_rectangular_pyramid(dimension):
    """Ensure that the rectangular_pyramid function calculates the volume correctly."""
    assert Geometry.volume_rectangular_pyramid(dimension[0], dimension[1], dimension[2]) == 2.0