# def factorial(n) :
#     if n == 1 :
#         return 1
#     return n * factorial(n - 1)

# print( factorial(4) )


filed = ( 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15 )

i = 0
for i in range(0, 16, 4) : 
    print( filed[i:i+4] )
