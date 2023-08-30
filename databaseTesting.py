import sqlite3
from database import Bollo
from time import sleep

test =Bollo()
# number of data passed
#print(len(test.seeAllData()))
#see to find departement passed
#print(test.inWhichDepartement('3-03279AA'))
# leave it as it there is problem here '3-03279AA' and 'HRGS Olympia site'
#print(test.seeAllData())
#see the plate Numbers in the department
#lst=test.seeDepartementPlateNo('HRGS')
#print(len(lst))
#print(test.DepartementExists('GM OPERATIONS'))
#lst=test.seePlateNoAndRemark('HRGS')
#data=[]
#for i in lst:
#   if i[1]=="":
#      data.append("<td>"+i[0]+"</td>"+"<td>"+"Remark None"+"</td>")
# else:
#    data.append("<td>"+i[0]+"</td>"+"<td>"+i[1]+"</td>")
#print(lst)

con=sqlite3.Connection('Bollo.db')
pointer=con.cursor()
query="UPDATE Bollo SET REMARK= ? where PLATE_NO= ?"
pointer.execute(query,('checked','3AAA123'))
con.commit()

