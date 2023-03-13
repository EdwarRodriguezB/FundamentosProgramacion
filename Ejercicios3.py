#variables
edad = int (input("edad:"))
sueldoBasico = float(input("sueldoBasico"))
noHijos = int (input("noHijos:"))
estado = input("estado")

#EJERCICIO 1
if  edad > 55:
    Bono = sueldoBasico * 0.5
    sueldo_total = sueldoBasico + Bono 
    print("Bono de pension ${:,0f} Sueldo Total0 ${:,0f}".format(Bono,sueldo_total))
else:
    print(f"Sueldo Total ${sueldoBasico:,.0f}")

#EJECICIO 2

if  estado == "casado" and noHijos >= 1:
    print("Tiene un viaje pago en los diciembres")
else:
    print("Uste no tiene viaje pago")

#EJERCICIO 3

if sueldoBasico >= 1000000 and sueldoBasico <= 1500000:
    Comision = sueldoBasico *0.02
    comsion1=sueldoBasico+Comision
    print("El valor de la comision es ${:,.0f} El valor Total es ${:,.0f}".format(Comision,comsion1))
elif sueldoBasico >=1500001 and sueldoBasico <= 2000000:
    comision2 = sueldoBasico *0.05
    TotalComsion2 = sueldoBasico + comision2
    print("valor de la comision ${:,.0f} valor Total ${:,.0f}".format(comision2,TotalComsion2))

else:
    print("sin comision")

