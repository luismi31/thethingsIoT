import random
import decimal

class RandomIot:
    
    def __init__(self):
        self.data = None
        
    def getTempInt(self):
        return float(decimal.Decimal(random.randrange(2000, 2300))/100)
    