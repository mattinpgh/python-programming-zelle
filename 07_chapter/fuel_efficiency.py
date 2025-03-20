"""
Compute fuel efficiency:
prompt for starting odometer reading
for each leg: get current odometer and amount of fuel used
signal end of trip with blank entry
print out mpg per leg print out total mpg
"""

def get_input(is_starting=False):
    if is_starting:
        which_odo = "starting"
    else:
        which_odo = "current"

    while True:
        odometer = ""
        try:
            print("Enter a blank line to quit.")
            odometer = abs(int(input(f"Enter the {which_odo} odometer reading: ")))
            if odometer == "":
                return ""
            break
        except ValueError:
            print("The odometer reading must be an integer.")
            

    if not is_starting:
        while True:
            try:
                fuel = abs(int(input(
                    "Enter the amount fuel used during the previous leg: ")))
                break
            except ValueError:
                print("The amount of fuel must be an integer.")

    return odometer, fuel if not is_starting else odometer


def main():
    start_odometer = get_input(True)
    leg_odometer, last_odometer = start_odometer
    fuel_counter = 0
    
    
    while True:
        leg_odometer, leg_fuel = get_input()
        if leg_odometer == "":
            break
        leg_miles = leg_odometer - last_odometer
        leg_efficiency = leg_miles // leg_fuel
        fuel_counter += leg_fuel
        last_odometer = leg_odometer
        print(f"This leg's MPG is {leg_efficiency}.")

    final = (last_odometer - start_odometer) // fuel_counter
    print(f"The total MPG for the trip is {final}")


if __name__ == "__main__":
    main()
