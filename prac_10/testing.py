"""Testing tasks with asserts and doctests"""

def repeat_string(s, n):
    return s * n


def is_long_word(word, length=5):
    return len(word) >= length


def format_sentence(phrase):
    """
    >>> format_sentence("hello")
    'Hello.'
    >>> format_sentence("hello.")
    'Hello.'
    >>> format_sentence("HELLO WORLD")
    'Hello world.'
    """
    phrase = phrase.strip().rstrip('.')
    phrase = phrase.capitalize()
    return phrase + '.'


# Car class test
class Car:
    def __init__(self, name, fuel):
        self.name = name
        self.fuel = fuel


# Assert tests
car1 = Car("Test", 50)
assert car1.fuel == 50
car2 = Car("Empty", 0)
assert car2.fuel == 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()