# Entendendo a lista e seus indices
numeroNosIndices = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# fatiamento

print(numeroNosIndices[3:])
print(numeroNosIndices[:3])
print(numeroNosIndices[::2])
print(numeroNosIndices[1::2])
print(numeroNosIndices[0])
print(numeroNosIndices[-1])
print(numeroNosIndices[1])
print(numeroNosIndices[0:])

# entendendo len()
# entendendo o fatiamento

frase = 'Curso em video python'
print(frase)
print("_"*12)
print(frase)
print(frase[0])
print(frase[5:9])
print(frase.count('o'))
print(len(frase))
print("Curso" in frase)
print("Curso" in frase[::-1])
print(frase.lower())
print(frase.upper())
print(frase.capitalize())
print(frase.title())
print(frase.split())
print(frase.strip())