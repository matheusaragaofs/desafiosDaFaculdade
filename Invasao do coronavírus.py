# O tempo de voo de Appa normalmente são 120 horas, se ele estiver com Aang o tempo aumenta em 50%.
# outros diminuem o tempo de voo dependendo do peso, mantimentos reduzem o tempo em 7%, Sokka em 50%, Zuko em 4%, Katara em 1%,
# Iroh em 6%. Qualquer objeto que não seja uma das pessoas citadas deve ser considerado como mantimento. No máximo Appa consegue levar 5 objetos/pessoas
# diga para Aang quanto tempoAappa conseguirá voar com a precisão de duas casas decimais.
totalHoras =120
e1 = input()
if e1 == 'Aang':
    totalHoras = 120*1.5
elif e1 =='Sokka':
    totalHoras =120*0.5
elif e1 == 'Zuko':
    totalHoras = 120*0.96
elif e1 == 'Katara':
    totalHoras = 120*0.99
elif e1 == 'Iroh':
    totalHoras = 120*0.94
else:
    totalHoras = 120*0.93

#
e2 = input()
if e2 == 'Aang':
    totalHoras *= 1.5
elif e2 == 'Sokka':
    totalHoras *= 0.5
elif e2 == 'Zuko':
    totalHoras  *= 0.96
elif e2 == 'Katara':
    totalHoras *= 0.99
elif e2 == 'Iroh':
    totalHoras *= 0.94
else:
    totalHoras *= 0.93



e3 = input()

if e3 == 'Aang':
    totalHoras *= 1.5
elif e3 == 'Sokka':
    totalHoras *= 0.5
elif e3 == 'Zuko':
    totalHoras  *= 0.96
elif e3 == 'Katara':
    totalHoras *= 0.99
elif e3 == 'Iroh':
    totalHoras *= 0.94
else:
    totalHoras *= 0.93





e4 = input()

if e4 == 'Aang':
    totalHoras *= 1.5
elif e4 == 'Sokka':
    totalHoras *= 0.5
elif e4 == 'Zuko':
    totalHoras  *= 0.96
elif e4 == 'Katara':
    totalHoras *= 0.99
elif e4 == 'Iroh':
    totalHoras *= 0.94
else:
    totalHoras *= 0.93

e5 = input()
if e5 == 'Aang':
    totalHoras *= 1.5
elif e5 == 'Sokka':
    totalHoras *= 0.5
elif e5 == 'Zuko':
    totalHoras  *= 0.96
elif e5 == 'Katara':
    totalHoras *= 0.99
elif e5 == 'Iroh':
    totalHoras *= 0.94
else:
    totalHoras *= 0.93
print(totalHoras)

print(f'Appa conseguira voar por {totalHoras:.2f} horas.')

#
# aang = *1.5
# mant = e*0.93
# sokka = e*0.5
# zuko = e*0.96
# katara = e*0.99
# iroh = e*0.94
# totalHoras