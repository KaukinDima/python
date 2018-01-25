import sys
t = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
col2 = [row[1] for row in t]


# arr = [ [1,2,3 ], [4,5,6] ]
# arr = [ [1,2,3 ], [4,5,6] ]
# col = [row[2] for row in arr]
# print(col)
# print(col2)

newar = [1,2,3]
newar.remove(3)
newar.append(3)
print(newar)

b = [4,5,6]

newar.extend(b)
newar.insert(len(newar), 8)
print(newar)

newar.pop(1)
print(newar)
newar.clear()
print(newar)

a=[1, 2, 2, 3, 3]
print(a.count(2))

a.sort()
a.reverse()