#Taller 1

def Formulario(Form):
    return Form

resp = "si"
while resp =="si" or resp == "s":

    Nombre = input("Digite su nombre : ")
    Apellido = input("Digite su Apellido : ")
    Direccion = input("Digite su Direccion : ")
    Telefono = int(input("Digite su Telefono : "))
    Estado = input("Digite su Estado Civil : ")
    NumHijos = input("Digite su Numero de hijos : ")
    Centi = float(input("Digite su Estatura en centimetros  : "))
    Contratacion = input("Digite su Estatura en fecha de contratacion  : ")
    sueldoB = float(input("Digite su Estatura en Sueldo basico  : "))
    DiasL = int(input("Digite su Estatura en Dias laborados  : "))
    resp = input("Desea volver a llenar el fomulario ")

print(f"Sus datos son : \n Nombre = {Nombre}\n",f"Apellido = {Apellido}\n",f"Direccion = {Direccion}\n",f"Telefono = {Telefono}\n",f"Estado cilvi = {Estado}\n",f"Numeros Hijos = {NumHijos}\n",f"Cuanto mide = {Centi}\n",f"contratacion = {Contratacion}\n",f"Sueldo basico = {sueldoB}\n",f"Dias Laborados = {DiasL}\n")

#Taller 2

#Ejercicio 1 Vendedor

respo= "si"
while respo == "si" or respo == "s":
    Nota1=float(input("Digite Su primera venta : "))
    Nota2=float(input("Digite Su segunda venta : "))
    Nota3=float(input("Digite Su tercera venta : "))

    sum= Nota1+Nota2+Nota3 * 0.10
    print(f"Su venta en total es = {sum}")
    respo = input("¿Desea ejecutar de nuevo(si/no) : ")

#Ejercicio 2 Tienda

respo= "si"
while respo == "si" or respo == "s":
    Venta1=float(input("Digite Su primera venta : "))
    Venta2=float(input("Digite Su segunda venta : "))
    Venta3=float(input("Digite Su tercera venta : "))
    Venta4=float(input("Digite Su cuarta venta : "))

    sum= Venta1+Venta2+Venta3+Venta4 * 0.15

    print("Su venta en total es {}".format(sum))

    respo = input("¿Desea volver a calcular sus ventas de nuevo(si/no) : ")

#Ejercicio 3  Notas

respo= "si"
while respo == "si" or respo == "s":
    Nota1=float(input("Digite Su primera Nota : "))
    Nota2=float(input("Digite Su segunda Nota : "))
    Nota3=float(input("Digite Su tercera Nota : "))
    Nota4=float(input("Digite Su cuarta Nota : "))

    prom = round ((Nota1+Nota2+Nota3+Nota4))

    print(f"Su venta en total es {prom}")

    respo = input("¿Desea volver a calcular sus notas de nuevo(si/no) : ")

#Ejercicio 5 Genero


respo= "si"
while respo == "si" or respo == "s":
    Genero1=float(input("Digite Su Genero Nota : "))
    Genero2=float(input("Digite Su Genero Nota : "))
    Genero3=float(input("Digite Su Genero Nota : "))
    Genero4=float(input("Digite Su Genero Nota : "))

    Generos = round ((Genero1+Genero2+Genero3+Genero4))

    print(f"Su venta en total es {Generos}")

    respo = input("¿Desea volver a calcular los generos de nuevo(si/no) : ")