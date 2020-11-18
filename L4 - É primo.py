number = int(input())
def primo(x):
    count=0
    for y in range(1,number+1):
       if number%y == 0:
        count+=1
    if count == 2:
        print('E primo')
    else:
        print('Nao e primo')

primo(number)
