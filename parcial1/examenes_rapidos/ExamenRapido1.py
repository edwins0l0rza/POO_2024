respuesta="si"
while respuesta == "si":
 input("Ingrese el nombre del paciente: ")
 input("Ingrese su tipo de sangre: ")
 print(".::REGISTRO DE PRESION ARTERIAL::.")
 print("Presion SIStolica:")
 sis1=int(input("1er medición: "))
 sis2=int(input("2da medición: "))
 sis3=int(input("3er medición: "))

 suma_sis=int(sis1+sis2+sis3)
 promedio1=suma_sis/3

 print("Presión DIAstolica:")
 dis1=int(input("1er medición: "))
 dis2=int(input("2da medición: "))
 dis3=int(input("3er medición: "))

 suma_dia=int(dis1+dis2+dis3)
 promedio2=suma_dia/3

 print("Medicion al Final Del Día:")
 fin_sis=int(input("SIStolica: "))
 prome_finsis=(promedio1+fin_sis)/3
 fin_dia=int(input("DIAstolica: "))
 prome_findia=(promedio2+fin_dia)/3

 respuesta=(input("¿Desea checar otro articulo? (si/no) "))

print("PRESIÓN SISTOLICA")
if prome_finsis == "120":
  print("Tiene una presión NORMAL")
elif prome_finsis < "120":
  print("Tiene una presión MALA")

print(promedio1)


print("PRESIÓN DIASTOLICA")
if prome_findia == "80":
  print("Tiene una presion NORMAL")
elif prome_findia < "80":
  print("Tienes una presion BAJA")

print(promedio2)

print("MEDIOCIÓN FINAL:")
print("SIStolica:")
print(prome_finsis)
print("DIAstolica:")
print(prome_findia)