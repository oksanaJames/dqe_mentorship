class Geometry:
    name = ""

    def __init__(self):
        self.name = "NoName"

    def is_triangle(side_1: int, side_2: int, side_3: int) -> bool:
        """
        Given 3 side lengths, determine if the sides can create a triangle.

        :param side_1: A side of a potential triangle
        :param side_2: A side of a potential triangle
        :param side_3: A side of a potential triangle
        """
        is_triangle = False

        if (side_1 + side_2 > side_3) and (side_1 + side_3 > side_2) and (side_2 + side_3 > side_1):
            is_triangle = True

        return is_triangle

    def volume_rectangular_prism(length: float, width: float, height: float) -> float:
        return length * width * height

    def volume_rhombic_prism(long_diagonal: float, short_diagonal, length: float) -> float:
        return long_diagonal * short_diagonal * length * 0.5

    def volume_rectangular_pyramid(length: float, width: float, height: float) -> float:
        return length * width * height / 3
