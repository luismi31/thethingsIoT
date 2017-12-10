import sys
from time import sleep
from randomIot import RandomIot
from timer import RepeatedTimer
from dbClass import Database
from actionTrigger import action
from cloudConnector import thethings

def setTempInt(random, db, thethings):
    data = action().lowTemp(random.getTempInt,21)
    db.insertData(db,data,'internal','temp')
    thethings.sendData('temperatureInt',data)
    
def setTempExt(random, db, thethings):
    data = action().lowTemp(random.getTempExt,19)
    db.insertData(db,data,'external','temp')
    thethings.sendData('temperatureExt',data)
    
def setHumInt(random, db, thethings):
    data = str(random.getHumInt())
    db.insertData(db,data,'internal','hum')
    thethings.sendData('humidityInt',data)
    
def setHumExt(random, db, thethings):
    data = str(random.getHumExt())
    db.insertData(db,data,'external','hum')
    thethings.sendData('humidityExt',data)

db = Database()
random = RandomIot()
thethings = thethings("19sbFlk2ZtBRc7fNwagHZ-MgyrgQjaZP1gI9UbS5Aso")
print "starting..."
rt = RepeatedTimer(60, setTempInt, setTempExt, setHumInt, setHumExt, random, db, thethings)

