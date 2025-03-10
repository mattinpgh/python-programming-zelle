from graphics import *


def main():
    win = GraphWin("Draw a Triangle", 640, 480)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    triangle = Polygon(p1, p2, p3)
    triangle.setFill("pink")
    triangle.setOutline("red")
    triangle.draw(win)

    message.setText("Click anywhere to quit.")
    win.getMouse()

main()