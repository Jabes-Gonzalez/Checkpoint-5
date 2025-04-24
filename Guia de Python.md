# ¿Qué es un condicional?

En programación, las condicionales son una herramienta esencial que nos permite tomar decisiones dinámicas a lo largo de la ejecución de nuestro programa. Estas instrucciones tienen la capacidad de dividir el flujo del programa en diferentes caminos lógicos, los cuales eventualmente se vuelven a unir en algún punto específico.

Mediante las condicionales, podemos definir la ruta que debe seguir el programa según la evaluación de ciertas expresiones. Estas expresiones, a menudo comparaciones o verificaciones lógicas, determinan la dirección que tomará la ejecución del código. Las condicionales proporcionan flexibilidad y control, permitiéndonos adaptar el comportamiento del programa en función de las circunstancias durante su ejecución.

## Comprendiendo las condicionales

Para entender mejor cómo funcionan las condicionales, podemos visualizarlo a través de un diagrama de flujo. En este diagrama, evaluamos una expresión en función de un valor de entrada y, según el resultado de esa evaluación, seguimos el flujo establecido. Es como un mapa visual que nos guía a través de las diferentes ramificaciones del código, dependiendo de las condiciones que se cumplan o no. Esto facilita la comprensión de cómo las decisiones afectan el curso de ejecución del programa.

## Declaraciones de condicionales

Python cuenta con 3 tipos de declaraciones para el uso de condicionales, aquí las diferentes formas de emplear condicionales en Python:

* Declaración If.
* Declaración Else.
* Declaración Elif.

A continuación revisaremos las definiciones y ejemplos de cada una de ellos.

### 1. Declaración If

En Python, la declaración `if` se usa para evaluar una expresión. Si la expresión dentro de esta condición es evaluada como verdadera, se ejecutará la instrucción definida dentro del bloque `if`; en caso contrario, si la expresión es falsa, la instrucción no se ejecutará. Es una forma de introducir lógica condicional en el código, permitiendo que ciertas acciones se realicen solo cuando se cumplen ciertas condiciones.


```python
n = int(input("Choose number: "))

if n % 2 == 0:
         print("The number is even")
```


Es importante señalar que la declaración condicional if en Python realiza una conversión automática a booleano de la expresión proporcionada. Esto implica que si se le pasa un valor almacenado en una variable, es crucial tener en cuenta los tipos de datos considerados como falsos.

En Python, hay ciertos tipos de datos que se consideran automáticamente como valores falsos. Estos incluyen:

* False - El valor booleano False.
* None - El valor nulo.
* 0 - El número entero cero.
* 0.0 - El número de punto flotante cero.
* '' - La cadena vacía.
* [] - La lista vacía.
* () - La tupla vacía.
* {} - El diccionario vacío.
* set() - El conjunto vacío.

### 2. Declaración Else
En Python, la declaración else se utiliza en conjunto con una declaración if. La declaración else se ejecuta únicamente si la condición evaluada por la declaración if resulta ser falsa. En otras palabras, cuando la instrucción dentro del if no se ejecuta debido a que la condición es falsa, entonces la instrucción dentro del bloque else es la que se ejecuta. Esto proporciona una bifurcación en la lógica del programa, permitiendo definir acciones alternativas cuando la condición inicial no se cumple.

```python
n = int(input("Choose number: "))

if n % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
```

### 3. Declaración Elif
En Python, la declaración elif se emplea para especificar condiciones adicionales dentro de la estructura de un bloque if. Si la primera condición en el bloque if resulta ser falsa, el programa procederá a verificar la siguiente condición dentro de elif.

La declaración elif es útil para añadir casuísticas adicionales a la evaluación, permitiendo así gestionar múltiples condiciones de manera organizada. Es importante destacar que es posible anidar varias declaraciones elif según la necesidad y criterio del desarrollador. Esto proporciona flexibilidad en la lógica del programa al permitir manejar diferentes escenarios en función de las condiciones evaluadas.

