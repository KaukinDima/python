from thing import Thing 

class classException(Exception):
    def __init__(self, foo):
        self.par = foo

class Basket : 
    objects = {}

    def __init__(self, kg = 10) :
        self.kg = int(kg)

    def putIntoBasket(self, object) : 

        try : 
            if not isinstance(object, Thing) : 
                raise classException("Должен быть родитель Thing")
        except classException as e : 
            print(e.par)
            return

        kg = object.kg
        name = object.name

        if kg > self.kg : 
            print('Нельзя поместить мало места')
            return

        if len(self.objects) == 0 : 
            self.objects[0] = (name, kg)
        else : 
            self.objects[ list(self.objects.keys())[-1] + 1 ] = (name, kg)
        
        self.kg -= kg
 

    def removeFromBasket(self, name) : 
        for i in self.objects : 
            tup = self.objects[i] 
            if tup[0] == name : 
                self.kg += tup[1]
                self.objects.pop(i)
                return
