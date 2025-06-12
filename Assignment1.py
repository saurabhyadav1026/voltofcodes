def convert_temperature(temp, unit):
    if unit == 'F':
        # Convert Fahrenheit to Celsius
        celsius = (temp - 32) * 5/9
        return round(celsius, 2)
    elif unit == 'C':
        # Convert Celsius to Fahrenheit
        fahrenheit = (temp * 9/5) + 32
        return round(fahrenheit, 2)
    else:
        return "Invalid option. Please use 'F' or 'C'."
