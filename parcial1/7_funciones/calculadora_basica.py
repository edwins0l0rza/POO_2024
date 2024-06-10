"""VERSION #0"""
# print("..::: CALCULADORA BÁSICA :::.. \n 1.-SUMA \n 2.- RESTA \n 3.-MULTIPLICACIÓN \n 4.-DIVISIÓN \n 5.-SALIR")
# opcion=input("\t Elige una opción: ").upper()

# if opcion == "5" or opcion=="SALIR":
#     print("¡¡Gracias Por Utilizar Mi Sistema!!")

# else:
#     n1=int(input("Numero #1: "))
#     n2=int(input("Numero #2: "))

# if opcion=="1" or opcion=="+" or opcion=="SUMA":
#     print(f"{n1}+{n2}={n1+n2}")
# elif opcion=="2" or opcion=="-" or opcion=="RESTA":
#     print(f"{n1}-{n2}={n1-n2}")
# elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
#     print(f"{n1}-{n2}={n1*n2}")
# elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
#     print(f"{n1}-{n2}={n1/n2}")


"""VERSION #1"""
from varias_funciones import espereTecla, calculadora, solicitarNumeros
# def solicitarNumeros():
#     global n1,n2
#     n1=int(input("Numero #1: "))
#     n2=int(input("Numero #2: "))
#     # return n1,n2

# def calculadora(n1,n2,opcion):
#      if opcion=="1" or opcion=="+" or opcion=="SUMA":
        
#         return f"{n1}+{n2}={n1+n2}"
#      elif opcion=="2" or opcion=="-" or opcion=="RESTA":
        
#         return f"{n1}-{n2}={n1-n2}"
#      elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
       
#         return f"{n1}*{n2}={n1*n2}"
#      elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
        
#         return f"{n1}/{n2}={n1/n2}"
     

# def espereTecla():
   # print("Oprima cualquier tecla para continuar...")
   # input()

import os
opcion=True
while opcion:
    os.system("cls")
    print("..::: CALCULADORA BÁSICA :::.. \n 1.-SUMA \n 2.-RESTA \n 3.-MULTIPLICACIÓN \n 4.-DIVISIÓN \n 5.-SALIR")
    opcion=input("\t Elige una opción: ").upper()
    if opcion!="5":
     n1,n2=solicitarNumeros()
     print(calculadora(n1,n2,opcion))
     espereTecla()
    else:
        opcion=False
        print("Gracias por utilizar el sistema ...")