
class action:
    
    def lowTemp(self,callback,minimum):
        data = callback()
        if data < minimum:
            '''
            IMPLEMENT ACTIONS TO INTERACT WITH OTHER DEVICES/TRIGGER CLOUD/GPIO
            '''
            print "WARNING "+ str(callback.__name__) + ": Minimum temp defined is: " + str(minimum) + ", actual: " + str(data)
        return str(data)
        