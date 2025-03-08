from graphics import *


def main():
    # Simplest solution - draw each one.
    win = GraphWin("Archery Target", 1000, 1000)
    win.setCoords(0.0, 0.0, 500.0, 500.0)
    center = Point(250, 250)
    center_radius = 20
    '''layer_one = Circle(center, center_radius * 5)
    layer_one.setFill("white")
    layer_one.draw(win)
    layer_two = Circle(center, center_radius * 4)
    layer_two.setFill("black")
    layer_two.draw(win)
    layer_three = Circle(center, center_radius * 3)
    layer_three.setFill("blue")
    layer_three.draw(win)
    layer_four = Circle(center, center_radius * 2)
    layer_four.setFill("red")
    layer_four.draw(win)
    layer_five = Circle(center, center_radius)
    layer_five.setFill("yellow")
    layer_five.draw(win)'''

    # better method
    for i in range(5, 0, -1):
        print('we in here')
        shape = Circle(center, center_radius * i)
        match i:
            case 5: shape.setFill("white")
            case 4: shape.setFill("black")
            case 3: shape.setFill("blue")
            case 2: shape.setFill("red")
            case 1: shape.setFill("yellow")
        shape.draw(win)

    win.getMouse()

main()