```python
alice_age = int(input("Choose number: "))

if alice_age < 18:
    print("Alice is younger than 18 years.")
elif 18 <= alice_age <= 21:
    print("Alice has between 18 and 21 years.")
else:
    print("Alice has more than 21 years.")
```

# ¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?

Por lo general, el código en Python se ejecuta de manera secuencial, es decir, empieza por la primera línea, pasa a la segunda y así va. Sin embargo, existen casos, cuando se necesita que un fragmento de código se repita. Python cuenta con las herramientas llamadas bucles o loops para facilitar esta tarea. Los bucles te permiten cambiar el flujo lineal del programa para repetir una parte del código tantas veces que sea necesario.

## ¿Qué son los bucles en Python?
Primero, aclaremos el término iterar que significa “realizar una acción varias veces”, y cada repetición se llama iteración. Los bucles sirven para que los programas implementen iteraciones, es decir, ejecuten un mismo bloque de código dos o más veces mientras se cumple la condición declarada. Cuando la condición llega a ser falsa, el programa sale del bucle y continúa con su ejecución de forma secuencial.

El flujo de ejecución es el siguiente:

* Evaluar la condición, definiendo si es verdadera o falsa (True o False).
* Si la condición es verdadera, ejecutar el cuerpo y regresar al paso 1.
* Si la condición es falsa, salir del bucle y continuar con la siguiente sentencia.
   
**Python cuenta con dos tipos de bucles fundamentales:**

**While**, los que tienen un número indefinido de iteraciones,
**For**, los que tienen un número definido de iteraciones.

### Bucle while
Una forma de iteración en Python es la sentencia while que permite repetir la ejecución de un bloque de código siempre y cuando la condición del bucle sea verdadera.

La sintaxis es muy simple:

```python
    while <condición>:
    <bloque de código>
```

El código del cuerpo del bucle debe cambiar una o más variables hasta que la condición resulte falsa y el bucle termine. En este ejemplo la variable de iteración cambia el valor del parámetro cada vez que se ejecuta el ciclo y controla cuándo finaliza el ciclo.

```python
x = 5
while x > 0:
x -= 1
print(x)
print('¡Pum!')
4
3
2
1
0
¡Pum!
```

En Python se puede indicar una operación alternativa mediante la sentencia else al final del bucle while. El fragmento de código dentro de else se ejecutará una vez la condición del bucle ya no devuelve True, es decir, hasta que la condición del bucle deja de cumplirse.

```python
x = 5
while x > 0:
x -= 1
print(x)
else:
print('Fin del bucle')
4
3
2
1
0
Fin del bucle
```

Si no hay ninguna variable de iteración que determine cuántas veces tiene que ejecutar un bucle y la condición permanece verdadera, el mismo fragmento de código se repetirá para siempre, lo que producirá un bucle infinito. Normalmente, los bucles infinitos se deben a errores y hay que evitarlos para no perder el control del programa.

```python
x = 5
while x > 0:
print('¡Al infinito y más allá!')
¡Al infinito y más allá!
¡Al infinito y más allá!
¡Al infinito y más allá!
…
```

### Bucle For
La sentencia for forma un bucle definido que recorre los elementos de una colección de datos o una secuencia ordenada como listas, diccionarios, tuplas, strings, etc. El bucle hará tantas iteraciones cuántos elementos hay en la secuencia.

El bucle for en Python tiene la siguiente sintaxis:

```python
for <variable> in <secuencia>:
<bloque de código>
```

Por ejemplo, para iterar los elementos de la lista “idiomas” con un bucle for, se le asigna el nombre “idioma” a una variable que representará los elementos de la lista en cada repetición.

```python
idiomas = ['Árabe', 'Inglés', 'Francés', 'Español']
índice = 0
for idioma in idiomas:
print ('Este idioma está en la lista: ' + idiomas[índice])
índice += 1
Este idioma está en la lista: Árabe
Este idioma está en la lista: Inglés
Este idioma está en la lista: Francés
Este idioma está en la lista: Español
```

El bucle for con cadenas tipo string funciona de la misma manera, pero con caracteres en lugar de elementos:

