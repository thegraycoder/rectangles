from models import Point, Rectangle

if __name__ == '__main__':
    # Point p1 and p2 create left to right diagonal of rectangle r1
    p1 = Point(0, 4)
    p2 = Point(4, 0)
    r1 = Rectangle(p1, p2)

    # Point p3 and p4 create left to right diagonal of rectangle r2
    p3 = Point(1, 3)
    p4 = Point(3, 1)
    r2 = Rectangle(p3, p4)

    if r1.does_intersect(r2):
        print("The rectangles intersect!")
    else:
        print("The rectangles do not intersect!")
