"""
Counting heating days and cooling degree days over a span
accept a span of days
if the day's average temperature is below 60, add the degrees to the running heating degree days
if the day's average temperature is above 80, add the degrees to the running cooling degree days
print both days

"""

def get_degree_days(temp):
    heat_degrees = 0.0
    cool_degrees = 0.0


    if temp < 60.0:
        heat_degrees = 60.0 - temp
    elif temp > 80.0:
        cool_degrees = temp - 80.0

    return heat_degrees, cool_degrees


def main():
    heating_degree_days = 0.0
    cooling_degree_days = 0.0

    while True:
        temp = input("Enter the day's average temperature (enter 'x' to quit): ")
        if not temp.isdigit():
            if temp == "x" or temp == "X":
                break
            print("You must enter a number or 'x' to quit")
        else:
            temp = float(temp)
            heat, cool = get_degree_days(temp)
            heating_degree_days += heat
            cooling_degree_days += cool

    print(f"Heating degree days: {heating_degree_days}")
    print(f"Cooling degree days: {cooling_degree_days}")

if __name__ == "__main__":
    main()
