from graphics import *


win = GraphWin("Shapes")

center = Point(100,100)
circ = Circle(center, 30)
circ.setFill("red")
circ.draw(win)

label = Text(center, "Red Circle")
label.draw(win)

rect = Rectangle(Point(30, 30), Point(70, 70))
rect.draw(win)

line = Line(Point(20, 20), Point(180, 165))
line.draw(win)

oval = Oval(Point(20, 120), Point(180, 199))
oval.draw(win)
x = input()