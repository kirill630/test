class Calc:

    def mult(self, x, y):
        return x * y

    def divis(self, x, y):
       if y == 0:
           return "Error"
       else:
           return x / y

    def plus(self, x, y):
        return x + y

    def subs(self, x, y):
        return x - y