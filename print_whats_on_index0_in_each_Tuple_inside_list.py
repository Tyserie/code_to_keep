list = [(1, u'abc'), (2, u'def')]

for i in list:                    #For every element(each Tuple) in list
    x = [i[0] for i in list]      #x is whats on first possition of every tuple inside the list.
print(x)