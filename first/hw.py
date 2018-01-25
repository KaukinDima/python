# Программа выводить в консоль текст загадки и ждать ввода пользователя
'''quantity = 0
answer = input('Елка - цвет?')
if 'зелёный' == answer.lower() or 'зелeный' == answer.lower() :
    print('Молодец')
    quantity += 1 
else : 
    print('Answer is wrong')
    print('\nТвой ' + answer + ' Правильный ответ - ' + answer.lower())

answer = input('1 + 1 ?')
if answer == '2' :
    print('Молодец')
    quantity += 1 
else : 
    print('Answer is wrong')
    print('\nТвой ' + answer + ' Правильный ответ - ' + answer.lower())

print( 'Количество правильных ответов :' + str(qauntity) )'''

# Напишите программу, которая считает площадь прямоугольника,
#  спрашивая у пользователя длину двух сторон

'''def rectangle() :
    a = input('length') 
    b = input('width')
    res = (int(a) + int(b)) * 2
    print('Площадь прямоугольника' + str(res) )

rectangle()'''

# Напишите программу, которая спрашивает у пользователя
#  два числа и знак: "+" или "-". В зависимости от знака выводит их сумму или разницу

'''def plusOrMinus() : 
    a = input('first\n') 
    b = input('second\n')
    sign = input('plusOrMinus\n')
    res = 'err'
    if sign == '+' :
        res = int(a) + int(b)
    elif sign == '-' :
        res = int(a) - int(b)
    print('res', res)

plusOrMinus()'''
# Напишите программу, которая находит все 
# простые числа между 0 и пользовательским числом

'''def simpleNumber() :
    res = []
    a = int(input('Number'))
    for i in range(2, a + 1) :
        index = 0    
        print(i, 'паа')
        for k in range(2 , i) : 
            if i % k == 0 :
                index += 1
            if index == 1 : 
                break
            if (i-1) == k :
                res.append(i)
    print(res)'''

# simpleNumber()

# Напишите программу, которая выводит все 
# кратные 5 числа между двумя пользовательскими числами     

'''def lessSimpleNumber() :
    res = []
    a = int(input('Number'))
    b = int(input('second Number'))
    for i in range(a, b + 1) :
        if i % 5 == 0 : 
            res.append(i)
    print(res)'''

#  'Заполните пробел: Для преобразования числа в строку выполните "___(100)"':'str',
#  'Для преобразования строки в число выполните "___(100)"':'int',
#  'Какой тип данных будет у переменной f, если f = 12 + 2.5?':'float',
#  'Как в Python обозначается истина?':'True', 
#  'Цикл с пред-условием':'While',
#  'Чему равна переменная b, если b = bool(51)?':'True',
#  'Чему равно утверждение: (True or False) and True?': 'True',
#  'Чему равно утверждение 0 == None?': 'False',
#  'Что вернет выражение "Hello"[1]?':'e',
#  'Что вернет выражение len("Hello world!")':'12'
