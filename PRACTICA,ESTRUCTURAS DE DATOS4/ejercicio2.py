productos = {
    "Cafe": 3.0,
    "Pan": 1.0,
    "Galleta": 3.0,
    "Huevos": 2.0,
    "Queso": 4.0,
}

nombre_producto = input("Ingrese el nombre de un producto: ")
cantidad = int(input("Ingrese la cantidad: "))

if nombre_producto in productos:
    precio_unitario = productos[nombre_producto]
    total_pagar = precio_unitario * cantidad
    print(f"El total a pagar por {cantidad} {nombre_producto} es: ${total_pagar}" )
else:
    print("El producto ingresado no se encuentra disponible.")