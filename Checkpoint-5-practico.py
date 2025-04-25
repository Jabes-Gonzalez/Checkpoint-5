# Ejercicio-1

for numero in range(1, 101):
    print(numero)

print()

#Ejercicio-2

def suma(a, b, c):
    return a + b + c

resultado = suma(17, 20, 50)
print(resultado)

print()

#Ejercicio-3

suma_lambda = lambda a, b, c: a + b + c

resultado_lambda = suma_lambda(17, 20, 50)
print(resultado_lambda)

print()

#ejercicio-4

nombre = 'Enrique'
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']

if nombre in lista_nombre:
  print(f"El siguiente nombre '{nombre}' consta en la lista.")
else:
  print(f"El siguiente nombre '{nombre}' no consta en la lista.")