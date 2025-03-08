from graphics import *

def main():
    win = GraphWin("Face", 1000, 600)
    win.setCoords(0,0,1000,1000)
    leftEye = Circle(Point(250,750),75)
    leftEye.setFill("blue")
    leftEye.draw(win)
    leftIris = Circle(Point(250,750),25)
    leftIris.setFill("white")
    leftIris.draw(win)
    rightEye = leftEye.clone()
    rightEye.move(500,0)
    rightIris = leftIris.clone()
    rightIris.move(500,0)
    rightEye.draw(win)
    rightIris.draw(win)
    mouth = Polygon(Point(250,450),Point(500,350),Point(750,450))
    mouth.setFill("red")
    mouth.draw(win)
    nose = Circle(Point(500,650),25)
    nose.setFill("yellow")
    nose.draw(win)

    win.getMouse()
    win.close()

main()