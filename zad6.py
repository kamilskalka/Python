#Napisać obiektowo prosty dekorator na funkcji wypisującej jakiś string, a celem dekoratora jest zamiana liter w napisie na duże litery

class DecoratorClass:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        return result.upper()

@DecoratorClass
def decorator():
    return "hello there"

print(decorator())

