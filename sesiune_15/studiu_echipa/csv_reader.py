import csv
import json

from tabulate import tabulate


def read(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        return list(reader)


students = read('students.csv')
tabel = tabulate(students[1:], headers=students[0])
print(tabel)

def write_json(filename, data):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        data = []
        for row in reader:
            data.append(row)
    with open(filename, 'w') as f:
        json.dump(students, data, indent=4)


write_json('students.csv')
