import MySQLdb
import os

class GetDbData():
    #lists to hold values from db
    #order: course code, course name, credits, prereqs, session #, type, letter, day, time, location, teacher's name
    lList = []
    #order: course code, course name, session #, type, letter, day, time, location
    tuList = []
    #order: course code, course name, session #, type, letter, day, time, location
    laList = []
    
    #course variables - sufixed with a 'c'
    cDbId = None
    cCode = None
    cName = None
    cCreds = None
    cPrereq = None
    
    #teacher variables - sufixed with a 't'
    tDbId = None
    tFistName = None
    tLastName = None
    
    #lecture variables - sufixed with an 'l'
    lDbId = None
    lSemester = None
    lLetter = None
    lTime = None
    lDay = None
    lLocation = None
    
    #tutorial variables - sufixed with an 'tu'
    tuDbId = None
    tuLetter = None
    tuTime = None
    tuDay = None
    tuLocation = None
    
    #laboratory variables - sufixed with an 'la'
    laDbId = None
    laLetter = None
    laTime = None
    laDay = None
    laLocation = None
    
    #variables to handle database operation
    db = None
    cursor = None
    data = None
    
    def __init__(self):
        self.initVars()
    
    def initVars(self):
        self.cDbId = 0
        self.cCode = ""
        self.cName = ""
        self.cCreds = 0
        self.cPrereq = ""
        
        self.tDbId = 0
        self.tFistName = ""
        self.tLastName = ""
        
        self.lDbId = 0
        self.lSemester = 0
        self.lLetter = ""
        self.lTime = ""
        self.lDay = ""
        self.lLocation = ""
        
        self.tuDbId = 0
        self.tuLetter = ""
        self.tuTime = ""
        self.tuDay = ""
        self.tuLocation = ""
        
        self.laDbId = 0
        self.laLetter = ""
        self.laTime = ""
        self.laDay = ""
        self.laLocation = ""
        
    def dbConnect(self):
        # Open database connection
        self.db = MySQLdb.connect("localhost", "root","root","Scheduler")
        # prepare a cursor object using cursor() method
        self.cursor = self.db.cursor()
        
    def dbClose(self):
        # disconnect from server
        self.db.close()
        
    def getData(self, cl, s):
        if self.db != None:
            for courseStr in cl:
                self.cursor.execute("SELECT * FROM Courses where code = '" + courseStr +"'")
                self.data = self.cursor.fetchall()
                for d in self.data:
                    codeTemp = d[1].split()
                    self.cDbId = d[0]
                    self.cCode = codeTemp[1]
                    self.cName = codeTemp[0]
                    self.cCreds = d[3]
                    self.cPrereq = d[4]

                self.cursor.execute("SELECT * FROM Lectures where lec_course_id = " + str(self.cDbId) + " and semester = " + s) # + " and semester = " + s
                self.data = self.cursor.fetchall()
                for c in self.data:
                    self.lDbId = c[0]
                    self.lSemester = c[3]
                    self.lLetter = c[5]
                    self.lTime = c[6]
                    self.lDay = c[7]
                    self.lLocation = c[8]
                    self.tDbId = c[1]

                    self.cursor.execute("SELECT * FROM Teachers where teacher_id = " + str(self.tDbId))
                    tData = self.cursor.fetchone()
                    self.tFirstName = tData[1]
                    self.tLastName = tData[2]

                    tempLectList = []
                    tempLectList.append(self.cName)
                    tempLectList.append(self.cCode)
                    tempLectList.append(self.lSemester)
                    tempLectList.append(self.cCreds)
                    tempLectList.append("LEC")
                    tempLectList.append(self.lLetter)
                    tempLectList.append(self.tFirstName + " " + self.tLastName)
                    tempLectList.append(self.lDay)
                    tempLectList.append(self.lTime)
                    tempLectList.append(self.lLocation)
                    tempLectList.append("")
                    tempLectList.append(self.cPrereq)
                    self.lList.append(tempLectList)

                    self.cursor.execute("SELECT * FROM Tutorials where tut_lecture_id = " + str(self.lDbId))
                    self.data = self.cursor.fetchall()
                    for q in self.data:
                        self.tuDbId = q[0]
                        self.tuLetter = q[2]
                        self.tuTime = q[3]
                        self.tuDay = q[4]
                        self.tuLocation = q[5]

                        tempTutList = []
                        tempTutList.append(self.cName)
                        tempTutList.append(self.cCode)
                        tempTutList.append(self.lSemester)
                        tempTutList.append("")
                        tempTutList.append("TUT")
                        tempTutList.append(self.lLetter + " " + self.tuLetter)
                        tempTutList.append("")
                        tempTutList.append(self.tuDay)
                        tempTutList.append(self.tuTime)
                        tempTutList.append(self.tuLocation)
                        tempTutList.append("")
                        tempTutList.append("")
                        self.tuList.append(tempTutList)

                        self.cursor.execute("SELECT * FROM Laboratories where lab_lec_id = " + str(self.lDbId) + " and lab_tut_id = " + str(self.tuDbId))
                        self.data = self.cursor.fetchall()
                        for w in self.data:
                            self.laDbId = w[0]
                            self.laLetter = w[3]
                            self.laTime = w[4]
                            self.laDay = w[5]
                            self.laLocation = w[6]

                            tempLabList = []
                            tempLabList.append(self.cName)
                            tempLabList.append(self.cCode)
                            tempLabList.append(self.lSemester)
                            tempLabList.append("")
                            tempLabList.append("LAB")
                            tempLabList.append(self.lLetter + " " + self.tuLetter + " " + self.laLetter)
                            tempLabList.append("")
                            tempLabList.append(self.laDay)
                            tempLabList.append(self.laTime)
                            tempLabList.append(self.laLocation)
                            tempLabList.append("")
                            tempLabList.append("")
                            self.laList.append(tempLabList)

                    self.cursor.execute("SELECT * FROM Laboratories where lab_lec_id = 0" + str(self.lDbId) + " and lab_tut_id = 0")
                    self.data = self.cursor.fetchall()
                    for z in self.data:
                        self.laDbId = z[0]
                        self.laLetter = z[3]
                        self.laTime = z[4]
                        self.laDay = z[5]
                        self.laLocation = z[6]

                        tempLabList = []
                        tempLabList.append(self.cName)
                        tempLabList.append(self.cCode)
                        tempLabList.append(self.lSemester)
                        tempLabList.append("")
                        tempLabList.append("LAB")
                        tempLabList.append(self.lLetter + " " + self.tuLetter + " " + self.laLetter)
                        tempLabList.append("")
                        tempLabList.append(self.laDay)
                        tempLabList.append(self.laTime)
                        tempLabList.append(self.laLocation)
                        tempLabList.append("")
                        tempLabList.append("")
                        self.laList.append(tempLabList)
        else:
            print "A connection to the database was not found!!"









#end of script
