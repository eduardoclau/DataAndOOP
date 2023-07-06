import math


class Calculadora:

    def __init__(self):
        numeroInteiroA = int(
            input("Digite o primeiro inteiro (penúltimo número do seu RU):  "))
        numeroInteiroB = int(
            input("Digite o segundo inteiro (último número do seu RU): "))

        if numeroInteiroA == 0:
            numeroInteiroA = 5

        if numeroInteiroB == 0:
            numeroInteiroB = 5

        operacao = int(input("Escolha uma operação: \n \
                            1 - Soma \n \
                            2 - Subtração \n \
                            3 - Multiplicação \n \
                            4 - Divisão \n \
                            5 - Expoente \n \
                            6 - Resto \n \
                            7 - Raíz Quadrada \n"))

        if operacao == 1:
            self.soma(numeroInteiroA, numeroInteiroB)
        elif operacao == 2:
            self.subtraçao(numeroInteiroA, numeroInteiroB)
        elif operacao == 3:
            self.multiplicaçao(numeroInteiroA, numeroInteiroB)
        elif operacao == 4:
            self.divisao(numeroInteiroA, numeroInteiroB)
        elif operacao == 5:
            self.expoente(numeroInteiroA, numeroInteiroB)
        elif operacao == 6:
            self.resto(numeroInteiroA, numeroInteiroB)
        elif operacao == 7:
            self.sqtr(numeroInteiroA, numeroInteiroB)

    def soma(self, numeroInteiroA, numeroInteiroB):
        soma = numeroInteiroA + numeroInteiroB
        print("A soma é:", soma)

    def subtraçao(self, numeroInteiroA, numeroInteiroB):
        subtraçao = numeroInteiroA - numeroInteiroB
        print("A subtração é:", subtraçao)

    def multiplicaçao(self, numeroInteiroA, numeroInteiroB):
        multiplicaçao = numeroInteiroA * numeroInteiroB
        print("A multiplicação é:", multiplicaçao)

    def divisao(self, numeroInteiroA, numeroInteiroB):
        divisao = numeroInteiroA / numeroInteiroB
        print("A divisão é:", divisao)

    def expoente(self, numeroInteiroA, numeroInteiroB):
        expoente = numeroInteiroA ** numeroInteiroB
        print("O expoente é:", expoente)

    def resto(self, numeroInteiroA, numeroInteiroB):
        resto = numeroInteiroA % numeroInteiroB
        print("O resto é:", resto)

    def sqtr(self, numeroInteiroA, numeroInteiroB):
        sqtr = math.sqrt(numeroInteiroA + numeroInteiroB)
        return print("A raíz quadrada é:", sqtr)


resposta = Calculadora()
