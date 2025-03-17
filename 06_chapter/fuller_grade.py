"""
Take a grade 0 - 100 and return a letter grade
Use the following grading scale:
A: 90 - 100
B: 80 - 89
C: 70 - 79
D: 60 - 69
F: 0 - 59
"""


def input_grade():
    while True:
        try:
            grade = int(input("Enter your grade: "))
            if grade >= 0 and grade <= 100:
                return grade
            else:
                print("Grades must be integers between 0 and 100")
        except ValueError:
            print("Grades must be integers between 0 and 100")
            continue

def calculate_grade(grade):
    return "a" if grade >= 90 else "b" if grade >= 80 else "c" if grade >= 70 \
        else "d" if grade >= 60 else "f"

def main():
    num_grade = input_grade()
    letter_grade = calculate_grade(num_grade)
    print(f"Grade: {letter_grade.upper()}")


if __name__ == "__main__":
    main()