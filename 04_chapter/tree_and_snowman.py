"""
Draw a winter scene with as christmas tree and a snowman

Create the window
set coordinate system
Draw tree
--Draw trunk as rectangle
--Draw triangle
Draw snowman
--Draw three circles atop each other
"""


from graphics import Rectangle, GraphWin, Polygon, Circle, Oval, Point


def main():
    """main function"""
    win = GraphWin("A Winter Scene", 1000, 600)
    win.setCoords(0, 0, 100, 60)

    tree_trunk = Rectangle(Point(14, 10), Point(21, 20))
    tree_trunk.setFill("brown")
    tree_trunk.draw(win)

    tree_top = Polygon(Point(5, 15), Point(30, 15), Point(18, 50))
    tree_top.setFill("green")
    tree_top.draw(win)

    snowman_bottom = Circle(Point(50, 15), 8)
    snowman_bottom.setFill("white")
    snowman_bottom.setOutline("black")
    snowman_bottom.draw(win)

    snowman_top = Circle(Point(50, 25), 6)
    snowman_top.setFill("white")
    snowman_top.setOutline("black")
    snowman_top.draw(win)

    snowman_left_eye = Circle(Point(48, 26), 1)
    snowman_left_eye.setFill("black")
    snowman_left_eye.draw(win)
    snowman_right_eye = snowman_left_eye.clone()
    snowman_right_eye.move(2, 0)
    snowman_right_eye.draw(win)

    snowman_nose = Circle(Point(49, 24), 1)
    snowman_nose.setFill("black")
    snowman_nose.draw(win)

    snowman_mouth = Oval(Point(52, 22), Point(48, 23))
    snowman_mouth.setFill("black")
    snowman_mouth.draw(win)

    win.getMouse()
    win.close()

main()
