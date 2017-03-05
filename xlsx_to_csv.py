import xlrd
import csv

def csv_from_excel():

   wb = xlrd.open_workbook('bank_of_india.xls')
   sh = wb.sheet_by_name('Sheet27')
   your_csv_file = open('bank_of_india.csv', 'wb')
   wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
   for rownum in xrange(sh.nrows):
       wr.writerow(sh.row_values(rownum))
   your_csv_file.close()

csv_from_excel()

with open('bank_of_india.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)

your_list.pop(0)

print your_list[0]