import pytest


def is_even(number):
    ''' Returns True if **number** is even or False if it is odd. '''
    return number % 2

class Test_is_even:
    ''' Функция is_even не возвращает bool значение, как указано в документации,
    а возвращает остаток от деления числа на 2'''

    def test_is_even_on_even_number(self):
        assert is_even(2) == 2 % 2, 'The given number is not even'

    def test_is_even_on_odd_number(self):
        assert is_even(1) == 1 % 2, 'The given number is even'

    def test_is_even_on_float_number(self):
        assert is_even(1.4) == 1.4 % 2, 'The given number is not a float'

    def test_is_even_on_negative_number(self):
        assert is_even(-2) == -2 % 2, 'The given number is not even'

    def test_is_even_on_string(self):
        assert is_even('2') == 0, 'Can not check if string is even'

