import sys
import datetime
from time import sleep
from randomIot import RandomIot
from timer import RepeatedTimer
from dbClass import Database
from cloudConnector import thethings

def insertData(db,value,name,type): 
    query = "INSERT INTO IOTDB.data (value, name, timestamp, type) VALUES (" + "'" + value + "','" + name + "','" + str(datetime.datetime.now()) + "','" + type + "');"
    db.insert(query)

def setTempInt(random, db, thethings):
    data = str(random.getTempInt())
    print 'STORED: ' + data
    insertData(db,data,'internal','temp')
    print 'SENT DATA TO THINGS.IO'
    thethings.sendData('temperature',data)
    
def setTempExt(random, db, thethings):
    data = str(random.getTempExt())
    print 'STORED: ' + data
    insertData(db,data,'external','temp')
    print 'SENT DATA TO THINGS.IO'
    thethings.sendData('temperature',data)
    
def setHumInt(random, db, thethings):
    data = str(random.getHumInt())
    print 'STORED: ' + data
    insertData(db,data,'internal','hum')
    print 'SENT DATA TO THINGS.IO'
    thethings.sendData('humidity',data)
    
def setHumExt(random, db, thethings):
    data = str(random.getHumExt())
    print 'STORED: ' + data
    insertData(db,data,'external','hum')
    print 'SENT DATA TO THINGS.IO'
    thethings.sendData('humidity',data)

db = Database()
random = RandomIot()
thethings = thethings("19sbFlk2ZtBRc7fNwagHZ-MgyrgQjaZP1gI9UbS5Aso")
print "starting..."
tempInt = RepeatedTimer(10, setTempInt, random, db, thethings)
tempExt = RepeatedTimer(10, setTempExt, random, db, thethings)
humInt = RepeatedTimer(10, setHumInt, random, db, thethings)
humExt = RepeatedTimer(10, setHumExt, random, db, thethings)


'''
try:
    sleep(5) # your long-running job goes here...
finally:
    rt.stop() # better in a try/finally block to make sure the program ends!
'''




