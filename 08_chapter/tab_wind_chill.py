from tabulate import tabulate


def wind_chill(wind_speed, temperature):
    return int((35.74 + (0.6215 * temperature) - 
            (35.75 * (wind_speed ** 0.16)) + 
            (0.4275 * temperature * (wind_speed ** 0.16))))


def main():
    windspeed_values = [0,5,10,15,20,25,30,35,40,45,50]
    temperature_values = [-20,-10,0,10,20,30,40,50,60]
    headers = ["MPH"] + temperature_values
    
    # Build data rows
    data = []
    for speed in windspeed_values:
        row = [speed] + [wind_chill(speed, temp) for temp in temperature_values]
        data.append(row)
    
    # Generate table with headers
    table = tabulate(data, headers=headers, tablefmt="github")
    
    # Add title
    title = "Wind Chill Values at Temperature and Windspeed"
    print(title)
    print('-' * len(title))
    print(table)

main()
