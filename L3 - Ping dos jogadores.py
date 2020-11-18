list = [ ]
numbers = [ ]
people = [ ]
max_player = [ ]
min_player = [ ]
number_of_players = int(input())
for players in range(number_of_players):
    list.append(input().split())
# print(list)
for items in list:
    x = items[1].replace('ms','')
    people.append(items[0])
    numbers.append(int(x))

for index,x in enumerate(numbers):
    if x == max(numbers):
       max_player.append(people[index])
    if x == min(numbers):
       min_player.append(people[index])

#join ele percorre o array e concatena coisas a ele, sem necessidade do for
print(f'O maior ping é {max(numbers)}ms, do(s) jogador(es) {", ".join(max_player)}. E o menor é {min(numbers)}ms, do(s) jogador(es) {", ".join(min_player)}')