```python
cadena = 'Python'
for carácter in cadena:
print(carácter)
P
y
t
h
o
n
```

Igual que con el bucle while, se puede usar la sentencia else para agregar una acción adicional al finalizar el bucle. Veamos un ejemplo con la función range():

```python
for x in range(5):
print(x)
else:
print('Fin del bucle')
0
1
2
3
4
Fin del bucle
```

## Cómo controlar los bucles en Python

Usando ciertas instrucciones, puedes interrumpir el flujo de ejecución de un bucle si lo necesitas. La sentencia break “rompe” el bucle en cualquier momento, aun cuando la condición sigue siendo verdadera. En el siguiente ejemplo el bucle for recorre todos los números del rango del 0 al 4, pero el programa finaliza cuando el número tenga el valor de 3:

```python
for x in range(5):
if x == 3:
break
print (x)
0
1
2
```

Lo mismo pasa con el bucle while: al recibir una entrada determinada, el programa sale del bucle y procede a la siguiente línea del código:

```python
while True:
respuesta = input('> ')
if respuesta == 'salir':
break
else:
print(respuesta)
print ('¡Adiós!')
> ¡Hola!
¡Hola!
> ¿Qué tal?
¿Qué tal?
> salir
¡Adiós!
```

La sentencia continue termina la iteración corriente sin tomar en cuenta el código que está debajo y se vuelve al inicio del bucle.

```python
x = 0
while x < 5:
x += 1
if x == 3:
continue
print(x)
1
2
4
5
```

En el ejemplo abajo, cuando el valor llegue a ‘y’, el programa saltará de nuevo al bucle for sin ejecutar la última línea de print y sin salir del bucle:

```python
for carácter in 'Python': 
if carácter == 'y':
continue
print ('La letra es:', carácter)
La letra es: P
La letra es: t
La letra es: h
La letra es: o
La letra es: n
```

Por último, cabe mencionar la sentencia pass. Cuando la ejecución de un bucle llega a la sentencia pass, simplemente pasa a la siguiente instrucción sin modificar el flujo establecido. Habitualmente, se utiliza para reservar espacio si en el momento de escribir un código hay una parte que todavía no está completada:

```python
for x in range(1, 5):
if x == 2:
pass
print (x)
1
2
3
4
```

# ¿Qué es una lista por comprensión en Python?

Una lista por comprensión en Python (o list comprehension) es una construcción sintáctica que permite crear listas de manera concisa y eficiente a partir de cualquier iterable (como listas, tuplas, cadenas, etc.), aplicando operaciones y/o condiciones a sus elementos en una sola línea de código

### Sintaxis básica
La estructura general de una lista por comprensión es:

```python

nueva_lista = [expresión for elemento in iterable if condición]
```

* expresión: lo que deseas agregar a la nueva lista (puede ser el elemento tal cual o una transformación de este).

* for elemento in iterable: recorre cada elemento del iterable.

* if condición (opcional): filtra los elementos que cumplen la condición

### Ejemplos prácticos
Si queremos obtener las letras de una palabra:

```python
lista = [letra for letra in 'casa']
# Resultado: ['c', 'a', 's', 'a']
```

* Si queremos crear una lista con los cuadrados de los números del 0 al 10:

```python
lista = [numero**2 for numero in range(0, 11)]
# Resultado: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

* Filtrar y transformar elementos (cuadrados de los números impares del 1 al 10):

```python
lista = [x**2 for x in range(1, 11) if x % 2 != 0]
# Resultado: [1, 9, 25, 49, 81]
```

### Ventajas

* Permite escribir código más compacto y legible, evitando bucles for tradicionales y llamadas a funciones como map() o filter()
* Es más eficiente en términos de velocidad y claridad cuando se trata de operaciones simples sobre iterables

En resumen podriamos dercir que las listas por comprensión son una herramienta poderosa y elegante de Python para crear nuevas listas a partir de otras colecciones, aplicando transformaciones y filtros en una sola línea de código.

# ¿Qué es un argumento en Python?

En Python, los argumentos son los valores que se proporcionan a una función cuando se la llama. Permiten que las funciones sean reutilizables y flexibles, ya que pueden operar sobre diferentes datos cada vez que se ejecutan.

### Tipos de Argumentos
* Argumentos Posicionales:
Se asignan a los parámetros según el orden en que se pasan.

```python
def resta(a, b):
    return a - b

