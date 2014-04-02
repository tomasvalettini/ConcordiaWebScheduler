__author__="philipblaquiere"
__date__ ="$Mar 22, 2012 3:37:17 PM$"
import Class
from Class import *

import json

class SpecificClass:

    def __init__(self, _selection):
        #_selection contains a list of classes
        self.selection = _selection
        self.selectionSize = len(_selection)
        self.numLectures = self.getNumberOf("LEC")
        self.numTutorials = self.getNumberOf("TUT")
        self.numLaboratories = self.getNumberOf("LAB")
        
    
    def get_selection(self):
        return self.selection

    def addSelection(self,anySingleClass):
        # Adds a single class (LEC,TUT,LAB) to the SpecificClass selection object
        # Therefore SpecificClass is instantiated with a lecture, and classes are
        # Then added to the list.
        selection.append(anySingleClass)
        self.numLectures = self.getNumberOf("LEC")
        self.numTutorials = self.getNumberOf("TUT")
        self.numLaboratories = self.getNumberOf("LAB")
        return
    
    def getNumberOf(self, classType):
        count = 0
        for i in xrange(0,self.selectionSize):
            if(self.selection[i].get_type() == classType):
                count+=1
        return count

    def getLecture(self):
        return self.selection[0]

    def getTutorial(self):
        if(numTutorials>0):
            return self.selection[1]

    def getLab(self):
        if(numLaboratories > 0):
            return self.selection[2]

    def __str__(self):
        string = ""
        if(len(self.selection)>0):
            for i in xrange(0,len(self.selection)):
                string+= str(self.selection[i])

                """("\nSession: "+str(self.selection[i].sessionNumber)+"\n"+
                    "Type: "+str(self.selection[i].type)+"\n"+
                    "Name: "+str(self.selection[i].name)+"\n"+
                    "Professor Name:"+str(self.selection[i].professorName)+"\n"+
                    "Days:"+str(self.selection[i].days[0])+"\n"+
                    "Start Time:"+str(self.selection[i].startTime)+"\n"+
                    "End Time:"+str(self.selection[i].endTime)+"\n"+
                    "Room Number:"+str(self.selection[i].roomNumber)+"\n"+
                    "Campus:"+str(self.selection[i].campus)+"\n")"""
        return string

    def toJSON(self):
        jsonStr = ""
        for i in xrange(0, len(self.selection)):
            daysOfClass = self.selection[i].get_jsonDays()
            daysArr = daysOfClass.split(",")
            for x in xrange(0, len(daysArr)):
                ls = {'start_hour' : self.selection[i].get_startHour(), 'end_hour' : self.selection[i].get_endHour(), 'start_minutes' : self.selection[i].get_startMins(), 'end_minutes' : self.selection[i].get_endMins(), 'date' : daysArr[x], 'name' : self.selection[i].get_code(), 'type' : self.selection[i].get_type(), 'section' : self.selection[i].get_name()}
                jsonStr += json.dumps(ls)
                if (i != len(self.selection) - 1):
                    jsonStr += ','
        return jsonStr


    
