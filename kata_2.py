

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']
#ejercicio 1 
print(planets)
#agregando a pluton
planets.append('pluton')
#mostrando el ultimo elemento
print(planets[-1])

#ejercicio 3 
planeta_buscar = input('Buscar este planeta:')
# Muestra los planetas más cercanos al sol

indice_planeta = planets.index(planeta_buscar)
print('planetas mas cercanos a  ' + planeta_buscar)
print(planets[0:indice_planeta])

#Muestra los planetas más lejanos al sol

print('planetas mas lejanos a al  ' + planeta_buscar)
print(planets[indice_planeta + 1:])