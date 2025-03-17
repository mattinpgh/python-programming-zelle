"""
Calculate total wages with OT and DT
"""


def calculate_pay(reg_hours, ot_hours, dt_hours, rate):
    reg_pay = reg_hours * rate
    ot_pay = ot_hours * rate * 1.5
    dt_pay = dt_hours * rate * 2
    return reg_pay + ot_pay + dt_pay


def main():
    reg = float(input("Enter regular hours: "))
    ot = float(input("Enter OT hours: "))
    dt = float(input("Enter DT hours: "))
    rate = float(input("Enter rate: "))

    if reg > 40:
        ot += reg - 40
        reg = 40

    print(f"The total pay is ${calculate_pay(reg, ot, dt, rate):.2f}.")


if __name__ == "__main__":
    main()