# This program will store my actual objectives
# WSID == "What Should I Do"

# Empty list that will store my objectives
objectives = []

# Objective's dictionarys declarations
one = {
    'name': 'make emilly even more happier',
    'priority': 9,
    'difficult': 'no',
    'WSID': 'continue playing with her, talking with her and giving candys to her;'
}

two = {
    'name': 'become python developer',
    'priority': 9,
    'difficult': 'no',
    'WSID': 'continues studying with this book, read even more code, get even more knowledge;'
}

# Adding the objectives to the list

objectives.append(one)
objectives.append(two)

# Showing Info

print("My name is Isac, and these are my actual objectives: \n")

for objective in objectives:
    # Assign the values to variables for easier understandment
    objective_name = objective['name']
    priority = objective['priority']
    difficult = objective['difficult']
    wsid = objective['WSID']

    # Showing the objectives
    print("\tName: " + objective_name.title() + ";")
    print("\tPriority: " + str(priority) + ";")
    print("\tDifficult: " + difficult + ";")
    print("\tWSID: " + wsid + ".\n")
