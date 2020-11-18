totalHoras =120
aang = 0.5*120
sokka = 0.5*120
zuko = 0.04*120
katara = 0.01*120
iroh =  0.06*120
mantimentos = 0.07*120
e1 = input()
if e1 == 'Aang':
    totalHoras = 120 + aang
elif e1 =='Sokka':
    totalHoras =120- sokka
elif e1 == 'Zuko':
    totalHoras = 120- zuko
elif e1 == 'Katara':
    totalHoras = 120 - katara
elif e1 == 'Iroh':
    totalHoras = 120- iroh
else:
    totalHoras = 120- mantimentos

e2 = input()
if e2 == 'Aang':
    totalHoras += aang
elif e2 =='Sokka':
    totalHoras -= sokka
elif e2 == 'Zuko':
    totalHoras -= zuko
elif e2 == 'Katara':
    totalHoras -= katara
elif e2 == 'Iroh':
    totalHoras -=  iroh
else:
    totalHoras -= mantimentos

e3 = input()

if e3 == 'Aang':
    totalHoras += aang
elif e3 =='Sokka':
    totalHoras -= sokka
elif e3 == 'Zuko':
    totalHoras -= zuko
elif e3 == 'Katara':
    totalHoras -= katara
elif e3 == 'Iroh':
    totalHoras -= iroh
else:
    totalHoras -= mantimentos

e4 = input()

if e4 == 'Aang':
    totalHoras += aang
elif e4 =='Sokka':
    totalHoras -= sokka
elif e4 == 'Zuko':
    totalHoras -= zuko
elif e4 == 'Katara':
    totalHoras -= katara
elif e4 == 'Iroh':
    totalHoras -= iroh
else:
    totalHoras -= mantimentos

e5 = input()
if e5 == 'Aang':
    totalHoras =+ aang
elif e5 =='Sokka':
    totalHoras -= sokka
elif e5 == 'Zuko':
    totalHoras -=  zuko
elif e5 == 'Katara':
    totalHoras -=  katara
elif e5 == 'Iroh':
    totalHoras -= iroh
else:
    totalHoras -= mantimentos
print(f'Appa conseguira voar por {totalHoras:.2f} horas.')