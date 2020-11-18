# D² = (X1 - X2)² + (Z1 - Z2)²
# Para entregar os ferros para as vilas, Tantan precisaria saber quais as
# distâncias da sua localidade para cada vila, podendo se programar em suas viagens.
# Nas anotações de Tantan, as vilas estavam associadas as seguintes coordenadas:
#
# Hogsmeade (X: 34, Y: 110, Z: 220)
# Kakariko (X: 0, Y: 64, Z: 0)
# Solitude (X: 140, Y: 200, Z: 456)
X = int(input())
Z = int(input())
DistHogs = ((X - 34)**2 + (Z - 220)**2)**(1/2)
DistKaka = ((X - 0)**2 + (Z-0)**2)**(1/2)
DistSolit  = ((X - 140)**2 + (Z-456)**2)**(1/2)
print(f'{DistHogs:.2f}')
print(f'{DistKaka:.2f}')
print(f'{DistSolit:.2f}')
# print(round(DistHogs,2))
# print(round(DistKaka,2))
# print(round(DistSolit,2))
