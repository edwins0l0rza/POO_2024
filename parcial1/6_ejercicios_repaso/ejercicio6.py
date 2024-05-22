# 6.- Mostrar todas las tablas del 1 al 10. Mostrando el titulo de la tabla 
# y luego las multiplicaciones del 1 al 10

tabla_desde = 1 
tabla_hasta = 10 
desde = 1 
hasta = 10

for num1 in range(tabla_desde, tabla_hasta + 1):
	print(f'Tabla de multiplicar del {num1}:') 
	for num2 in range(desde, hasta + 1):
		print(f'{num1} x {num2} = {num1 * num2}')
	print() 
    