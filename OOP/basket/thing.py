class strException(Exception):
    def __init__(self, foo):
        self.par = foo
class intException(Exception):
    def __init__(self, foo):
        self.par = foo

class Thing : 
    def __init__(self, kg, name) : 
        
        try :
            if not isinstance(kg ,int) :
                raise intException("Должно быть число")
            if not isinstance(name, str) : 
                raise strException("Должна быть строка")
        except strException as e : 
            print(e.par)
            return
        except intException as e : 
            print(e.par)
            return

        self.kg = kg
        self.name = name
    def printParams(self) : 
        print("kg", self.kg)
        print("name", self.name)

    def getParams(self) : 
        return ( self.kg, self.name )
    def getKg(self) : 
        return self.kg
    def getName(self) : 
        return self.name
