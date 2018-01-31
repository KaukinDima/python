class Shape :
    
    def __init__(self, *args) : 
        length = len(args)

        if length == 1 : 
            square(args)
            self.figure = square
            return
        if length == 2 : 
            rectangle(args)
            self.figure = rectangle
            return
        if length == 3 : 
            triangle(args)
            self.figure = triangle
            return

        print("Возмонжо длина только от 1 до 4")

    def printShapeParams(self, args, length) : 
        print("Фигура -", self.figure)
        print("Периметр -", self.params[0])
        print("Площадь -", self.params[1])
        

    def square(self, args) : 
        self.params( args[0] * 4, args[0]**2 )        

    def rectangle(self) : 
        a = args[0]
        b = args[1]
        self.params( (a+b) * 2 , a * b )        

    def triangle(self, args) :
        a = args[0]
        b = args[1]
        c = args[2]
        self.params( (a+b+c), a*b*c ) 
        