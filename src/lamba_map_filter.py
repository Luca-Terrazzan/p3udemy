# lambda functions in maps and filters

def to_square(num):
    return num ** 2

print(
    list(
        map(
            to_square,
            [1, 2, 3, 4, 5]
        )
    )
)

def is_even(word):
    return len(word) % 2 == 0

print(list(filter(is_even, ['asd', 'aa', 'asas', 'asdsa'])))

# some lambdas
print(list(map(
    lambda i: i[0] * i[1],
    [(1, 2), (56, 5)]
)))
