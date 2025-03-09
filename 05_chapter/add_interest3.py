from graphics import Text, Point


def add_interest(balance, rate):
    new_balance = float(balance.getText()) * (1+rate)
    balance.setText(str(new_balance))


def test():
    amount = Text(Point(0, 0), "1000")
    rate = 0.05
    add_interest(amount, rate)
    print(amount.getText())
