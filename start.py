import sys
from time import sleep
from randomIot import RandomIot
from timer import RepeatedTimer
from dbClass import Database
from cloudConnector import thethings

def setTempInt(random, db, thethings):
    data = str(random.getTempInt())
    print 'STORED: ' + data
    db.insertData(db,data,'internal','temp')
    print 'SENT DATA TO THINGS.IO'
    thethings.sendData('temperatureInt',data)
    
def setTempExt(random, db, thethings):
    data = str(random.getTempExt())
    print 'STORED: ' + data
    db.insertData(db,data,'external','temp')
    print 'SENT DATA TO THINGS.IO'
    thethings.sendData('temperatureExt',data)
    
def setHumInt(random, db, thethings):
    data = str(random.getHumInt())
    print 'STORED: ' + data
    db.insertData(db,data,'internal','hum')
    print 'SENT DATA TO THINGS.IO'
    thethings.sendData('humidityInt',data)
    
def setHumExt(random, db, thethings):
    data = str(random.getHumExt())
    print 'STORED: ' + data
    db.insertData(db,data,'external','hum')
    print 'SENT DATA TO THINGS.IO'
    thethings.sendData('humidityExt',data)

db = Database()
random = RandomIot()
thethings = thethings("19sbFlk2ZtBRc7fNwagHZ-MgyrgQjaZP1gI9UbS5Aso")
print "starting..."
rt = RepeatedTimer(10, setTempInt, setTempExt, setHumInt, setHumExt, random, db, thethings)



'''
try:
    sleep(5) # your long-running job goes here...
finally:
    rt.stop() # better in a try/finally block to make sure the program ends!
'''




