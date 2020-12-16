# Created by Leon Hunter at 9:54 AM 10/23/2020
class Calculator(object):
    def add(self, a, b):
        return int(a) + int(b)

    def subtract(self, a, b):
        returnint(a) - int(b)

    def multiply(self, a, b):
        return int(a) * int(b)

    def divide(self, a, b):
        return round(int(a)/int(b), 3)
