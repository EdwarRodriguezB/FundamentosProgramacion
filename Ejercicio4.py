#Variables

EdadP = 1
impares = 1
pares = 1
Acu = 1

#Ejercicio 1 Numeros Pares

for i in range(0,102,2):
    print(i)

#Ejercicio 2 Tabla de multiplicar

Numero = int(input("Digite el numero a multiplicar"))

for i in range(11):
    print(i," x ", Numero, " = ", i * Numero)

#Ejercicio 3 Edad

num = int(input("Digite su edad"))

for i in range(EdadP,num,1):
    print(i) 

#Ejercicio 4 Numero Entero


NumeroEntero = int(input("Digite el numero entero positivo"))

for i in range (impares,NumeroEntero,2):
    print(i,",")

#Ejercicio 5 Suma numero pares

for i in range(100):
    Acu=i
    print("El total de los pares es =",i*100)


    