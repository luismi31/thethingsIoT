import random
import decimal
import datetime as dt

class RandomIot:
    
    def __init__(self):
        self.data = None
                
    def getHourRangeTempExt(self):
        hour = dt.datetime.now().hour
        self.HourTempMax = (int(hour) + 1) * 100
        self.HourTempMin = (int(hour) - 1) * 100
    
    def getTempInt(self):
        return float(decimal.Decimal(random.randrange(2000, 2100))/100)
    
    def getTempExt(self):
        self.getHourRangeTempExt()
        return float(decimal.Decimal(random.randrange(self.HourTempMin, self.HourTempMax))/100)
    
    def getHumInt(self):
        return float(decimal.Decimal(random.randrange(5000, 5200))/100)
    
    def getHumExt(self):
        return float(decimal.Decimal(random.randrange(6300, 6500))/100)

