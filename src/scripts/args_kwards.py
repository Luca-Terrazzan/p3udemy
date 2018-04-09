# *args and **kwargs

def addition(*addendums):
    '''
    Use a dynamic amount of numbers to add
    addendums is treated as a tuple!
    '''
    return sum(addendums)

print(addition(1,2,3))
print(addition(1,2,3,4,5,6,7))

# Key worded arguments, these are treated as dicts
def func(**words):
    print(words)
    for word in words.items():
        print(word)

func(asD="asd", temp="ddddd")

def args_kwargs(*args, **kwargs):
    print("Args are {} while kwargs has this food item: {}".format(args, kwargs["food"]))

args_kwargs(1, 2, 3, 4, 5, food="can", temp="other")
