#ejercicio 1
def es_primo(numero):
    if numero <= 1:
        return False
    
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True

def numeros_primos_hasta_n(n):
    primos = []
    for numero in range(1, n + 1):
        if es_primo(numero):
            primos.append(numero)
    return primos

numero_n = int(input("Ingresa un número n: "))
primos_en_rango = numeros_primos_hasta_n(numero_n)
print("Números primos hasta", numero_n, "son:", primos_en_rango)
#ejercicio 2
def hacer_sandwich_v1():
    ingredientes = []
    ingrediente = input("Ingresa un condimento para el sándwich (o escribe 'salir' para terminar): ")

    while ingrediente.lower() != 'salir':
        ingredientes.append(ingrediente)
        print("Se ha agregado el ingrediente '{}' al sándwich.".format(ingrediente))
        ingrediente = input("Ingresa otro ingrediente (o escribe 'salir' para terminar): ")

    print("Los ingredientes del milanguche son:", ", ".join(ingredientes))

hacer_sandwich_v1()

#ejercicio 3 A
def hacer_remera(tamaño, mensaje):
    print("Tamaño de la remera:", tamaño)
    print("Mensaje impreso en la remera:", mensaje)

print("Llamada usando argumentos por posición:")
hacer_remera('M', 'cumbia , 420 ')

print("\nLlamada usando argumentos por clave:")
hacer_remera(mensaje='I <3 milanguche', tamaño='S')

#ejercicio 3 B

def hacer_remera(tamaño='L', mensaje='Me gusta Python'):
    print("Tamaño de la remera:", tamaño)
    print("Mensaje impreso en la remera:", mensaje)

print("Remera con valores por defecto:")
hacer_remera()

print("\nRemera con valores diferentes:")
hacer_remera(tamaño='XXL', mensaje=' Hola')

#ejercicio 4

def fibonacci(n):
    fib_nums = [0, 1] 
    while len(fib_nums) < n:
        next_num = fib_nums[-1] + fib_nums[-2]
        fib_nums.append(next_num)
    return fib_nums[:n]

n = int(input("Ingresa el número n para obtener los primeros n números de la serie de Fibonacci: "))
result = fibonacci(n)
print("Los primeros", n, "números de la serie de Fibonacci son:", result)
