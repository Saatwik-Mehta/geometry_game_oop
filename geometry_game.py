from random import randint
import turtle
from typing import Tuple


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle: "Rectangle") -> bool:
        if (
            rectangle.point1.x < self.x < rectangle.point2.x
            and rectangle.point1.y < self.y < rectangle.point2.y
        ):
            return True
        else:
            return False

    """
    Assignment1: 
    Add a new distance method to the Point class.
    The method should calculate the distance from the
    coordinates of the current point (i.e., the self.x and self.y coordinates)
    to the coordinates of any other given point, and such coordinates can be
    provided as x and y arguments to the distance method.
    """

    def calculate_distance_from(self, point: "Point") -> Tuple[int, int]:
        """
        This method calculates the distance between the points given at the time of initalization
        and the points provided in this method as arguments.
        point1 = (5, 6)
        and we have to calculate its distance from (10, 8).
        So, the distance will be the sqrt of sum of the
        square of the difference of x and y coords
        eg:

        x_diff = x1 - x
        y_diff = y1 - y
        ---------------
        distance = sqrt(sum(square(x), square(y)))
        """

        distance_from_x = point.x - self.x
        distance_from_y = point.y - self.y
        return (sum([(distance_from_x**2), (distance_from_y**2)])) ** 0.5


class Rectangle:
    def __init__(self, point1, point2):
        self.point1: Point = point1
        self.point2: Point = point2

    def area(self):
        """
        Formula: length * breadth
        Ex:
        point1: (5, 7)
        point2: (16, 20)

        Length = point2.y - point1.y;
        Breadth = point2.x - point1.x
        Area = Length * Breadth = 13 * 11 = 143
        """
        length = self.point2.y - self.point1.y
        breadth = self.point2.x - self.point1.x

        return length * breadth


class GuiRectangle(Rectangle):
    def draw(self, canvas: turtle.Turtle):
        # relocate the pen to the lower left point
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)
        canvas.pendown()

        # start creating the rectangle
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)


class GuiPoint(Point):
    def display_point(self, canvas:turtle.Turtle, size=5, color='red'):
        # This method will locate the user guessed point on the canvas
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


if __name__ == "__main__":
    point1 = Point(3, 4)
    point2 = Point(10, 8)
    print("total distance: ", point1.calculate_distance_from(point2))

    rectangle = GuiRectangle(
        Point(randint(0, 100), randint(0, 100)),
        Point(randint(100, 200), randint(100, 200)),
    )
    print(
        f"Your Rectangle coordinates are: {rectangle.point1.x}, {rectangle.point1.y} and {rectangle.point2.x}, {rectangle.point2.y}"
    )

    user_point = GuiPoint(
        float(input("Please enter X coord: ")), float(input("Please enter Y coord: "))
    )
    user_area = float(input("Guess rectangle area: "))
    print("Point falls in rectangle: ", user_point.falls_in_rectangle(rectangle))
    print("Your area was off by: ", rectangle.area() - user_area)

    canvas = turtle.Turtle()
    rectangle.draw(canvas)
    user_point.display_point(canvas)
    turtle.done()
