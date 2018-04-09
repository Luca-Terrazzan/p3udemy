# range creates a list of int - start, stop, step
toten = range(5, 10, 2)
print(list(toten))
for num in toten:
    print(num)

# enumerate, gets the tuple of an item paired with its index
for index, letter in enumerate('asdasd'):
    print(f'Index {index} for letter {letter}')

# zip function, tuple packs two lists together. the result has the shortest len
# of all the lists zipped together
for item in zip([1,2,3], [3,2,1]):
    print(item)

# 'in' operator
1 in [1,2,3] == True
'k1' in {'k1': 1} == True

# minimax
min([3,2,5,4,7])
max([3,2,5,4,7])

# import and rand
from random import shuffle # shuffle works in place
l = [1,2,3,4,5,6]
shuffle(l)
print(l)

from random import randint
print( randint(5, 23) )

# user input, it is always a string
input('Enter something: ')

# casting
s = '10'
int(s)
