
from string import punctuation
with open("data_set.txt") as better_open_file:
    better_contents = better_open_file.readlines()

data_matrix = []

for item in better_contents:
    data_matrix.append(item.split(","))

data_matrix.remove(data_matrix[0])


print(data_matrix)

#  Remove all vowels from this sentence List Comprehensions are the Greatest!


def devowel():
    my_sentence = "List Comprehensions are the Greatest!"
    vowels = ('a', 'e', 'i', 'o', 'u')
    output = []
    # '''
    # for x in vowels:
    #     my_sentence = my_sentence.replace(x, "")
    # print(my_sentence)
    # '''
    output = [character for character in my_sentence if character not in vowels]
    return output
print(*devowel())

devowel()


def water_temps():   # Create a list of Water Temps for each day the data set below.
    target_column = []
    target_column = [row[4] for row in data_matrix]
    return target_column
    print(target_column)

print(water_temps())


def water_floats():  # Convert the Water Temps from a string to a float
    target_column = water_temps()
    target_column = [float(item) for item in target_column]
    return target_column
    print(target_column)

print(water_floats())


def temp_convert():  # Convert the Water Temps from Celsius to Fahrenheit rounded to an int
    target_column = water_floats()
    # fahrenheit = (celsius * 1.8) + 32
    target_column = [(item * 1.8 + 32) for item in target_column]
    return target_column
    print(target_column)
print(temp_convert())


def date_dict():  # Create a dictionary with Date as the key and Wave Height as the value

    date_dict = {row[5].replace("\n", ""): row[1] for row in data_matrix}
    return(date_dict)

print(date_dict())
