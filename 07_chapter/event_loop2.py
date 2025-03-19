"""
color changing window with check instead of get
"""

from graphics import *


def handle_key(k, win):
    if k == "r":
        win.setBackground("pink")
    elif k == "w":
        win.setBackground("white")
    elif k == "g":
        win.setBackground("lightgray")
    elif k == "b":
        win.setBackground("lightblue")


def handle_click(pt, win):
    entry = Entry(pt, 10)
    entry.draw(win)

    while True:
        key = win.getKey()
        if key == "Return": 
            break

    entry.undraw()
    typed = entry.getText()
    Text(pt, typed).draw(win)

    win.checkMouse()


def main():
    win = GraphWin("Click and Type", 500, 500)

    while True:
        key = win.checkKey()
        if key == "q":
            break

        if key:
            handle_key(key, win)

        pt = win.checkMouse()
        if pt:
            handle_click(pt, win)

    win.close()

if __name__ == "__main__":
    main()