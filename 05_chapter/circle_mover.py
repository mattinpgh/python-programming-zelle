# Circle mover
from graphics import GraphWin, Circle, Point


def move_to(shape, new_center):
    shape.undraw()
    new_circ = Circle(new_center, shape.getRadius())
    new_circ.setFill("black")
    return new_circ


def main():
    win = GraphWin("CircleMover", 1000, 1000)
    win.setCoords(0, 0, 100, 100)

    circ = Circle(Point(50, 50), 10)
    circ.setFill("black")
    circ.draw(win)

    for x in range(0,10):
        circ = move_to(circ, win.getMouse())
        circ.draw(win)

    win.getMouse()

main()

