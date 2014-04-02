#
#  Schedule.py
#  
#
#  Created by Philip on 3/22/12.
#  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
#



class Schedule:
	
    def __init__(self,selectedClasses):
        self.selectedClasses = selectedClasses
        self.constraints = []
        self.numberOfClasses = len(selectedClasses)

    def get_constraints(self):
        return self.constraints
		
    def get_selectedClasses(self):
        return self.selectedClasses
		
    def toJSON(self):
        strJSON = '{ "course": ['
        for i in xrange(0, len(self.selectedClasses)):
            strJSON += self.selectedClasses[i].toJSON()
            if (i != len(self.selectedClasses) - 1):
                strJSON += ','
        strJSON += ']'
        strJSON += '}'
        return strJSON
