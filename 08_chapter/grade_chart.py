from graphics import GraphWin, Rectangle, Point, Text


def main():
    num_scores = int(input("Enter the number of scores: "))

    win = GraphWin("Student Grades", (100 * num_scores), (100 * num_scores))
    win.setCoords(0, 0, 100, (100 * num_scores))

    for i in range(num_scores):
        name, score = input("Enter a last name followed by a space and a score: ").split()
        ll_y = 100 * i
        ur_y = 100 * (i + 1)
        rect = Rectangle(Point(0,ll_y), Point(score, ur_y))
        rect.setOutline("black")
        rect.setFill("white")
        rect.draw(win)
        n_text = Text(Point(25, ((ll_y + ur_y) / 2)), name.title())
        n_text.draw(win)

    win.getMouse()

main()