# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="philipblaquiere"
__date__ ="$Mar 22, 2012 12:43:59 PM$"
__name__ = "__main__"

import json

class Class:

    def __init__(self,courseCode,sessionNumber,type,name, professorName,days,startTime,endTime,roomNumber,campus,section):
        self.sessionNumber = sessionNumber
        self.courseCode = courseCode
        self.type = type #holds  LEC, TUT, or LAB as a string.
        self.name = name #holds section number, JJ, TA etc...
        self.professorName = professorName
        self.days = self.convertDays(days)
        self.startTime = startTime #"12:00"
        self.endTime = endTime
        self.roomNumber = roomNumber
        self.campus = campus
        self.section = section
        
    def convertDays(self,days):
        dayList = []
        if days == '':
            tempDays = "Z"
        else:
            tempDays = days.split("|")
        	
        for i in xrange(0,len(tempDays)):
            if(tempDays[i]=="M"):
                dayList.append(0)
            elif(tempDays[i]=="T"):
                dayList.append(1)
            elif(tempDays[i]=="W"):
                dayList.append(2)
            elif(tempDays[i]=="J"):
                dayList.append(3)
            elif(tempDays[i]=="F"):
                dayList.append(4)
            elif(tempDays[i]=="S"):
                dayList.append(5)
            elif(tempDays[i]=="D"):
                dayList.append(6)
            else:
                dayList.append(8)
                
        return dayList
    
    def set_sessionNumber(self, sessionNumber):
        self.sessionNumber = sessionNumber

    def get_sessionNumber(self):
        return self.sessionNumber

    def set_type(self, type):
        self.type = type

    def get_type(self):
        return self.type

    def set_name(self, name):
        self.section = name

    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.courseCode
    
    def get_startHour(self):
        times = self.startTime.split(":")
        if times[0][0] == '0':
            return str(times[0][1])
        
        return str(times[0])
    
    def get_endHour(self):
        times = self.endTime.split(":")
        if times[0][0] == '0':
            return str(times[0][1])
        
        return str(times[0])
    
    def get_startMins(self):
        times = self.startTime.split(":")
        return str(times[1])
    
    def get_endMins(self):
        times = self.endTime.split(":")
        return str(times[1])

    def set_professorName(self, professorName):
        self.professorName = professorName

    def get_professorName(self):
        return self.professorName;

    def set_days(self,days):
        self.days = days

    def get_days(self):
        return self.days
    
    def get_jsonDays(self):
        strDays = ""
        for i in xrange(0, len(self.days)):
            strDays += str(self.days[i])
            if (len(self.days) > (i + 1)):
                strDays += ","
        return strDays


    def set_startTime(self, startTime):
        self.startTime = startTime

    def get_startTime(self):
        return self.startTime

    def set_endTime(self,endTime):
        self.endTime = endTime

    def get_endTime(self):
        return self.endTime

    def set_roomNumber(self,roomNumber):
        self.roomNumber = roomNumber

    def get_roomNumber(self):
        return self.roomNumber

    def set_campus(self,campus):
        self.campus = campus

    def get_campus(self):
        return self.campus

    def set_section(self, sections):
        self.section = sections

    def get_section(self):
        return self.section

    def hasTutorial(self):
        if(len(self.section)<1):
            return False

        elif(self.section[0].type=="TUT"):
                return True
        else:
            return False

    def __str__(self):
        return ("\nSession: "+str(self.sessionNumber)+"\n"+
                "Type: "+str(self.type)+"\n"+
                "Name: "+str(self.name)+"\n"+
                "Professor Name:"+str(self.professorName)+"\n"+
                "Days:"+str(self.days[0])+"\n"+
                "Start Time:"+str(self.startTime)+"\n"+
                "End Time:"+str(self.endTime)+"\n"+
                "Room Number:"+str(self.roomNumber)+"\n"+
                "Campus:"+str(self.campus)+"\n")

    def addClass(self, section1):
        self.section.append(section1)


    def getSections(self,position):
	return self.section[position]
