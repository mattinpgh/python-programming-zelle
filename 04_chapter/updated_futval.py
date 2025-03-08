from graphics import *

def main():
    print("this program plots the growth of a 10-year investment")

    win = GraphWin("Investment Growth Chart", 640, 480)
    win.setBackground("white")
    win.setCoords(-1.75, -800, 11.5, 10400)
    Text(Point(-1, 0), ' 0.0k').draw(win)
    Text(Point(-1, 2500), ' 2.5k').draw(win)
    Text(Point(-1, 5000), ' 5.0k').draw(win)
    Text(Point(-1, 7500), ' 7.5k').draw(win)
    Text(Point(-1, 10000), '10.0k').draw(win)

    Text(Point(2, -600), "Enter the initial principal: ").draw(win)
    principal_text = Entry(Point(4.33, -550), 5)
    principal_text.setText("2500")
    principal_text.draw(win)

    Text(Point(7.5, -600), "Enter the annualized interest rate: ").draw(win)
    apr_text = Entry(Point(10.5, -550), 5)
    apr_text.setText("0.025")
    apr_text.draw(win)

    win.getMouse()
    apr = float(apr_text.getText())
    principal = float(principal_text.getText())

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
