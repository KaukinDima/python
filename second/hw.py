# Создать лист из 6 любых чисел. Отсортировать его по возрастанию
'''sList = [ 1, 4, 6, 0, 15, 3 ]
sortByPython = sorted(sList) # O(n log n)
print(sList)
# O(6*log(6)) = 15.5
i = 0
k = 0
def bubbleSort( arr ) : # O(N^2)
    for i in range(0, len(arr)) :
        for k in range(0, len(arr)) :
            if arr[i] < arr[k] :
                hold = arr[i]
                arr[i] = arr[k]
                arr[k] = hold
    return arr
# O(6^2) = 36'''

'''ab = bubbleSort(sList)

sList.sort()
print(sList)'''

# Создать словарь из 5 пар: int -> str, 
# например {6: '6'}, вывести его в консоль попарно

''' newDicts = {
    1 : 'first',
    2 : 'second',
    3 : 'third',
    4 : 'fourth',
    5 : 'fifth',
    6 : 'sixth'
}

for k in newDicts : 
    print('key', k, 'content', newDicts[k]) '''

# Создать лист из 3 слов: ['Earth', 'Russia', 'Moscow'], 
# соеденить все слова в единую строку,
# чтобы получилось: 'Earth -> Russia -> Moscow'

'''arr2 = ['Earth', 'Russia', 'Moscow']
arr = ['Earth', 'Russia', 'Moscow']
i = 0
res = ''
for i in range(0, len(arr)) : 
    if i == len(arr) - 1  : 
        res += arr[i]
    else :
        res += arr[i] + ' -> '
print(arr)
print(" -> ".join(arr2))'''


# Взять строку '/bin:/usr/bin:/usr/local/bin' и разбить ее в список по символу ':'

'''
string = '/bin:/usr/bin:/usr/local/bin'
print( string.split(':') )  '''


# Пройти по всем числам от 1 до 100, 
# написать в консоль, какие из них 
# делятся на 7, а какие - нет
'''i = 0

for i in range(0, 100) : 
    answer = str(i) + ' - делиться на 7' if i % 7 == 0 else str(i) + ' - не делиться на 7' # print(answer)
print([i for i in range(1,100) if i%7 == 0])'''
# Создать матрицу любых чисел 3 на 4, 
# сначала вывести все строки, потом все столбцы

'''m = [
    [2, 25, 8.9],
    [4, 19, 6],
    [4, 8, 0],
    [10, 11, 136],
]

def printRow( arr, cr ) :
    i = 0 
    k = 0 
    for i in range(0, len(arr) ) : 
        for k in range( 0, len(arr[i]) ) :
            print( '%5s' % arr[i][k], ' ', end='' )
        print(cr, i + 1)

def matrix( arr ) :
    printRow(arr, 'Строки')
    i = 0
    k = 0
    j = 0
    while i < ( len(arr) * len(arr[0])) : 
        if k == (len(arr)) : 
            k = 0
            j += 1
            print('\n')
            print( '%5s' % 'Столбец', j+1, end = '')
        if i == 0 : 
            print( '%5s' % 'Столбец 1', end = '')
        print( '%5s' % arr[k][j], end = '' ) 
        k += 1
        i += 1

matrix(m)'''


# Создать список любых объектов, 
# в цикле напечатать в консоль: объект и его индекс

'''newObject = ['str', str, 123, 'asdasd']

for i in newObject:
	print( '%15s' % i, newObject.index(i))'''

# Создать список с тремя значениями 'to-delete' 
# и нескольми любыми другими, 
# удалить из него все значения 'to-delete'

'''toDelete = ['toDelete','asd' ,'yu','toDelete','ppp' ]

i = 0

for i in toDelete:
    if i == 'toDelete' :
        toDelete.remove('toDelete')

print(toDelete)

toDel = ['toDel','dssad','toDel','123123','lld','aa','toDel', str]
toDel = [dell for dell in toDel if dell !='to-delete']
print(toDel)
'''
 


# Пройти по всем числам от 1 до 10
#  в обратную сторону (то есть: от 10 до 1)
# , напечатать их в консоль

'''i = 0

for i in range(10, 0, -1):
	print(i)'''
    