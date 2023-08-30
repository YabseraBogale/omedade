import sqlite3 
import datetime
from time import sleep


class Bollo():

    def __init__(self):
        self.connection=sqlite3.Connection("Bollo.db",check_same_thread=False)
        self.pointer=self.connection.cursor()

    def insertIntoTableNew(self,PLATE_NO,DEPARTEMENT,REMARK):
        query="insert into Bollo(PLATE_NO,DEPARTEMENT,REMARK) values(?,?,?)"
        self.pointer.execute(query,(PLATE_NO,DEPARTEMENT,REMARK))
        self.connection.commit()
        return "Added"
    
    def seeAllData(self):
        query="select * from Bollo"
        self.pointer.execute(query)
        self.result=self.pointer.fetchall()
        self.lst=[]
        if type(self.result)==type(None):
            return "NO Data have supplied"
        for i in self.result:
            self.lst.append(i)
        return self.lst

    def seeDepartementPlateNo(self,DEPARTEMENT):
        query="select * from Bollo where DEPARTEMENT=(?)"
        self.pointer.execute(query,(DEPARTEMENT,))
        self.result = self.pointer.fetchall()
        self.lst=[]
        if type(self.result)==type(None):
            return "No Cars in the the Departement"
        for i in self.result:
            self.lst.append(i)
        return self.lst
    
    def DepartementExists(self,DEPARTEMENT):
        query="select count(DEPARTEMENT) from Bollo where DEPARTEMENT=(?)"
        self.pointer.execute(query,(DEPARTEMENT,))
        self.result=self.pointer.fetchone()
        if int(self.result[0])>=1:
            return True
        return False
    
    def UpdateRemark(self,REMARK,PLATE_NO):
        query="UPDATE Bollo SET REMARK= ? where PLATE_NO= ?"
        self.prev=self.previousBollo(PLATE_NO)
        if self.prev=="Saved":
            self.connection.execute(query,(REMARK,PLATE_NO))
            self.connection.commit()
            return "Updated"
        return "Falied"
    
    def giveTime(self):
        now=str(datetime.datetime.now()).split(',')[0].split('.')[0]
        return now

    def previousBollo(self,PLATE_NO):
        query="insert into updateBollo(remark_date,remark,plate_no) values(?,?,?)"
        self.pointer.execute(query,(self.giveTime(),self.giveRemark(PLATE_NO),PLATE_NO))
        self.connection.commit()
        return "Saved"

    def seePlateNoAndRemark(self,DEPARTEMENT):
        query="select PLATE_NO,REMARK from Bollo where DEPARTEMENT=(?)"
        self.pointer.execute(query,(DEPARTEMENT,))
        self.result=self.pointer.fetchall()
        if type(self.result)==type(None):
            return "No Cars in the Departement"
        self.lst=[]
        for i in self.result:
            self.lst.append(i)
        return self.lst
    
    def giveRemark(self,PLATE_NO):
        query="select REMARK from Bollo where PLATE_NO=?"
        self.pointer.execute(query,(PLATE_NO,))
        self.result=self.pointer.fetchone()
        return self.result[0]

    def inWhichDepartement(self,PLATE_NO):
        query="select * from Bollo where PLATE_NO=(?)"
        self.pointer.execute(query,(PLATE_NO,))
        self.result=self.pointer.fetchone()
        if type(self.result)==type(None):
            return "No Such Plate Number in the All Departements"
        return str(self.result[1])

    def doesDepartementHavePlateNO(self,PLATE_NO,DEPARTEMENT):
        query="select PLATE_NO,DEPARTEMENT from Bollo where PLATE_NO= ? and DEPARTEMENT= ?"
        self.pointer.execute(query,(PLATE_NO,DEPARTEMENT))
        self.result=self.pointer.fetchone()
        if type(self.result)==type(None):
            return False
        return True

    def getRemarkDate(self,PLATE_NO):
        query="select REMARK_DATE,REMARK from updateBollo where PLATE_NO=?;"
        self.pointer.execute(query,(PLATE_NO,))
        self.result=self.pointer.fetchall()
        if type(self.result)==type(None):
            return "No Remark Date"
        self.lst=[]
        for i in self.result:
            self.lst.append(i)
        return self.lst


