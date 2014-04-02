import copy
import Class
import Schedule 
import ClassConflict
import SpecificClass
from SpecificClass import *
from ClassConflict import *
from Schedule import *
from Class import *

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="philipblaquiere"
__date__ ="$Mar 22, 2012 1:35:29 PM$"

class Course:

    def __init__(self,courseCode,name,credits,preReqs,lectures):
        self.courseCode = courseCode
        self.name = name # eg. "ENGR 371"
        self.credits = credits
        self.preReqs = preReqs
        self.lectures = lectures

    def get_lectures(self):
        return self.lectures
    def addClass(self,lecture):
        self.lectures.append(lecture)

    def generateAllSpecificClasses(self):
        # Returns a list [] containing all specific classes possible
        # Within the course.
        # Working as of 12:35PM 29/03/12
        specificClassList = []

        for i in xrange(0,len(self.lectures)):
            tempLecture = self.lectures[i]
            classList = []
            classList.append(tempLecture)
            tutorialList = tempLecture.get_section()
            if(len(tutorialList) != 0):
                for j in xrange(0,len(tutorialList)):
                    classList1 = []
                    classList1.append(self.lectures[i])
                    tempTutorial = tutorialList[j]
                    classList1.append(tempTutorial)
                    tempLabList = tempTutorial.get_section()
                    if(len(tempLabList) != 0):
                        for k in xrange(0,len(tempLabList)):
                            classList2 = []
                            classList2.append(self.lectures[i])
                            classList2.append(tutorialList[j])
                            classList2.append(tempLabList[k])
                            specificClassList.append(SpecificClass(classList2))
                    else:
                        specificClassList.append(SpecificClass(classList1))
            else:
                # If lecture has no tutorials...
                specificClassList.append(SpecificClass(classList))
        

        return specificClassList
	
    def getCourseName(self):
	return self.name

    def get_tutorials(self,position):
        specificClass = self.lectures[position]
        return specificClass.get_section()
    def __str__(self):
        string = ""
        for i in xrange(0,len(self.lectures)):
            string+="New Lecture #"+str(i)+": \n"+str(self.lectures[i])
            tutList = self.lectures[i].get_section()
            if(len(tutList)>0):
                for j in xrange(0,len(tutList)):
                    string+=str(tutList[j])
                    labList = tutList[j].get_section()
                    if(len(labList)>0):
                        for k in xrange(0,len(labList)):
                            string+=str(labList[k])
        return string
"""
days = [1]
days1 = [1,2]
days2 = [2,3]


lab1 = Class(2,"LAB","JK","Philip Blaquiere",days,"12:00","13:30","S-2.222","LOY",None)
lab2 = Class(3,"LAB","JM","Philip Blaquiere",days2,"12:00","13:00","S-3.33","SWG",None)

labMap = [lab1,lab2]

tutorial1 = Class(2,"TUT","JK","Philip Blaquiere",[3],"12:15","13:30","S-2.222","LOY",[lab1])
tutorial2 = Class(3,"TUT","JM","Philip Blaquiere",[1,2],"13:30","14:30","S-3.33","SWG",None)
tutorial3 = Class(2,"TUT","JK","Philip Blaquiere",[3],"12:15","13:30","S-2.222","LOY",[lab2])

tutorialMap = [tutorial1,tutorial2]

class1 = Class(2,"LEC","JJ","Philip Blaquiere",[4],"9:00","10:15","S-2.222","LOY",[tutorial1])
class2 = Class(3,"LEC","GG","Philip Blaquiere",[5],"12:00","13:00","S-3.33","SWG",[tutorial2])
class3 = Class(3,"LEC","GG","Philip Blaquiere",[5],"12:00","13:00","S-3.33","SWG",None)
class4 = Class(2,"LEC","JJ","Philip Blaquiere",[4],"9:00","10:15","S-2.222","LOY",[tutorial3])

lectureMap = [class1,class2,class3,class4]

course = Course("1234","ENGR 331", "3","No Prereqs",lectureMap)


sequence1 = [class1,tutorial1,lab1]
sequence2 = [class2,tutorial2,lab2]

specificClass1 = SpecificClass(sequence1)
specificClass2 = SpecificClass(sequence2)

conflictObject = ClassConflict()
print "Checking Conflicts"
numConflicts = conflictObject.testConflict(specificClass1,specificClass2)
print "\n\nNumber of Conflicts: "+str(numConflicts)+"\n"

specificClassList = course.generateAllSpecificClasses()
for i in xrange(0,len(specificClassList)):
    print "Specific Class #"+str(i)+"\n"
    print specificClassList[i]
    print "\n"

"""

