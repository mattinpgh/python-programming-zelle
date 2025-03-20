"""
Compute fuel efficiency:
prompt for starting odometer reading
for each leg: get current odometer and amount of fuel used
signal end of trip with blank entry
print out mpg per leg print out total mpg
"""

def main():
    try:
        starting_odometer =  int(input("Enter the odometer reading at the beginning of the trip: "))
    except ValueError:
        print("The odometer reading must be an integer.")

    count = 1
    total_fuel = 0
    current_odometer = starting_odometer
    last_odometer_reading = starting_odometer

    while True:
        current_odometer = input(f"After completing {count} leg(s) of your trip, what is your new odometer reading? ")
        if current_odometer == "":
            break
        else:
            current_odometer = int(current_odometer)
        current_fuel = int(input("How much fuel did you use on this leg? "))

        leg_miles = int(current_odometer) - int(last_odometer_reading)
        leg_mpg = leg_miles / current_fuel
        total_fuel += current_fuel
        last_odometer_reading = current_odometer

        print(f"On this leg of the trip, your mileage was {leg_mpg:.2f} MPG.")
        count += 1

    total_mpg = (last_odometer_reading - starting_odometer) / total_fuel
    print(f"The mileage for your entire trip was {total_mpg:.2f} MPG.")

if __name__ == "__main__":    
    main()
