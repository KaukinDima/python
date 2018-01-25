s = 'string'
t = 'asd,asd,asd'
# print(s[1:])

s = 'z' + s[1:] 
# print(s)

# print(s.find('r'))


# print(s.replace('r', 'xss'))
# print(t.split(','))
# print(t.upper())

# print('%s, eggs, and %s' % ('spam', 'SPAM!'))

# print('{0}, eggs, and {1}'.format('spam', 'SPAM!') )

# print(dir(s))

a = t.split(',')
a.append('ttt')
a.pop(3)
print(a)
