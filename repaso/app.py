class Operaciones:
    def suma(a, b):
        return a +b

    def multiplicar(a,b,c):
        return a*b*c

    def restar (a,b):
        return a-b

operacion = Operaciones

resultado = operacion.suma(1,1)
resultado_2 = operacion.multiplicar(2,2,2)

print(resultado_2)

class Operaciones_2:
    def __init__(self, a, b ):
        self.primer_numero = a
        self.segundo_numero = b

    def restar(self):
        return self.primer_numero - self.segundo_numero

    def suma(self):
        return self.primer_numero + self.segundo_numero

op2 = Operaciones_2(4,5)

print(op2.restar())
print(op2.suma())