import datetime

student = {
    'name': ['kratos', 'dante', 'doomguy'],
    'nim': ['0000', '0001', '0003'],
    'scholarships': [False, False, True],
    'birthdate': [datetime.datetime(2001, 1, 1), datetime.datetime(2001, 1, 2), datetime.datetime(2001, 1, 3), datetime.datetime(2001, 1, 4)]
}

print(f"{'NIM':<10} {'NAME':<10} {'SCHOLARSHIPS':<15} {'BIRTHDATE':<10}")
print('='*50)
for i in range(0, len(student.get('nim'))):
    NIM = student.get('nim')[i]
    NAME = student.get('name')[i]
    SCHOLARSHIPS = student.get('scholarships')[i]
    BIRTHDATE = student.get('birthdate')[i].strftime("%x")

    print(f"{NIM:<10} {NAME:<10} {SCHOLARSHIPS:^15} {BIRTHDATE:<10}")
