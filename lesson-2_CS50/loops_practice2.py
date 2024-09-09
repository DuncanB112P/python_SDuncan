students = ['Hermione', 'Harry', 'Ron']

'''for student in students:
    print(student)'''


'''for i in range(len(students)):  #using 'len' to identify the length of the list for Python to iterate through
    print(students[i])'''




# DICTIONARIES
    
'''students = {
    'Hermione': 'Griffyndor',
    'Harry': 'Gryffindor',
    'Draco': 'Slytherin',
}

for student in students:
    print(student, students[student], sep=', ')'''


# LIST OF DICTIONARIES

'''students = [
    {'name': 'Hermione', 'house': 'Griffyndor', 'patronus': 'Otter'},
    {'name': 'Harry', 'house': 'Griffyndor', 'patronus': 'Stag'},
    {'name': 'Ron', 'house': 'Griffyndor', 'patronus': 'Dog'},
    {'name': 'Draco', 'house': 'Slytherin', 'patronus': 'None'}
]

for student in students:
    print(student['name'], student['house'], student['patronus'], sep=', ')'''


household = [
    {'name': 'Sam', 'age': '47'},
    {'name': 'Stepanie', 'age': '41'},
    {'name': 'Preston', 'age': '16'},
    {'name': 'Mackenzie', 'age': '13'}
]

for person in household:
    print(person['name'], person['age'])
    