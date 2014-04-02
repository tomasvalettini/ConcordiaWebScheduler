import sys
from GetDbData import *
from CourseContainer import *
from ScheduleContainer import *

cList = []
cInt = len(sys.argv) - 2
pos = 2


while True:
	cStr = sys.argv[pos] + " "
	pos += 1
	cStr += sys.argv[pos]
	cList.append(cStr)
	pos += 1
	if pos > cInt:
		break

dd = GetDbData()
dd.dbConnect()
dd.getData(cList, sys.argv[1])
dd.dbClose()

cc = CourseContainer()
cc.addLectureList(dd.lList)
cc.addTutorialList(dd.tuList)
cc.addLaboratoryList(dd.laList)

sc = ScheduleContainer(cList, cc)
sc.generateSchedules()
#print "ball sack"
print sc.toJSON()









# end of script
