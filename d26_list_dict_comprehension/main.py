# LIST COMPREHENSION
# numbers = [1,2,3]
# new_list = [n+1 for n in numbers]
# print(new_list)

# double_numbers = [n*2 for n in range(1,5)]
# print(double_numbers)

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name.upper() for name in names if len(name) >= 5]
# print(short_names)


# DICT COMPREHENSION
# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# students_scores = {student:random.randint(1,100) for student in names}
# print(students_scores)
# passed_students = {student:score for (student, score) in students_scores.items() if score > 50}
# print(passed_students)


# DICT COMPREHENSION WITH PANDAS
# import pandas
# 
# student_dict = {
#     "student": ["Robert", "James", "Lily"],
#     "score": [56, 76, 98]
# }
# 
# students_df = pandas.DataFrame(student_dict)
#
#  for (index, row) in students_df.iterrows():
#     if row.student == "Robert":
#         print(row.score)


# NATO alphabet
import pandas

data = pandas.read_csv("d26_list_dict_comprehension/nato_phonetic_alphabet.csv")
new_dict = {row.letter:row.code for (index, row) in data.iterrows()}
is_on = True
while is_on:
    word = input("Enter a word :): ").upper()
    try:
        output_list = [new_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        is_on = False
        print(output_list)