qtdNomes = int(input())
def inverter (qtdNomes):
    if qtdNomes > 0:
        nome = input()
        print(nome[::-1])
        inverter(qtdNomes -1)
inverter(qtdNomes)