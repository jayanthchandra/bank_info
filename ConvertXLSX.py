import os
import sqlite3
import csv

Bank_List = []

#capture all the image from the folder

path="C:\Users\jayan_000\Desktop\Razorpay\XLSX_Files"
for bank in os.listdir(path):
	Bank_List.append(path+'/'+bank)

print Bank_List
conn = sqlite3.connect('Bank.db')
cur = conn.cursor() 
cur.execute("""CREATE TABLE IF NOT EXISTS Bank(BANK varchar,IFSC varchar,MICR varchar,BRANCH varchar,ADDRESS varchar,CONTACT varchar,CITY varchar,DISTRICT varchar,STATE varchar)""")
        
for filename in Bank_List :
    filename.encode('utf-8')
    print "test1"
    with open(filename) as f:
        reader = csv.reader(f)
        for field in reader:
            cur.execute("INSERT INTO Bank VALUES (?,?,?,?,?,?,?,?,?);", field)

conn.commit()
conn.close()


