from graphics import *

def main():
    win = GraphWin("Convert", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    Text(Point(1, 3), "   Celsius Temperature").draw(win)
    Text(Point(1, 1), "Fahrenheit Temperature").draw(win)

    inputText = Entry(Point(2.25, 3), 5)
    inputText.setText("0.0")
    inputText.draw(win)

    outputText = Text(Point(2.25, 1), "")
    outputText.draw(win)

    button = Text(Point(1.5, 2), "Convert it!")
    button.draw(win)

    win.getMouse()

    celsius = float(inputText.getText())
    fahrenheit = (9.0 / 5.0) * celsius + 32

    outputText.setText(round(fahrenheit, 2))
    button.setText("Quit")

    win.getMouse()
    win.close()

main()