# 8.- Hacer un programa que resuelva lo siguiente. ¿Cuanto es el X por ciento de X numero?

porce = int(input("Ingrese el Porcentaje a calcular: "))
num = int(input("Ingrese el número al que se le calculará el porcentaje: "))

num_por= (porce*num)/100

print("Resultado:")
print(num_por)