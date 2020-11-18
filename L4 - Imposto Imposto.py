n_habitantes = int(input())
salarios = []
impostos = []
for i in range(n_habitantes):
    salario = int(input())
    salarios.append(salario)
def calcular_imposto(salario):
    if salario <=1000:
        return 0
    elif 1001<=salario<=5000:
        return float((salario*0.075)-100)
    elif 5001<=salario<=7000:
        return float((salario*0.15)-500)
    elif salario>7000:
        return float((salario*0.225)-700)
for i in range(n_habitantes):
    imposto = calcular_imposto(salarios[i])
    impostos.append(imposto)
def imprimir_impostos(y):
    for x in impostos:
            print(f"{x:.2f}")
imprimir_impostos(impostos)