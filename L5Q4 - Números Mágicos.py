def mdc(a, b):
  if(b == 0): 
    return a 
  else: 
    return mdc(b,a % b)

def mmc(a, b):
  return a*b/mdc(a, b)
    
def repetir_mdc(sequencia):
  if len(sequencia) == 1:
    maior = sequencia[0]
  else:
    maior = mdc(sequencia[0], sequencia[1])
    for i in range(2, len(sequencia)):
      maior = mdc(maior, sequencia[i])
  return maior
    
def repetir_mmc(sequencia):
  if len(sequencia) == 1:
    menor = sequencia[0]
  else:
    menor = mmc(sequencia[0], sequencia[1])
    for i in range(2, len(sequencia)):
      menor = mmc(menor, sequencia[i])
  return menor

def fatorialx(number):
  if number == 1:
    return number
  else:
    return number*fatorialx(number-1)

def e_magico(sequencia):
  mdc = repetir_mdc(sequencia)
  mmc = repetir_mmc(sequencia)
  if abs(mmc/mdc) != mmc and abs(mmc/mdc) != 1:
    degree = fatorialx(len(sequencia))+abs(mmc/mdc)
    return True, degree
  else:
    return False, None
    
n = int(input())
for x in range(n):
  qi = int(input())
  sequencia = list(map(int, input().split()))
  magic, degree = e_magico(sequencia)
  if magic:
    print(f'Numeros magicos! {degree:.1f}')
  else:
    print('Numeros feios')