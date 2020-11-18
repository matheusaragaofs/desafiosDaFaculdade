contadorET =  0
contadorREAL1 = 0
contadorREAL2= 0
contadorREAL3=  0
real1 = input()
real2 = input()
real3 = input()
string1 = input()
string2= input()
string3 = input()
string4 =  input()
string5  = input()
familia1 = familia2 = familia3 = 0
for s1 in string1:
    for s2 in string2:
        for s3 in string3:
            for s4 in string4:
                for s5 in string5:
                    Nome = s1 + s2 + s3 + s4 + s5

                    if Nome == real1:
                        contadorREAL1+=1
                    elif Nome == real2:
                        contadorREAL2+=1
                    elif Nome == real3:
                        contadorREAL3+=1
                    else:
                        contadorET+=1

if contadorREAL1==0:
    familia1 =0
else:
    familia1 = 2**contadorREAL1

if contadorREAL2 == 0:
    familia2 = 0
else:
    familia2 = 5**contadorREAL2

if contadorREAL3 == 0:
    familia3 = 0
else:
    familia3 = 7**contadorREAL3


print(f'a familia {real1} possui um poder de {familia1}')
print(f'a familia {real2} possui um poder de {familia2}')
print(f'a famlia {real3} possui um poder de {familia3}')
print(f'os demais ETs somam um poder de {contadorET}')