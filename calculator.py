from add import add
from subtract import subtract
from multiply import multiply
from divide import divide
from modulo import modulo
from power import power


class Calculator:
    def add(self, a, b):
        return add(a, b)

    def subtract(self, a, b):
        return subtract(a, b)

    def multiply(self, a, b):
        return multiply(a, b)

    def divide(self, a, b):
        return divide(a, b)

    def modulo(self, a, b):
        return modulo(a, b)

    def power(self, a, b):
        return power(a, b)
