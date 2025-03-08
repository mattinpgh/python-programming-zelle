from graphics import *


def main():
    win = GraphWin("Rectangle Information", 1280, 800)
    win.setCoords(-10, -10, 10, 10)

    message_display = Text(Point(0, -8), "Click in two locations to create a rectangle.")
    message_display.draw(win)

    p1 = win.getMouse()
    p2 = win.getMouse()
    rect = Rectangle(p1, p2)    
    rect.setOutline("black")
    rect.draw(win)

    length = abs(p1.getX() - p2.getX())
    width = abs(p1.getY() - p2.getY())
    area = length * width
    perimeter = 2 * (length + width)

    message_display.setText(f"The length is {length} and the width is {width}\n \
        The perimeter of the rectangle is {perimeter}\n \
        The area of the rectangle is {area}.\n\n \
        Click anywhere to exit.")

    win.getMouse()

main()
