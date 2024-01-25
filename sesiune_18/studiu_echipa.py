import sqlite3

# CREAREA DE BAZA DE DATE
# conn = sqlite3.connect('clasa_elevi.db')
# cursor = conn.cursor()
# script = '''
# CREATE TABLE IF NOT EXISTS Elevi(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# nume TEXT NOT NULL,
# note REAL DEFAULT 0,
# absente INTEGER DEFAULT 0);
# '''
#
# cursor.executescript(script)

# ADAUGAREA IN BAZA DE DATE
# conn = sqlite3.connect('clasa_elevi.db')
# cursor = conn.cursor()
#
# cursor.execute('''
# insert into Elevi (nume, note, absente)
# Values ("Cristian Constantin", "8", "5");
# ''')
#
# cursor.execute('''
# insert into Elevi (nume, note, absente)
# Values ("Tudor Andrei", "9", "1");
# ''')
#
# cursor.execute('''
# insert into Elevi (nume, note, absente)
# Values ("Dora Maria", "10", "0");
# ''')
#
# conn.commit()
# cursor.execute('select * from Elevi;')
