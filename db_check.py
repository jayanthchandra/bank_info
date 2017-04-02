import sqlite3

conn = sqlite3.connect('Bank.db')
print "Opened database successfully";

cursor = conn.execute("SELECT BANK,IFSC,MICR,BRANCH,ADDRESS,CONTACT,CITY,DISTRICT,STATE from Bank Where BRANCH='VIDHARBHA KONKAN GRAMIN BANK HO NAGPUR'")
for row in cursor:
   print "Bank Name = ", row[0]
   print "IFSC = ", row[1], "\n"

print "Operation done successfully";
conn.close()