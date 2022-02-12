#ejercicio 1 
planetas = []
nuevo_planeta = ''

while nuevo_planeta.lower() != 'listo':
    nuevo_planeta = input('Ingresa el nombre del planeta que quieras agrgar: ')
    if(nuevo_planeta.lower() != 'listo'):
        planetas.append(nuevo_planeta)

print(planetas) 

#ejercicio 2

for i in range(len(planetas)):
    print(planetas[i])