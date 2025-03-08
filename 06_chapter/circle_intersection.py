from graphics import *
from math import sqrt


def main():
    circle_radius = float(input("Input the radius of the circle: "))
    y_intercept = float(input("Enter the y-intercept of the line: "))

    win = GraphWin("Circle Intersection", 640, 480)
    win.setCoords(-10, -10, 10, 10)

    circ = Circle(Point(0,0), circle_radius)
    circ.setOutline("black")
    circ.draw(win)
    
    hor_line = Line(Point(-10, y_intercept), Point(10, y_intercept))
    hor_line.draw(win)

    x_intercept = sqrt((circle_radius ** 2) - (y_intercept ** 2))

    point1 = Point(x_intercept, y_intercept)
    point2 = Point(-x_intercept, y_intercept)

    point1.setFill("red")
    point2.setFill("red")    
    point1.draw(win)
    point2.draw(win)

    print(f"The x-intercepts are {x_intercept} and -{x_intercept}")

    win.getMouse()
    win.close()

main()
