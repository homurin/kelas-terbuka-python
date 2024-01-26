import datetime as dt
import os
import string
import random

student_template = {
    'student_id': '0000',
    'name': 'name',
    'birthdate': dt.datetime(1945, 1, 1)
}

list_of_student = {}


while True:
    student = dict.fromkeys(student_template.keys())
    student['student_id'] = input('student id: ')
    student['name'] = input('student name: ')
    BIRTH_YEAR = int(input('birth year (YYYY): '))
    BIRTH_MONTH = int(input('birth month (MM): '))
    BIRTH_DAY = int(input('birth day (DD) :'))
    student['birthdate'] = dt.datetime(BIRTH_YEAR, BIRTH_MONTH, BIRTH_DAY)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    list_of_student.update({KEY: student})
    os.system('clear')

    print(f"{'KEY':<2} {'STUDENT_ID':<12} {'NAME':<20} {'BIRTHDATE'}")
    print('='*50)
    for student in list_of_student:
        KEY = student
        NAME = list_of_student[KEY]['name']
        STUDENT_ID = list_of_student[KEY]['student_id']
        BIRTHDATE = list_of_student[KEY]['birthdate'].strftime("%x")

        print(f'{KEY:<2} {STUDENT_ID:<12} {NAME:<20} {BIRTHDATE}')
    is_done = input('exit program [y/N]: ')
    if (is_done == 'n'):
        break
