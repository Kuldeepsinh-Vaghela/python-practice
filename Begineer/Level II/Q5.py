# You are developing a program that analyzes weather data. Write
# a Python function that takes a list of temperature readings for a
# specific location and determines the average temperature, highest
# temperature, and lowest temperature.
# Input: temperature_readings = [25, 28, 21, 24, 27]
# Output:
# Average Temperature: 25.0
# Highest Temperature: 28
# Lowest Temperature: 21


def temp_analyzer(lst):
    min_temp = min(lst)
    max_temp = max(lst)
    sum_temp = sum(lst)
    avg_temp = sum_temp/len(lst)

    print(f"Highest Temperature: {max_temp}\n"
          f"\nLowest Temperature: {min_temp}\n"
          f"\nAverage Temperature: {avg_temp}")


answer = temp_analyzer([25,28,21,24,27])