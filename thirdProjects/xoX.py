from random import randint

'''create : 
1. field + 
2. combination of winners +
3. function which check input from somebody +
4. function which check winners +
5. create move +
6. start loop +
'''

X = "X"
O = "O"
FIRST = "a"
i = 1 
FIELD = [ i for i in range(1,10) ]

print(FIELD)

COMBINATION = [
    [1 ,2 ,3],
    [4, 5 ,6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]
]

class eWinner(Exception):
    def __init__(self, foo):
        self.par = foo
class sameValueException(Exception):
    def __init__(self, foo):
        self.par = foo

def printField() :
    for i in range( 1, len(FIELD) + 1 ) : 
        if i == 1 : 
            print("\n")
        if i % 3 == 0 :
            print("| {{", FIELD[i-1], " }} |\n") 
        else : 
            print("| {{", FIELD[i-1] , end=" }} ")

def takeInput() :
    res = input()
    
    if res != FIRST :
        raise XorO
    else : 
        return res 

def makeMove() :
    print("Компьтер делает ход\n")
    while True : 
        move = randint(1,9)
        if move in FIELD : 
            if FIRST != "O" : 
                FIELD[ move - 1 ] = "O"
            else :
                FIELD[ move - 1 ] = "X"  
            break

def checkWinner() :
    params = X + O
    arr = [ [], [] ]
    
    for i in range(0, len(params)) : 
        for k in range(1, len(FIELD) + 1 ) :
            if FIELD[ k - 1 ] == params[i] : 
                arr[i].append(k)
    print(arr, 'asdsd')

    for i in arr : 
        for k in COMBINATION :
            if len( list(set(i) & set(k)) ) == 3 : 
                if FIRST == params[0] :
                    raise eWinner('Вы победили')
                else : 
                    raise eWinner('Вы проиграли')



def game() :
    move = 1
    COUNT = 0
    COMP = 1
    
    if FIRST == 'X' : 
        COMP = 0

    while True :
        try :
            
            printField()
            
            if move ^ COMP :
                print('Выберите клетку ')  
                cell = int(input())

                if cell > 9 or cell < 1 :
                    raise ValueError
                if isinstance(FIELD[ cell - 1 ], int) : 
                    FIELD[ cell - 1 ] = FIRST
                else :    
                    raise sameValueException('Нельзя нажимать туда где занято')
                
                COMP = 1
            else :
                makeMove()
                COMP = 0
            
            COUNT += 1
            checkWinner()

            if COUNT == 9 : 
                print("Ничья")
                break
        except ValueError as e : 
            print('Вы можете ввести толко цифры')
        except eWinner as e : 
            printField()
            print(e.par)
            break
        except sameValueException as e : 
            print(e.par)

while True : 
    print('Введите как будете играть X или O (не ноль, букваа)')
    try : 
        res = input()
        if res.lower() == 'x' or res.lower() == 'o' :
            FIRST = res.upper()
            game()
            break 
        print("\n", res, "\n")
    except ValueError as e : 
        print('error')

