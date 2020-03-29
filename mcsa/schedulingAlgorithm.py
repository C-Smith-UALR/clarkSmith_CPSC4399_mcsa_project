#This file will contain the functions necessary to create a month's worth of shifts
#for a given physician pool

from .models import McsaShift, McsaPhysician, userMonthYear
from datetime import datetime, date
from calendar import monthrange
from random import seed
from random import randint


def getDocList():
    physiciansQuerySet = McsaPhysician.objects.all()
    docs = physiciansQuerySet[::1]
    docAndShift=[]
    for doc in docs:
        temp=[doc, 0, 0]
        docAndShift.append(temp)

    return docAndShift

def isAlreadyCovered(day):
    try:
        shift=McsaShift.objects.get(start_time__day=day)
    except McsaShift.DoesNotExist:
        shift=None
    if shift:
        return True
    else:
        return False

def getWeekDayDoc(docs):
    while True:
        # loop until you find a doc that's not already maxed on calls
        randomInt = randint(0, len(docs)-1)
        doc = docs[randomInt]
        print(doc)
        if doc[1] < doc[0].maxShiftLoad:
            doc[1]+=1
            return doc[0]

def getWeekendDoc(docs):
    while True:
        # loop until you find a doc that's not already assigned a weekend call
        randomInt = randint(0, len(docs)-1)
        doc = docs[randomInt]
        if doc[2] < 1:
            doc[2]+=1
            return doc[0]

def getWeekendShifts(month, year, dayOfMonth, doc):
    lastDay=monthrange(year, month)[1]
    print(dayOfMonth)
    print(lastDay)
    shiftList=[]
    saturdayDay=dayOfMonth+1
    sundayDay=dayOfMonth+2
    startTimeFri=datetime(year, month, dayOfMonth, 17, 0)
    endTimeFri=datetime(year, month, dayOfMonth, 23, 59)

    fridayShift=McsaShift(start_time=startTimeFri, end_time=endTimeFri, title='LRIPC', physicianOnCall=doc)
    shiftList.append(fridayShift)
    if dayOfMonth != lastDay:
        startTimeSat = datetime(year, month, saturdayDay, 1, 0)
        endTimeSat = datetime(year, month, saturdayDay, 23, 59)
        satShift = McsaShift(start_time=startTimeSat, end_time=endTimeSat, title='LRIPC', physicianOnCall=doc)
        shiftList.append(satShift)
        if saturdayDay !=lastDay:
            startTimeSun = datetime(year, month, sundayDay, 1, 0)
            endTimeSun = datetime(year, month, sundayDay, 23, 59)
            sunShift = McsaShift(start_time=startTimeSun, end_time=endTimeSun, title='LRIPC', physicianOnCall=doc)
            shiftList.append(sunShift)
    return shiftList

def main(month, year):
    docs=getDocList()
    #print(docs)
    randomSeed=randint(0,1000)
    seed(randomSeed)
    daysInMonth=monthrange(year,month)[1]  #get the number of days in user-selected month
    for day in range(daysInMonth):
        dayOfMonth=day+1
        print(dayOfMonth)
        if not isAlreadyCovered(dayOfMonth):
            mcsaDate=date(year,month,dayOfMonth)
            print(mcsaDate)
            mcsaDayOfWeek=mcsaDate.weekday()
            print(mcsaDayOfWeek)
            if mcsaDayOfWeek in range(0,4):
                doc=getWeekDayDoc(docs)
                startTime=datetime(year, month, dayOfMonth, 17, 0)
                endTime=datetime(year, month, dayOfMonth, 23, 59)
                tempShift = McsaShift(start_time=startTime, end_time=endTime, title='LRIPC', physicianOnCall=doc)
                tempShift.save()
            else:
                doc=getWeekendDoc(docs)
                weekendShifts=getWeekendShifts(month, year, dayOfMonth, doc)
                for shift in weekendShifts:
                    shift.save()





    return True










