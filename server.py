from flask import Flask
from flask import jsonify,redirect
import xlrd
import csv
import json 
import sqlite3

app = Flask(__name__)
# bank_list=list()

# def csv_from_excel():

#    wb = xlrd.open_workbook('bank_of_india.xls')
#    sh = wb.sheet_by_name('Sheet27')
#    your_csv_file = open('bank_of_india.csv', 'wb')
#    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
#    for rownum in xrange(sh.nrows):
#        wr.writerow(sh.row_values(rownum))
#    your_csv_file.close()

#    with open('bank_of_india.csv', 'rb') as f:
# 	      reader = csv.reader(f)
# 	      bank_list = list(reader)

#    bank_list.pop(0)
#    return bank_list



@app.route('/')
def hello_world():
    return 'IFSC Portal'

@app.route('/<IFSCd>',methods=['GET'])
def getinfo(IFSCd):
	#print IFSC
	#print len(bank_list)
	#print bank_list
	conn = sqlite3.connect('Bank.db')
	
	cursor = conn.execute("SELECT BANK,IFSC,MICR,BRANCH,ADDRESS,CONTACT,CITY,DISTRICT,STATE from Bank Where IFSC=\'"+IFSCd+"'")
	for row in cursor:
	   # print "Bank Name = ", row[0]
	   # print "IFSC = ", row[1], "\n"
	   return row[0]+" "+row[3]

	conn.close()

	   # print "IFSC = ", row[1],
	# for sublist in bank_list:
	# 	if sublist[1] == IFSC :
	# 		return json.dumps(sublist)
	return redirect('/Error')

@app.route('/<Bank>/<City>/<Branch>',methods=['GET'])
def getBankInfo(Bank,City,Branch):
	print Bank,City,Branch
	for sublist in bank_list:
		if (all(x in sublist for x in [Bank,City,Branch])) == True :
			return sublist[1]
	return redirect('/Error')

@app.route('/Error')
@app.errorhandler(404)
def errorpage():
	return "Error in the Input"



if __name__ == '__main__':
	#bank_list=csv_from_excel()
	#	app.debug(True)
	app.run(debug=True)