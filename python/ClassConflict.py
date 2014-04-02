#
#  ClassConflict.py
#  
#
#  Created by Philip on 3/23/12.
#  Copyright (c) 2012 __FlyingMongoose__. All rights reserved.
#

class ClassConflict:

    def __init__(self):
        self.conflictReport = None #holds a list of strings with conflict info
        self.conflictCounter = 0 #keeps track of how many conflicts there are
        self.isConflict = None #true if a conflict exists, false otherwise
        
		
    def convertToIntegerMinutes(self, timeString):
        # Takes in a string time value "XX:YY" and multiplies XX (hours) by 60
        # and adds it to YY to give total number of minutes.

        time = timeString.split(":", 2)
        hours = int(time[0])
        minutes = int(time[1])
        return ((hours * 60) + minutes)

    def numberOfConflicts(self, primaryClass, otherClass):
        # Method checks for time conflicts between NON-SPECIFIC primaryClass and otherClass
        # Returns the number of found conflicts between two classes
        # Functional as of 26/03/12 4:02 PM

        numberOfConflicts = 0
 
        primaryStartTime = self.convertToIntegerMinutes(primaryClass.get_startTime())
        primaryEndTime = self.convertToIntegerMinutes(primaryClass.get_endTime())
        otherStartTime = self.convertToIntegerMinutes(otherClass.get_startTime())
        otherEndTime = self.convertToIntegerMinutes(otherClass.get_endTime())

        primaryDays = primaryClass.get_days()
        otherDays = otherClass.get_days()

        for i in xrange(0, len(primaryDays)):
            for j in xrange(0, len(otherDays)):
                if(otherDays[j] == primaryDays[i]):
                    if((otherStartTime >= primaryStartTime) & (otherStartTime <= primaryEndTime)):
                        numberOfConflicts += 1
                    elif((primaryStartTime <= otherEndTime) & (otherEndTime <= primaryEndTime)):
                        numberOfConflicts += 1
        return numberOfConflicts   

    def testConflict(self, primarySpecificClass, otherSpecificClass):
        # returns false if one of otherClass' lectures, tutorials and labs interferes
        # with primaryClass' lectures, tutorials or labs. Represents main funciton that
        # will be used to determine conflicts
        # Working as of 28/03/12
        numOfConflicts = 0
        primarySelection = primarySpecificClass.get_selection()
        otherSelection = otherSpecificClass.get_selection()
        primarySelectionLength = len(primarySelection)
        otherSelectionLength = len(otherSelection)
        for i in xrange(0, primarySelectionLength):
            for j in xrange(0, otherSelectionLength):
                numOfConflicts += self.numberOfConflicts(primarySelection[i], otherSelection[j])
        return numOfConflicts
