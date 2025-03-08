from graphics import *


def main():
    win = GraphWin()
    shape = Rectangle(Point(10, 10), Point(40, 40))
    #shape = Circle(Point(50, 50), 20)
    shape.setFill("red")
    shape.setOutline("blue")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        #c = shape.getCenter()
        #dx = p.getX() - c.getX()
        #dy = p.getY() - c.getY()
        #shape.move(dx, dy)
        shape = Rectangle(Point(p.getX(), p.getY()), Point(p.getX()+30,
                                                           p.getY()+30))
        shape.setFill("red")
        shape.setOutline("blue")
        shape.draw(win)

    outPutText = Text(Point(125, 50), "Click anywhere to quit.")
    outPutText.draw(win)
    z = win.getMouse()
    win.close()

main()