iva=(1.16)
basico=(0.987)
intermedio=(1.203)
dap=(12.56)


kWh=int(input("Ingrese la cantidad de kWh que consumió: "))

if kWh  <= 150:
    p_basico=kWh * basico
    basico_iva= p_basico * iva
    basico_total=basico_iva+dap
    print(".::PAGO BÁSICO::.")
    print("Precio por kWh:")
    print(basico)
    print("Total a Pagar:")
    print(basico_total)
elif kWh > 150:
    Wh=kWh-150
    p_basico=kWh * basico
    p_intermedio=Wh * intermedio
    inter_iva= p_intermedio * iva
    inter_total=inter_iva+dap
    total=inter_total+p_basico
    print(".::PAGO INTERMEDIO::.")
    print("Precio por kWh:")
    print(basico)
    print("Precio por kWh:")
    print(intermedio)
    print("Total a Pagar:")
    print(total)