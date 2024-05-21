#3.- Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for

respuesta="si"
while respuesta == "si":
 print("Ingrese un numero del 0 al 59: ")
 numero = int(input(""))

 cuadrado = numero**2

 print("El cuadrado de su numero es: ")
 print(cuadrado)
 respuesta=input("¿Desea ingresar otro numero?")