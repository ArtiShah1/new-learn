import random
import pandas
# LIST & dICTIONARY COPREHENSIONS
#  New_list =[new_item for item in list]
# new_list = [new_list for item in list if test]

names = ['Amy','Aarati', 'Pushan', 'Jigna', 'siddharth', 'mahinas', 'dhabalia','Shahshah']

short_names = [name.upper() for name in names if len(name) < 4]
long_names = [name.upper() for name in names if len(name) > 3]
print(short_names,long_names)

name = "Arti"
letters_list = [letter for letter in name]
print(letters_list)

# range(1,5)
range_list = [num * 2 for num in range(1,5)]
print(range_list)

names = ['Amy', 'Aarati', 'Pushan', 'Jigna', 'siddharth', 'mahinas', 'dhabalia',  'Shahshah']
students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)

passed_students = {student_name : score for (student_name, score) in students_scores.items() if score >= 60}
print("total pass students" , passed_students)

student_dict = {
    "student" : ["Angela", "Mark","Lilly", "James"],
    "score" : [56, 76, 98, 82]
}
# Looping through dictionaries
# for (key, value) in student_dict.items():
#     print("key value", key)

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a data frame
for(key, value) in student_data_frame.items():
    print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)

# {new_key: new_value for (index, row) in df.iterrows()}
# --------------------****-----------------
# todo 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

dict_data = pandas.read_csv("nato_alphabet.csv")
# def alfa(**kwargs):
#     print(kwargs)
# alfa("A","Alfa")

print(dict_data. to_dict())
phonetic_dict = {row.letter: row.code for (index, row) in dict_data.iterrows()}
print(phonetic_dict)


# todo 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phpnetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phpnetic()
    else:
        print(output_list)

generate_phpnetic()
