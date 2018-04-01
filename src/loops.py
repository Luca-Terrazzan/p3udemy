# some loops
# some loops

iterable = [1, 'a', 2, 'g']
for item in iterable:
    print(item)

for even_item in iterable[0::2]:
    print(even_item)

# tuple unpacking
tuple_list = [(1, 2), ('a', 'b')]
for a, b in tuple_list:
    print(a)
    print(b)

# iterato through dicts
d = {
    'k1': 1,
    'k2': 2
}
for item in d:
    print(item) # prints only keys!

for k, v in d.items():
    print(item) # this prints the item!

# while loops
x = 0
while x < 5:
    print(x)
    x += 1
else: # is basically a finally clause
    print('finish!')
