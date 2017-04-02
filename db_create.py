import sqlite3
import csv

class csvrd(object):
    def csvFile(self):

        self.readFile('bank_of_india.csv')

    def readFile(self, filename):
        conn = sqlite3.connect('Bank.db')
        cur = conn.cursor() 
        cur.execute("""CREATE TABLE IF NOT EXISTS Bank(BANK varchar,IFSC varchar,MICR varchar,BRANCH varchar,ADDRESS varchar,CONTACT varchar,CITY varchar,DISTRICT varchar,STATE varchar)""")
        filename.encode('utf-8')
        print "test1"
        with open(filename) as f:
            reader = csv.reader(f)
            for field in reader:
                cur.execute("INSERT INTO Bank VALUES (?,?,?,?,?,?,?,?,?);", field)

        conn.commit()
        conn.close()

c = csvrd().csvFile()