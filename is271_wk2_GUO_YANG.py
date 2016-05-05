#Task 1a
def day_name(num):
    if num == 1:
        day_name = 'Sunday'
    elif num == 2:
        day_name = 'Monday'
    elif num == 3:
        day_name = 'Tuesday'
    elif num == 4:
        day_name = 'Wednesday'
    elif num == 5:
        day_name = 'Thursday'
    elif num == 6:
        day_name = 'Friday'
    elif num == 7:
        day_name = 'Saturday'
    else:
        break
    return day_name
#print(day_name(1))

#Task 1b
def day_name_2(num):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    return days[num]
#print(day_name_2(1))

#TASK 2
def weekend(day):
    if day == 'Saturday' or day == 'Sunday':
        return True
    else:
        return False
#print(weekend('Saturday'))


#TASK 3a
def max_while(list):
    i = 0
    max = list[0]
    n = len(list)
    while(i < n):
        if max <= list[i]:
            max = list[i]
        i += 1
    return max
#print (max_while ([101, 234, 15, 372, 20, 0]))

#TASK 3b
def max_for(list):
    i = 0
    max = list[0]
    n = len(list)
    for i in range(0, n):
        if max <= list[i]:
            max = list[i]
    return max
#print (max_for ([1,2,3,4,5]))

#TASK 4a
def calculate_fine(days):
    return days * 0.25

#print(calculate_fine(0)) #test codes
#print(calculate_fine(5))

#TASK 4b

def balance_due(list):
    n = len(list)
    sum = 0.0
    for i in range(0, n):
        sum = sum + list[i]["days_overdue"]
    return calculate_fine(sum)
'''
#test codes
my_loans = [
    {'book_ID': 1234, 'title': 'All About A', 'author': 'Mrs. A', 'days_overdue': 10},
    {'book_ID': 1235, 'title': 'Boundless B', 'author': 'Mrs. B', 'days_overdue': 20},
    {'book_ID': 1236, 'title': 'Calling C', 'author': 'Mrs. C', 'days_overdue': 15},
    {'book_ID': 1237, 'title': 'Dreaming D', 'author': 'Mrs. D', 'days_overdue': 30},
]
print (balance_due(my_loans))
'''
#TASK 4c
def display_loans(list):
    n = len(list)
    for i in range(0, n):
        print ("Title: {}".format(list[i]["title"]))
        print ("Author: {}".format(list[i]["author"]))
        print ("DAYS OVERDUE: {}".format(list[i]["days_overdue"]))
        print ("Fine: {}".format(calculate_fine(list[i]["days_overdue"]))) #use calculate_fine()
        print ("")
    print ("TOTAL DUE: {}".format(balance_due(list))) #use calculate_fine
#print(display_loans(my_loans)) #test codes

#TASK 4d
def heavy_users(patrons):
    return [p['name'] for p in patrons if len(p['loans']) >= 10]

'''
patrons = [
    {'name': 'person A',
     'loans': [{}, {}, {}, {}, {}]},
    {'name': 'person B',
     'loans': [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}]},
    {'name': 'person C',
     'loans': [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]},
    {'name': 'person D',
     'loans': [{}, {}, {}, {}, {}]},
    {'name': 'person E',
     'loans': [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]},
    {'name': 'person F',
     'loans': [{}, {}, {}, {}, {}]},
]
print(heavy_users(patrons))
'''
#TASK 4e
def block_list(patrons):
    return [p['name'] for p in patrons if balance_due(p['loans']) >= 25] #use balance_due()
'''
patrons = [
    {'name': 'person A',
     'loans': [{'days_overdue': 10},
               {'days_overdue': 10},
               {'days_overdue': 10},
               {'days_overdue': 10},
               {'days_overdue': 10}]},
    {'name': 'person B',
     'loans': [{'days_overdue': 10},
               {'days_overdue': 10},
               {'days_overdue': 0},
               {'days_overdue': 0},
               {'days_overdue': 0},
               {'days_overdue': 100},
               {'days_overdue': 0},
               {'days_overdue': 0},
               {'days_overdue': 0},
               {'days_overdue': 0}]},
    {'name': 'person C',
     'loans': [{'days_overdue': 10},
               {'days_overdue': 10},
               {'days_overdue': 0},
               {'days_overdue': 0},
               {'days_overdue': 0},
               {'days_overdue': 0},
               {'days_overdue': 0},
               {'days_overdue': 0},
               {'days_overdue': 0},
               {'days_overdue': 0}]},
    {'name': 'person D',
     'loans': [{'days_overdue': 10},
               {'days_overdue': 10},
               {'days_overdue': 10},
               {'days_overdue': 10},
               {'days_overdue': 10}]},
    {'name': 'person E',
     'loans': [{'days_overdue': 10},
               {'days_overdue': 10},
               {'days_overdue': 10},
               {'days_overdue': 10},
               {'days_overdue': 10},
               {'days_overdue': 10},
               {'days_overdue': 20},
               {'days_overdue': 20},
               {'days_overdue': 20},
               {'days_overdue': 20}]},
    {'name': 'person F',
     'loans': [{'days_overdue': 10},
               {'days_overdue': 10},
               {'days_overdue': 0},
               {'days_overdue': 0},
               {'days_overdue': 0},
               {'days_overdue': 0},
               {'days_overdue': 0},
               {'days_overdue': 0},
               {'days_overdue': 0},
               {'days_overdue': 0}]},
]

block_list(patrons)
'''

#TASK 5a
from pprint import pprint
def parse_data(data):
    fields = ('name', 'dob', 'occupation', 'gender', 'married', 'children')
    output = []
    errors = []
    for string in data:
        error = False
        row = {}
        values = string.split(',')
        for index, key in enumerate(fields):
            try:
                value = values[index].strip()
            except:
                errors.append(string)
                error = True
                break
            try:
                if key == 'married':
                    value = bool(value)
                elif key == 'children':
                    value = int(value)
            except:
                value = None
            row[key] = value
        if not error:
            output.append(row)
    return output
'''
#TASK 5a test codes
data = ["John Doe, 1972-03-28, carpenter, Male, False, 0",
        "Jane Doe, 1983-01-16, doctor, Female, True, 3"]
pprint(parse_data(data))
'''

#TASK 5b
from pprint import pprint
def parse_data(data):
    fields = ('name', 'dob', 'occupation', 'gender', 'married', 'children')
    output = []
    errors = []
    for string in data:
        error = False
        row = {}
        values = string.split(',')
        for index, key in enumerate(fields):
            try:
                value = values[index].strip()
            except:
                errors.append(string)
                error = True
                break
            try:
                if key == 'married':
                    value = bool(value)
                elif key == 'children':
                    value = int(value)
            except:
                value = None
            row[key] = value
        if not error:
            output.append(row)
    print('Errors:')
    pprint(errors)
    print('-------')
    return output
'''
#TASK 5b test codes
data = [
        "John Doe, 1972-03-28, carpenter, Male, False, 0",
        "Jane Doe, 1983-01-16, doctor, Female, True, 3",
        "John Deer, 1985-02-26, pilot, Male, Never, 0",
        "Jane Buck, 1987-11-06, lawyer, Female, True, five",
        "Jill Fawn, 1999-10-01, student, Female"
        ]

pprint(parse_data(data))
'''
