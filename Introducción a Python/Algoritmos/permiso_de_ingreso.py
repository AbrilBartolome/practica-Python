# Paso 1: Solicitar al usuario que ingrese la edad del cliente
    
edad = int(input("Ingrese la edad del cliente:  "))

# Paso 2: Verificar si la edad ingresada cumple con los requisitos del establecimiento

#-Una forma de resumir el bloque de código de abajo es haciendo un ternario:
# permitido = True if edad >=18 else False

permitido = True
if edad >= 18:
    permitido = True
else:
    permitido = False

# Paso 3: Mostrar al usuario si el cliente puede ingresar o no

if permitido:
    print("Puede ingresar.")
else:
    print("Lo sentimos, no puede ingresar.")