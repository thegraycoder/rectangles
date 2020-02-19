class Point:
    def __init__(self, x, y):
        """
        Point on a 2D cartesian plane

        :param x: X-coordinate
        :param y: Y-coordinate
        """
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, top_left, bottom_right):
        """
        Rectangle created using top left and bottom right points (Left to Right Diagonal)

        :param top_left: Point on top left corner of rectangle
        :param bottom_right: Point on bottom right corner of rectangle
        """
        self.top_left = top_left
        self.bottom_right = bottom_right

        if self.top_left.x > self.bottom_right.x or self.top_left.y < self.bottom_right.y:
            raise ValueError('Invalid coordinates for rectangle')

    def does_intersect(self, rectangle):
        """
        Check if a rectangle intersects with another

        :param rectangle: The other rectangle
        :return: If rectangles intersect
        """
        # Check if they intersect on X-Axis
        if self.top_left.x > rectangle.bottom_right.x or rectangle.top_left.x > self.bottom_right.x:
            return False

        # Check if they intersect on Y-Axis
        if self.top_left.y < rectangle.bottom_right.y or rectangle.top_left.y < self.bottom_right.y:
            return False

        # Check if 1st rectangle is inside the 2nd
        if self.top_left.x < rectangle.top_left.x and rectangle.bottom_right.x < self.bottom_right.x:
            return False

        # Check if 2nd rectangle is inside the 1st
        if rectangle.top_left.x < self.top_left.x and self.bottom_right.x < rectangle.bottom_right.x:
            return False

        return True

