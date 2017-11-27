import random
import decimal

class RandomIot:
    
    def __init__(self):
        self.data = None
        
    def getTempInt(self):
        return float(decimal.Decimal(random.randrange(2000, 2300))/100)
    
    def getTempExt(self):
        return float(decimal.Decimal(random.randrange(1400, 1600))/100)
    
    def getHumInt(self):
        return float(decimal.Decimal(random.randrange(4000, 5000))/100)
    
    def getHumExt(self):
        return float(decimal.Decimal(random.randrange(6000, 6500))/100)