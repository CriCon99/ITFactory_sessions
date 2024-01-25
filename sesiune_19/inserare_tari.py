import sqlite3
import csv
from sesiune_19 import constants

# -> 4
conn = sqlite3.connect(constants.DATABASE)
cursor = conn.cursor()

insert_countries = []
with open('countries.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        row[-1] = row[-1].replace('mil', '')
        insert_countries.append(row)
script = '''
INSERT INTO countries( name, code, continent_id, population)
VALUES (?,?,?,?);
'''

cursor.executemany(script, insert_countries)
conn.commit()
conn.close()
