# n = int(input())
# a = input().split()
# count = 0
# for i in range(len(a)):
#     for j in range(1, len(a)):
#         for k in range(2, len(a)):
#             if a[i] != a[j] and a[i] != a[k] and a[j] != a[k]:
#                 if a[i] + a[j] < a[k] or a[i] + a[k] < a[j] or a[k] + a[j] < a[i]:zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
#                     count+=1
#
# if count >0:
#     print('Existe um caso que não é possivel formar um triangulo')
# else:
#     print('E sempre possivel formar um triangulo')


#
#
# n = int(input())
# a = input().split()
# def verificar(x):
#     NaoTriangulo = 0
#
#     for i in range(len(a)):
#         for j in range(1, len(a)):
#             for k in range(2, len(a)):
#                 # if a[i] != a[j] and a[i] != a[k] and a[j] != a[k]:
#                     if (a[i] + a[j] <= a[k]) or (a[i] + a[k] <= a[j]) or (a[k] + a[j] <= a[i]):
#                         NaoTriangulo += 1
#
#     if NaoTriangulo > 0:
#         return print('Existe um caso que não é possivel formar um triangulo')
#     else:
#         return print('E sempre possivel formar um triangulo')
#
#
# verificar(a)
#

n = int(input())
a = list(map(int, input().split()))

def verificar(x):
    NaoTriangulo = 0

    for x in a:
      for y in a:
        for z in a:
          if (x + y <= z ) or (x + z <= y) or (y+z <= x):
              # print(x,y,z)
              NaoTriangulo += 1

    if NaoTriangulo > 0:
        return print('Existe um caso que não é possivel formar um triangulo')
    else:
        return print('E sempre possivel formar um triangulo')
verificar(a)