from graphics import *

def main():
    print("this program plots the growth of a 10-year investment")

    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annualized interest rate: "))

    win = GraphWin("Investment Growth Chart", 640, 480)
    win.setBackground("white")
    win.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1, 0), ' 0.0k').draw(win)
    Text(Point(-1, 2500), ' 2.5k').draw(win)
    Text(Point(-1, 5000), ' 5.0k').draw(win)
    Text(Point(-1, 7500), ' 7.5k').draw(win)
    Text(Point(-1, 10000), '10.0k').draw(win)

    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill('green')
    bar.setWidth(2)
    bar.draw(win)

    for year in range(1, 11):
        principal = principal * (1 + apr)
        bar = Rectangle(Point(year, 0), Point(year + 1, principal))
        bar.setFill('green')
        bar.setWidth(2)
        bar.draw(win)

    input("Press <Enter> to quit")
    win.close()

main()
