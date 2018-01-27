from random import randint, sample

class QException(Exception):
    def __init__(self, foo):
        self.par = foo
class NumException(Exception):
    def __init__(self, foo):
        self.par = foo
class lenException(Exception):
    def __init__(self, foo):
        self.par = foo
class strException(Exception):
    def __init__(self, foo):
        self.par = foo

def takeInput() :
    ans = input()
    
    if ans == 'q' :
        raise QException('q')
    return ans

WORD = [ i for i in "AMAZING" ]

emptyArr = sample(range(0, len(WORD)), 3)
LENGTH  = len(WORD)
show = [ " XXX " ] * LENGTH
attempt = 3
for i in emptyArr :
    show[i] = " " + WORD[i] + " " 

print('\n', emptyArr, '\n')
print('Игра в виселицу - чтобы выйти нажмите q') 

while True : 
    
    print("\n", "".join(show), "\n ")
    print('Постарайтесь угадать чтобы выйграть')

    try : 
        print()
        print('Введите какую букву')
        num = int(takeInput())
        print('Введите букву')
        ans = takeInput()
        if len(ans) > 1 : 
            raise lenException

        if WORD[num - 1].lower() == ans.lower() and show[num - 1].lower() != ans.lower(): 
            show[num - 1] = ans.upper()
        else : 
            attempt -= 1
            if attempt == 0 : 
                break
            print('Вы ошиблись \n')

    except QException as e: 
        print(  )
        break
    except ValueError as e: 
        print( e )
    except lenException as e: 
        print( 'Введите одну букву' )
    except QException as e: 
        print( 'Ведите число' )
        break
