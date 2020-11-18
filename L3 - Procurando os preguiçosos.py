qtd_tripulantes = int(input())
tripulantes =  []
tasks = [ ]
for x in range(qtd_tripulantes):
         person = input().split()
         tripulantes.append(person[0])
         tasks.append(int(person[1]))

#BUBBLE SORT PARA TASKS
ordenado = False
while not ordenado:
    ordenado = True
    for i in range(len(tripulantes)-1):
        if tasks[i] > tasks[i+1]:
            tasks[i], tasks[i+1] = tasks[i+1],tasks[i]
            tripulantes[i], tripulantes[i + 1] = tripulantes[i + 1], tripulantes[i]
            ordenado = False

        if tasks[i] == tasks[i+1] and  tripulantes[i] > tripulantes[i+1]:
            tripulantes[i], tripulantes[i + 1] = tripulantes[i + 1], tripulantes[i]
            ordenado = False
for i in range(len(tasks)):
    print(f"{tripulantes[i]} {tasks[i]}")

