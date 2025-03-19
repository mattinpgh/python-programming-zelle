"""Gets rectangle info"""
from graphics import GraphWin, Text, Rectangle, Point


def get_rectangle_info(p1, p2):
    """compute the dimensions are, and perimeter of a rectangle"""
    length = abs(p1.getX() - p2.getX())
    width = abs(p1.getY() - p2.getY())
    area = length * width
    perimeter = 2 * (length + width)
    return length, width, area, perimeter


def main():
    """Run the main function to display rectangle information."""
    win = GraphWin("Rectangle Information", 1280, 800)
    win.setCoords(-10, -10, 10, 10)

    message = "Click in two locations to create a rectangle."
    message_display = Text(Point(0, -8), message)
    message_display.draw(win)

    p1, p2 = win.getMouse(), win.getMouse()
    rect = Rectangle(p1, p2)
    rect.setOutline("black")
    rect.draw(win)

    length, width, area, perimeter = get_rectangle_info(p1, p2)

    message = (
        f"The length is {length} and the width is {width}\n"
        f"The perimeter of the rectangle is {perimeter}\n"
        f"The area of the rectangle is {area}.\n\n"
        "Click anywhere to exit."
    )
    message_display.setText(message)

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
