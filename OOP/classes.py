
class Car:
    _c = 234
    __t = 123


c = Car()
print(c, type(c))

print("protected _c  ", c._c)
try : 
    print(c.__t)
except NameError as e: 
    print("_tt is PRIVATE")

class Room:
    number = 'Room 34'
    floor = 4


r = Room()
r1 = Room()
print(r.number, r1.number)
print(r.floor, r1.floor)

r.number = 12
r.floor = '5 floor'
print(r.number, r1.number)
print(r.floor, r1.floor)



class Car:
    speed = 0

    def accelerate(self):
        self.speed = self.speed + 3

    def accelerate_to(self, speed_delta):
        self.speed = self.speed + speed_delta

    def stop(self):
        self.speed = self.speed - 3

def foo():
    pass


class Door:

    def open(self):  
        print('self is', self)
        print('Door is opened!')
        self.opened = True   


d = Door()
d.open()

d1 = Door()
d1.open()



class Terminal:
    def hello(self, user_name):
        print('self is the object itself', self)
        print('Hello,', user_name)


t = Terminal()
t.hello('Nikita')
t.hello('Vova')


class Window:
    is_opened = False

    def open(self):
        self.is_opened = True
        print('Window is now', self.is_opened)

    def close(self):
        self.is_opened = False
        print('Window is now', self.is_opened)


w = Window()
w1 = Window()

print('Initial state', w.is_opened, w1.is_opened)

w.open()
print('New state', w.is_opened, w1.is_opened)

w.close()
print('New state', w.is_opened, w1.is_opened)
