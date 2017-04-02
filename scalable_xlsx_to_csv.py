import xlrd
import csv
import os

Bank_List = []

path="C:\Users\jayan_000\Desktop\Razorpay\XLSX_Files"
for bank in os.listdir(path):
	Bank_List.append(path+'/'+bank)

def csv_from_excel(filename):

   wb = xlrd.open_workbook(filename)
   sh = wb.sheet_by_name('Sheet27')
   your_csv_file = open(filename+'.csv', 'wb')
   wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
   for rownum in xrange(sh.nrows):
       wr.writerow(sh.row_values(rownum))
   your_csv_file.close()

for b in Bank_List :
	print b
	csv_from_excel(b)
	