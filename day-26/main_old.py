# numbers = [1, 2, 3]
#
#
# def square(x: int) -> int:
#     return x * x
#
#
# new_list: list[int] = [(lambda x: square(x) * square(x + 1))(number) for number in numbers if number % 2 == 0]
# print(new_list)
#
# new_numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_number = [number**2 for number in new_numbers]
# print(squared_number)
#
# even_numbers = [number for number in new_numbers if number % 2 == 0]
# print(even_numbers)

# with open("file1.txt") as f:
#     file_1_numbers = [int(line.strip()) for line in f.readlines()]
#
# with open("file2.txt") as f:
#     file_2_numbers = [int(line.strip()) for line in f.readlines()]
#
# result = [number for number in file_1_numbers if number in file_2_numbers]

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#
# result = {word.strip(): len(word.strip()) for word in sentence.split()}

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}


def celcius_to_fahrenheit(celcius: int) -> float:
    return celcius * 9 / 5 + 32


result = {key: celcius_to_fahrenheit(value) for key, value in weather_c.items()}
print(result)