resta(10, 3)  # a=10, b=3
```

* Argumentos Nombrados (Keyword Arguments):
Se pasan especificando el nombre del parámetro, lo que permite cambiar el orden y mejora la claridad.

```python
def persona(nombre, edad):
    print(f"{nombre} tiene {edad} años.")

persona(edad=25, nombre="Carlos")
```

* Argumentos por Defecto:
Permiten asignar un valor predeterminado a un parámetro. Si no se proporciona el argumento al llamar la función, se usa el valor por defecto.

```python
def saludar(nombre="invitado"):
    print(f"Hola, {nombre}!")

saludar()           # Hola, invitado!
saludar("María")    # Hola, María!
```

* Argumentos de Longitud Variable:
Permiten que una función acepte cualquier cantidad de argumentos.

**args**: Recibe una tupla con todos los argumentos posicionales extra.

**kwargs**: Recibe un diccionario con todos los argumentos nombrados extra.

```python
def sumar(*numeros):
    return sum(numeros)

print(sumar(1, 2, 3))  # 6

def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=30)
```

Los argumentos en Python son esenciales para el funcionamiento flexible y reutilizable de las funciones. Permiten pasar datos, establecer valores por defecto y manejar cantidades variables de información, haciendo que el código sea más limpio, eficiente y fácil de mantener.

# ¿Qué es una función Lambda en Python?

Las expresiones lambda en Python son, en esencia, funciones pequeñas, sin nombre, definidas con la palabra clave lambda. Lo que las hace únicas es su capacidad para ser escritas en una sola línea de código, concentrando una funcionalidad específica en una expresión concisa. A diferencia de las funciones definidas con def, que pueden contener múltiples expresiones y sentencias, una función lambda se limita a una única expresión cuyo resultado es el valor de retorno de la función.

## Sintaxis de las Funciones Lambda
Se definen utilizando la palabra clave lambda, seguida de los argumentos, un signo de dos puntos (:), y finalmente la expresión que se evaluará y devolverá implícitamente.

```python
sumar = lambda x, y: x + y
print(sumar(5, 3))  # Salida: 8
```

La belleza de las funciones lambda reside en su simplicidad y en la capacidad de escribir funciones pequeñas de manera rápida y eficiente.

## Comparación entre Funciones Lambda y Funciones Normales

Aunque las funciones lambda y las funciones normales pueden parecer similares porque ambas pueden realizar operaciones y devolver resultados, existen diferencias clave entre ellas.

Definición: Las funciones normales se definen con la palabra clave def y pueden contener múltiples expresiones. Las funciones lambda se definen con la palabra clave lambda y están limitadas a una sola expresión.
Nombre: Las funciones normales tienen un nombre con el cual se pueden referenciar o invocar más tarde. Las funciones lambda son anónimas, lo que significa que no tienen un nombre asignado, aunque se pueden asignar a una variable.
Uso: Las funciones normales son ideales para operaciones complejas y pueden contener varias líneas de código, incluidas declaraciones de control de flujo. Las funciones lambda están diseñadas para tareas sencillas y suelen usarse en contextos donde se necesita una función por un corto periodo de tiempo o directamente dentro de otra función como un argumento.
Las funciones lambda son especialmente útiles en combinación con funciones como filter(), map(), y reduce(), donde actúan sobre una lista (o cualquier iterable) de manera eficiente y concisa. Por ejemplo, usar map() con una función lambda para duplicar los valores en una lista se vería así:

```python
numeros = [1, 2, 3, 4, 5]
duplicado = list(map(lambda x: x * 2, numeros))
print(duplicado)  # Salida: [2, 4, 6, 8, 10]
```

## Casos de Uso Comunes para Funciones Lambda

Las funciones lambda son una herramienta extremadamente versátil en Python, utilizadas en una amplia gama de aplicaciones. Su sintaxis concisa y la capacidad de operar sobre datos de forma eficiente las hacen ideales para varios patrones comunes de programación, especialmente en el análisis de datos y la manipulación de estructuras de datos complejas.

### Uso con filter()

La función filter() en Python toma dos argumentos: una función y una lista (o cualquier iterable). La función se aplica a cada elemento de la lista, y filter() devuelve un nuevo iterable con los elementos para los cuales la función devuelve True. Las funciones lambda son particularmente útiles aquí, permitiendo definir el criterio de filtrado de manera rápida y concisa:

```python
numeros = range(-5, 6)
positivos = list(filter(lambda x: x > 0, numeros))
print(positivos)  # Salida: [1, 2, 3, 4, 5]
```

### Uso con map()
Similar a filter(), map() aplica una función a todos los elementos de un iterable y devuelve un nuevo iterable con los resultados. Las funciones lambda se utilizan comúnmente con map() para realizar transformaciones simples en los datos:

```python
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)  # Salida: [1, 4, 9, 16, 25]
```

### Uso con reduce()
La función reduce(), que forma parte del módulo functools, es otra herramienta poderosa que se beneficia del uso de funciones lambda. Reduce() aplica una función de dos argumentos acumulativamente a los elementos de un iterable, de izquierda a derecha, para reducir el iterable a un único valor. Este método es útil para operaciones como sumar todos los elementos de una lista:

```python
from functools import reduce
numeros = [1, 2, 3, 4, 5]
suma_total = reduce(lambda x, y: x + y, numeros)
print(suma_total)  # Salida: 15
```

## Limitaciones de las Funciones Lambda
Aunque las funciones lambda son herramientas poderosas y flexibles en Python, tienen sus limitaciones. Comprender estas restricciones es crucial para utilizarlas de manera efectiva y evitar errores comunes en el desarrollo de software.

Simplicidad de expresión: La principal limitación de una función lambda es que solo puede contener una expresión. Esto significa que no pueden albergar múltiples declaraciones o expresiones complejas que incluyan bucles o estructuras de control de flujo como if-else más allá de las operaciones ternarias.
Legibilidad: Aunque la concisión es una ventaja, el uso excesivo de funciones lambda puede perjudicar la legibilidad del código, especialmente para usuarios que no están familiarizados con su sintaxis o para operaciones complejas que serían más claras con funciones definidas tradicionalmente.
Depuración difícil: Las funciones lambda son difíciles de depurar debido a su naturaleza anónima. Las herramientas de depuración no pueden asignarles un nombre de función significativo, lo que puede complicar el rastreo de errores.
No es adecuado para operaciones complejas: Debido a la restricción de una sola expresión, las funciones lambda no son adecuadas para operaciones que requieren pasos múltiples o lógica compleja.

# ¿Qué es un paquete pip?

En Python, un paquete pip es un conjunto de módulos y bibliotecas que pueden ser instalados y gestionados utilizando pip, el sistema de gestión de paquetes estándar para Python, estos paquetes permiten añadir funcionalidades adicionales a tus proyectos, como herramientas para análisis de datos, desarrollo web, aprendizaje automático, entre otros.

pip facilita la instalación, actualización y eliminación de estos paquetes desde el repositorio oficial de Python, conocido como PyPI (Python Package Index), así como la gestión de sus dependencias y versiones. Por ejemplo, para instalar un paquete basta con ejecutar en la terminal:

```bash
pip install nombre_del_paquete
```

Además, pip permite listar los paquetes instalados, desinstalarlos, actualizar sus versiones y gestionar archivos de requisitos (requirements.txt) para reproducir entornos de desarrollo fácilmente

Un paquete pip es cualquier biblioteca o módulo de Python que puede ser instalado y administrado mediante el gestor de paquetes pip, facilitando la reutilización y distribución de código en la comunidad Python