from graphics import *


def draw_die(win, x, y, size=1, value=1):
    die = Rectangle(Point(x, y), Point(x + size, y + size))
    die.setOutline("black")
    die.draw(win)

    pip_radius = 0.05 * size
    pip_positions = {
        1: [(0.5, 0.5)],
        2: [(1/3, 0.5), (2/3, 0.5)],
        3: [(0.25, 0.5), (0.5, 0.5), (0.75, 0.5)],
        4: [(1/3, 1/3), (2/3, 1/3), (1/3, 2/3), (2/3, 2/3)],
        5: [(1/3, 1/3), (2/3, 1/3), (1/3, 2/3), (2/3, 2/3), (0.5, 0.5)],
        6: [(1/3, 1/3), (2/3, 1/3), (1/3, 0.5), (2/3, 0.5), (1/3, 2/3),
            (2/3, 2/3)],
    }

    for offset_x, offset_y in pip_positions[value]:
        pip = Circle(Point(x + (offset_x * size), y + (offset_y * size)),
                     pip_radius)
        pip.setFill("black")
        pip.draw(win)

def main():
    win = GraphWin("Dice", 1200, 200)
    win.setCoords(0, 0, 6, 1)

    for i in range(6):
        draw_die(win, i, 0, 1, i+1)

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()