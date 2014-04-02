# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="philipblaquiere"
__date__ ="$Apr 1, 2012 11:09:18 AM$"


from Class import *
from Course import *


class CourseContainer:

    def __init__(self):

        self.courseMap = {"ENGR" : [],
        "COMP" : [],"SOEN" : [],
        "ENCS" : [],"ELEC" : [],
        "BIOL" : [],"CHEM" : [],
        "GEOL" : [],"PHYS" : [],
        "MATH" : [],"ACCO" : [],
        "BTM"  : [],"COMM" : [],
        "DESC" : [],"ECON" : [],
        "SCOM" : [], "MECH" : [],
        }
    def getCourseContainer(self):
        return self.courseMap
    
    def getCourse(self,courseName):
        #courseName contains for example "ENGR 371"
        #this function will return a course object

        courseArray = courseName.split(" ",2)
        
        courseList = self.courseMap.get(courseArray[0])
        for i in xrange(0,len(courseList)):
            courseNumber = courseList[i].getCourseName().split(" ",2)
            if(courseNumber[1]==courseArray[1]):
                return courseList[i]

    
    def convertTime(self,time):
        #Returns an array containing start time [0] and end time [1] of a class

         newTime = time.split("|", 2)
         return newTime
    def toString(self):
        
        engrList = self.courseMap.get("ENCS")
        for i in xrange(0,len(engrList)):
            print i
            print str(engrList[i])
            
    def addLectureList(self,lectures):
        #main function being called by the database.
        for i in xrange(0, len(lectures)):
            lecturelist = lectures[i]
            self.addClass(lecturelist[0],lecturelist[1],lecturelist[2],lecturelist[3],lecturelist[4],lecturelist[5],lecturelist[6],lecturelist[7],lecturelist[8],lecturelist[9],lecturelist[10],lecturelist[11])

    def addTutorialList(self,tutorials):
        #main function being called by the database.
        for i in xrange(0, len(tutorials)):
            tutorialList = tutorials[i]
            self.addClass(tutorialList[0],tutorialList[1],tutorialList[2],tutorialList[3],tutorialList[4],tutorialList[5],tutorialList[6],tutorialList[7],tutorialList[8],tutorialList[9],tutorialList[10],tutorialList[11])

    def addLaboratoryList(self,lectures):
        #main function being called by the database.
        for i in xrange(0, len(lectures)):
            lecturelist = lectures[i]
            self.addClass(lecturelist[0],lecturelist[1],lecturelist[2],lecturelist[3],lecturelist[4],lecturelist[5],lecturelist[6],lecturelist[7],lecturelist[8],lecturelist[9],lecturelist[10],lecturelist[11])


    def addClass(self,courseName,courseNumber,sessionNumber,credits,type,section, professorName,days,lecTime,roomNumber,campus,prereqs):
        #change parameters courseName & courseNumber to courseCode (basically fusing them together)
        #Type contains LEC,TUT,LAB/

        #incomplete

        classTime = self.convertTime(lecTime)
        name = str(courseName)+" "+str(courseNumber) #Ex. Concatenates ENGR + " " + 371 .
        newClass = Class(name,sessionNumber,type,section, professorName,days,classTime[0],classTime[1],roomNumber,campus,[])
        
        classNameArray = newClass.get_name().split(" ")
        courseList = self.courseMap.get(courseName)
       
        if(len(courseList)==0):
            self.courseMap.get(courseName).append(Course("Course Code",name,credits,prereqs,[newClass]))
            
        else:
            for i in xrange(0,len(courseList)):
                if(name == courseList[i].getCourseName()):
                    #Hit found in course list ("ENGR 371" == "ENGR 371"), therefore course exists.
                    #Proceed to appropriate tut or lab, or append new lecture to course
                    if(newClass.get_type() == "LEC"):
                        courseList[i].addClass(newClass)


                    if(newClass.get_type() == "TUT"):
                        #Will appropriate the tutorial to the correct lecture
                        #Compare the first letter of the lecture section to the first of the tut
                        # If they are the same, tutorial is appended to the lecture
                        lectureList = courseList[i].get_lectures()
                        for j in xrange(0,len(lectureList)):
                            if(lectureList[j].get_name()==classNameArray[0]):
                                lectureList[j].addClass(newClass)
                    if(newClass.get_type() == "LAB"):
                        lectureList = courseList[i].get_lectures()
                        for j in xrange(0,len(lectureList)):
                            lectureName = lectureList[j].get_name()
                            if(lectureName == classNameArray[0]):
                                if(lectureList[j].hasTutorial()==False):
                                    #Lecture doesn't have any tutorials, therefore lab is added
                                    #This situation doesn't happen often
                                    lectureList[j].addClass(newClass)
                                else:
                                    tutList = lectureList[j].get_section()
                                    for k in xrange(0,len(tutList)):
                                        tutName = tutList[k].get_name().split(" ")
                                        if(tutName[1] == classNameArray[1]):
                                            tutList[k].addClass(newClass)

                elif(i==(len(courseList)-1)):
                    #create Course and add it to map containing newClass
                    newCourse = Course("Course Code",name,credits,prereqs,[newClass])
                    self.courseMap.get(courseName).append(newCourse)
                            



