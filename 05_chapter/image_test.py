# Testing the image display features of graphics.py
from graphics import GraphWin, Image, Point


def main():
    win = GraphWin("Image Test", 1920, 1080)
    win.setCoords(0, 0, 1000, 562)
    testy = Image(Point(500, 231), "testy.gif")
    testy.draw(win)
    win.getMouse()

main()
