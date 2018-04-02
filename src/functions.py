# functions

def hello(name = "noname"):
    '''
    Prints something!
    '''
    print(f"Hello {name}")

hello("asd")
hello()

def has_dog(phrase):
    return "dog" in phrase.lower()

print(has_dog("some dog"))
print(has_dog("some cat"))

def pig_latin(word):
    '''
    If word starts with a consonant, remove it and append it to word,
    then appends 'ay'
    '''
    if word[0] in 'aeiou':
        return word + "ay"
    else:
        return word[1:] + word[0] + "ay"

word = "test"
word_latin = pig_latin(word)

print(word_latin)
