def myFunc() :
    print('Myfunc')

test = myFunc

nList = []

nList.append(myFunc)
# nList[0]()
# print(myFunc)
# 
# print('func is object', isinstance(myFunc, object))test = myFunc
# 
# test()
# print('func is object', isinstance(test, object))


# try :
#     d = 2 
#     d()
# except TypeError as e :
    # print('is not function')

# print( callable(nList[0]) )



# localGlobal

some = 123

def yy() :
    some = 0
    print("local some var \n", some)
    def someInner() :
        print('inner')
yy()

print("global some var\n", some)