a = {a: a ** 2 for a in range(7)}
print( { i : i for i in range(1,22) if i%7 == 0 } )
print([i for i in range(1,100) if i%7 == 0])

print('a' ,a)
print( dict.values(a) )