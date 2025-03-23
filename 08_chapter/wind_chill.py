def wind_chill(wind_speed, temperature):
    return int((35.74 + (0.6215 * temperature) - 
            (35.75 * (wind_speed ** 0.16)) + 
            (0.4275 * temperature * (wind_speed ** 0.16))))

def main():
    windspeed_values = [0,5,10,15,20,25,30,35,40,45,50]
    temperature_values = [-20,-10,0,10,20,30,40,50,60]
    matrix = []

    for idx, value in enumerate(windspeed_values):
        row = [wind_chill(value, x) for x in temperature_values]
        row.insert(0, windspeed_values[idx])
        matrix.append(row)

    matrix.insert(0, temperature_values)

    row_builder = ""
    string_matrix = []
    matrix[0].insert(0, "     ")

    for row in matrix:
        if row == matrix[0]:
            top_string = "Wind Chill Values at Temperature and Windspeed"
            print(top_string)
            print('-' * len(top_string))
        for element in row:
            if element != matrix[0][0]:
                row_builder += f"{element:3d}  "
            else:
                row_builder += element
        string_matrix.append(row_builder)
        row_builder = ""

    for row in string_matrix:
        print(row)

main()