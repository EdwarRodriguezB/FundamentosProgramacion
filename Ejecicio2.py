
#Ejercicio 1 Vendedor


Sueldo= float (input("Digite su Sueldo"))
Venta1= float (input("Digite su nota primera venta"))
Venta2= float (input("Digite su nota Segunda venta"))
Venta3= float (input("Digite su nota Tercer venta"))

Res= Sueldo + Venta1 + Venta2 + Venta3 * 0.10 

print("Su sueldo mas variable es de {}".format(Res))



#Ejercicio 2 Tienda

PrimerArticulo= float (input("Digite el primer articulo"))
SegundoArticulo= float (input("Digite el segundo articulo"))
TercerArticulo= float (input("Digite el tercer articulo"))
CuartoArticulo= float (input("Digite el cuarto articulo"))

Resul= PrimerArticulo + SegundoArticulo + TercerArticulo + CuartoArticulo * 0.15 

print("Su descuento es de {}".format(Resul))

#Ejercicio 3 Calificacion Final Alumno

Nota1= float (input("Digite su nota primera nota"))
Nota2= float (input("Digite su nota Segunda nota"))
Nota3= float (input("Digite su nota Tercer nota"))

prom = round ((Nota1 + Nota2 + Nota3))

print(f"Su promedio es ={prom}")

#Ejercicio 4 Calificacion Final Alumno

Gen1= float (input("Digite su Genero"))
Gen2= float (input("Digite su Genero"))
Gen3= float (input("Digite su Genero"))
Gen4= float (input("Digite su Genero"))

prome = round ((Gen1 + Gen2 + Gen3 + Gen4))

print(f"Su promedio es ={prome}")


