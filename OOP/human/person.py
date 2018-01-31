from friend import Friend

class Person(Friend) : 
    people = {}

    def know(self, object) : 
        
        if not isinstance(object, Friend) : 
            print('err')
            return 

        self.people[object.uniq] = object
    
    def isKnown(self, uniq ) :

        if uniq in list( self.people.keys() ) : 
            print("Да знаю")
            return "Да знаю"
        else : 
            print("Не знаю")
        
