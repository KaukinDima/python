from collections import OrderedDict

words = {'ac':33, 'gw':20, 'ap':102, 'za':321, 'bs':10}
t = OrderedDict((word, True) for word in words)
print(t['ac'])