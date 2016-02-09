import csv
import datetime

myfile = open("dataset", 'wb')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
wr.writerow(mylist)

def remove_vowels(phrase):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    cons_word = "".join([char for char in phrase if char not in vowels])
    return cons_word


def list_water_temps(csv_file):
    with open(csv_file) as file:
        reader = csv.DictReader(file)
        temp_list = [temp["Water Temp"] for temp in reader]
    return temp_list


def str_to_float(temp_list):
    float_temp_list = [float(temp) for temp in temp_list]
    return float_temp_list


def cel_to_fahren(temp_list):
    fahren_list = [round(temp*9/5+32) for temp in temp_list]
    return fahren_list


def create_waves_dict(csv_file):
    with open(csv_file) as file:
        reader = csv.DictReader(file)
        waves_dict = {row["Date"]: row["Wave Height"] for row in reader}
        return waves_dict


def avg_hw_one(students_dict):
    scores = [
        hw['Homework 1']
        for hw in students_dict.values()
        ]
    hw_average = sum(scores) / len(scores)
    return hw_average


def convert_dates(csv_file):
    with open(csv_file) as file:
        reader = csv.DictReader(file)
        date_list = [datetime.datetime.strptime(row["Date"], '%Y-%m-%d').weekday() for row in reader]
    return date_list


def find_average(dict_list, key):
    working_sum = 0
    for num in dict_list:
        working_sum += float(num[key])
    return round(working_sum / len(dict_list), 2)


student_dict = {'Gale': {'Homework 1': 88, 'Homework 2': 76},
                'Jordan': {'Homework 1': 92, 'Homework 2': 87},
                'Peyton': {'Homework 1': 84, 'Homework 2': 77},
                'River': {'Homework 1': 85, 'Homework 2': 91}}
temperature_list = list_water_temps("buoy.csv")
floats_list = str_to_float(temperature_list)
fahrens = cel_to_fahren(floats_list)
wave_dict = create_waves_dict("buoy.csv")
hw_1_average = avg_hw_one(student_dict)
print(temperature_list)
print(floats_list)
print(fahrens)
print(wave_dict)
print(hw_1_average)
