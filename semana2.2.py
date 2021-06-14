"""condicion.py"""

class condicion:

    def __init__(self,n1, n2) -> None:
        self.num1=n1
        self.num2=n2
        numero = self.num1+self.num2
        self.num3=numero

    def condicion(self):
        # if _ _ _ elif _ _ _ else _ _ _: permiten condicionar la ejecucion de uno o varios bloques mediante condiciones
        # de sentencias al cumplimiento de una o varias condiciones.
        if self.num1 == self.num2 :
            print("numero1: {} y numero2: {} son iguales".format(self.num1, self.num2))
        elif self.num1 < self.num3:
            print("numero1: {} es menor que numero3: {}".format(self.num1, self.num3))
        else:
            print("no son iguales")
        print("fin del metodo")



condi1 = condicion(4,8)
print(condi1.num3)
print(condi1.condicion())



"""ciclos.py"""

class ciclo:

    def __init__(self,num=10):
        self.numero=num

    def usowhile(self):
        print("Dentro de la clase", self.numero)
        # ciclo repetitivo que se ejecuta mientras la condicion se cumple (verdadero),
        # es decir sale por falso

        caracter=""
        while caracter.lower() not in ("a", "e", "i", "o","u"):
            caracter = input("Ingrese vocal: ")
    
        
        print("Felicitaciones el caracter: {} es una vocal".format(caracter))

ciclo1 = ciclo()
print("fuera de la clase", ciclo1.numero)
#print(ciclo1.usowhile())
ciclo1.usowhile()
