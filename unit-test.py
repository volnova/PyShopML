# -*- coding: utf-8 -*-
"""Разработайте юнит-тесты проверяющие корректность работы функции.
Удалось ли найти какие-либо дефекты в этой функции, полагаясь на
ее назначение исходя из описания? Учтите, что вопрос не на знание
фреймворков тестирования и их применение, можете взять любой, или
даже разработать ряд самостоятельных функций."""


def is_even(number):
    # Returns True if **number** is even or False if it is odd.
    return number % 2


def test_is_even():
    assert is_even(42) == True


def test_is_odd():
    assert is_even(43) == False

"""Запускаем командой python -m pytest -q unit-test.py
Тесты не упали бы в случае, если бы функции выглядели так:

def test_is_even():
    assert is_even(42) == False

def test_is_odd():
    assert is_even(43) == True

То есть функция is_even() работает не так, как заявлено в её описании."""