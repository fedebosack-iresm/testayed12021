dinero_disponible = 50000.0
"""Ingresa dinero al sistema y actualiza el saldo"""
def ingresar_y_actualizar():
    global dinero_disponible
    while True:
        try:
            dinero_ingresar = float(input("Ingrese dinero a depositar: "))
            if dinero_ingresar > 0 :
                break
            else:
                print("Por favor ingrese una suma positiva")
        except:
            print("Error en los parametros")
        
    

    dinero_disponible += dinero_ingresar
    return dinero_disponible

def retirar_y_actualizar():
    global dinero_disponible
    while True:
        try:
            dinero_retirar= float(input("Ingrese el dinero a retirar: "))
            if dinero_retirar > 0 and dinero_retirar<=dinero_disponible :
                break
            else:
                print("Por favor ingrese una suma positiva o menor al dinero disponible")
        except:
            print("Error en los parametros")
        
    dinero_disponible -= dinero_retirar
    return dinero_disponible

def consultar_saldo():
    global dinero_disponible
    print(f"El dinero disponible es: {dinero_disponible}")
