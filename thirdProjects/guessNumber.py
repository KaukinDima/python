from random import randint

print("Игра - угадай число")

comp = 0
ansT = 1
rangeNum = [15,50,100]
attempt = [3, 10, 15]
print("Выберите сложность: 1, 2, 3 (чтобы выйти нажмите q или Q)")


def guessStart() :
    while True :
        print("Введите ответ У вас есть", attempt[comp - 1], "попытки")
        try :
            ans = input() 
            print("asdasd", ans)
            if ans == "q" :
                print('Ты закончил играть')
                break
            ans = int(ans)

            if ansT == ans :
                print('Ты выйграл')
                break
            attempt[comp - 1] -= 1
            if attempt[comp - 1] == 0 :
                print('Вы проиграли')
                break
        except ValueError as e :
            print("\n ", comp, "\n")
            print('Введите число')



while True : 
    try :
        comp = input().lower() 
        if comp == "q" :
            break
        comp = int(comp)
        if comp > 3 :
            raise Exception  
        break
    except ValueError as e :
        if comp.lower() == "q" :
            break
        print('\nВведите число\n')
    except Exception as e :
        print('\n Введите сложность от 1 до 3 \n')

ansT = randint(1, rangeNum[comp - 1])

if comp != 0 and isinstance(comp, int):
    guessStart()
