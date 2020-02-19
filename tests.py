import unittest
from models import Point, Rectangle


class MyTestCase(unittest.TestCase):
    def test_top_left_intersection(self):
        p1 = Point(-1, 1)
        p2 = Point(1, -1)
        rectangle1 = Rectangle(p1, p2)

        p3 = Point(-2, 2)
        p4 = Point(0, 0)
        rectangle2 = Rectangle(p3, p4)

        self.assertEqual(rectangle1.does_intersect(rectangle2), True)

    def test_top_right_intersection(self):
        p1 = Point(-1, 1)
        p2 = Point(1, -1)
        rectangle1 = Rectangle(p1, p2)

        p3 = Point(0, 2)
        p4 = Point(2, 0)
        rectangle2 = Rectangle(p3, p4)

        self.assertEqual(rectangle1.does_intersect(rectangle2), True)

    def test_bottom_left_intersection(self):
        p1 = Point(-1, 1)
        p2 = Point(1, -1)
        rectangle1 = Rectangle(p1, p2)

        p3 = Point(-2, 0)
        p4 = Point(0, -2)
        rectangle2 = Rectangle(p3, p4)

        self.assertEqual(rectangle1.does_intersect(rectangle2), True)

    def test_bottom_right_intersection(self):
        p1 = Point(-1, 1)
        p2 = Point(1, -1)
        rectangle1 = Rectangle(p1, p2)

        p3 = Point(0, 0)
        p4 = Point(2, -2)
        rectangle2 = Rectangle(p3, p4)

        self.assertEqual(rectangle1.does_intersect(rectangle2), True)

    def test_rectangle_inside_other_rectangle(self):
        p1 = Point(-1, 1)
        p2 = Point(1, -1)
        rectangle1 = Rectangle(p1, p2)

        p3 = Point(0, 0)
        p4 = Point(0, 0)
        rectangle2 = Rectangle(p3, p4)

        self.assertEqual(rectangle1.does_intersect(rectangle2), False)

    def test_rectangle_above_rectangle(self):
        p1 = Point(-1, 0)
        p2 = Point(1, -1)
        rectangle1 = Rectangle(p1, p2)

        p3 = Point(-2, 2)
        p4 = Point(2, 1)
        rectangle2 = Rectangle(p3, p4)

        self.assertEqual(rectangle1.does_intersect(rectangle2), False)

    def test_rectangle_beside_rectangle(self):
        p1 = Point(-1, 0)
        p2 = Point(0, -1)
        rectangle1 = Rectangle(p1, p2)

        p3 = Point(1, 1)
        p4 = Point(2, -2)
        rectangle2 = Rectangle(p3, p4)

        self.assertEqual(rectangle1.does_intersect(rectangle2), False)


if __name__ == '__main__':
    unittest.main()
