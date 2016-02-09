

sentence = "List Comprehensions are the Greatest!"


def remove_vowels(word):
    return ''.join([char for char in word if char.lower() not in 'aeiou'])
print(remove_vowels(sentence))

##############

data = open("dataset", "r")
content = data.readlines()
data.close()


def water_temp_and_date(item):
    return [line.split(',')[-2:] for line in item]
last_two = (water_temp_and_date(content))
print(last_two)

def water_list_string_to_float(item_2):
    return[float(item[0]) for item in item_2[1:]]
second_to_last = (water_list_string_to_float(last_two))
print(second_to_last)

def celcius_to_farenheight(item_3):
    return[int((temp * 9/5) + 32) for temp in item_3]
print(celcius_to_farenheight(second_to_last))

def date_and_wave_height(item_4):
    wave_height = [line.split(',')[1] for line in item_4[1:]]
    day = [line.split(',')[-1] for line in item_4[1:]]
    my_dict = {x: y for x in day for y in wave_height}
print(date_and_wave_height(content))

