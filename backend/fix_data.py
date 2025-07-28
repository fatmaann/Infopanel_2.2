import sqlite3

conn = sqlite3.connect('database_datetime_corrected_test.sqlite')
cursor = conn.cursor()

#cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#tables = cursor.fetchall()
#print("Список таблиц:")
#for table in tables:
#    print(table[0])

conn.commit()
conn.close()
