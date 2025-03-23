"""
Accept a quiz score as an input and print out a grade. Use a string as a lookup
table instead of a decision. 5-A, 4-B, 3-C, 2-D, 1-F, 0-F
"""

def main():
    while True:
        try:
            num_score = int(input(
                "Enter your numeric quiz grade" 
                "(an integer between 0 and 5): "))
            if 0<= num_score <= 5:
                break
            print("Ensure your input is an integer between 0 and 5.")
        except ValueError:
            print("Input must be an integer.")

    gradescale = "FFDCBA"
    print(f"Your letter grade is {gradescale[num_score]}")    

main()
