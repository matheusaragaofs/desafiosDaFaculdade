consumoM3 = int(input())
assinatura = 7
if 0<=consumoM3<= 10:
    print(assinatura)
elif 11<= consumoM3 <=30:
    taxa10 = consumoM3 - 10
    print(assinatura+taxa10)
elif 31<= consumoM3 <=100:
    taxa30 = consumoM3 -30
    print(assinatura+(taxa30*2)+20)
elif consumoM3 >100:
    taxa100 = consumoM3 -100
    print(assinatura+(taxa100*5)+20+140)





