from thethings import ThethingsAPI

class thethings:
    
    def __init__(self,token):
        self.connector = ThethingsAPI(token)
        
    def sendData(self,name,value):
        try:
            self.connector.addVar(name, value)
            self.connector.write()
            print 'SENT DATA TO THINGS.IO'
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print message