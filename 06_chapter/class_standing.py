"""
Calculate class standing by credits earned:
0 - 6: freshman
7 - 15: sophomore
16 - 25: junior
26+: senior
"""


def get_hours():
    while True:
        try:
            hours = int(input("Enter the number of hours completed: "))
            break
        except ValueError:
            print("Enter a valid integer only.")
    return hours


def get_class_from_hours(hours):
    if hours < 7:
        return "freshman"
    elif hours <= 15:
        return "sophomore"
    elif hours <= 25:
        return "junior"
    else:
        return "senior"

def main():
    hours = get_hours()
    level = get_class_from_hours(hours)
    print(f"With {hours} completed hours, the student is a {level}.")
     

if __name__ == "__main__":
    main()
    