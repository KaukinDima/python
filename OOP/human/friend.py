from functions import check

class Friend : 
    
    def __init__(self, uniq, age, name) : 
    
        checkParam = [ check( age , False ), check( uniq, True ), check( name, True ) ]
        if True not in checkParam : 
            print('err')
            return

        self.uniq = uniq
        self.age = age 
        self.name = name

