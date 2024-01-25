import sqlite3
from pprint import pprint
from sesiune_19 import constants

conn = sqlite3.connect(constants.DATABASE)
cursor = conn.cursor()

# ->5
select_all_countries = '''
select * from countries
order by name;
'''
cursor.execute(select_all_countries)
pprint(cursor.fetchall())

count_all_countries = '''
select count(*) from countries;
'''
cursor.execute(count_all_countries)
pprint(cursor.fetchone())

# -> 6
print(50 * '*')

countries_population_20m = '''
SELECT * FROM countries WHERE population > 20;
'''
cursor.execute(countries_population_20m)
pprint(cursor.fetchall())

# -> 7
print(50 * '*')


countries_starting_with_c = '''
SELECT * FROM countries WHERE name LIKE 'C%';
'''
cursor.execute(countries_starting_with_c)
pprint(cursor.fetchall())

conn.close()
