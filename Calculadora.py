import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("320x350")
app.title("Calculadora")

# ... widgets con ctk.CTkEntry, ctk.CTkButton, etc.


def Opciones():
    print("OPCIONES\n")
    print("0. Salir")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Potencia")
    print("6. Modulo")

def Numeros():
    try: 
        a = float(input("Ingrese el primero numero: "))
        b = float(input("Ingrese el segundo numero: "))
        return a, b
    except ValueError:
        print("Por favor, ingrese numeros")
        return None,None

def Suma():
    a, b = Numeros()
    if a is not None and b is not None:
        resultado = a + b
        print("El resultado de la suma es: ", resultado)

    while True:
                print("¿Desea encadenar la operacio1n? (s/n)")
                if input().lower() == "s":
                    a = resultado
                    b = float(input("Ingrese el segundo numero: "))
                    resultado = a + b
                    print("\nEl resultado de la suma es: ", resultado)
                else:
                    break

def Resta():
    a, b = Numeros()
    if a is not None and b is not None:
        resultado = a - b
        print("El resultado de la resta es: ", resultado)

    while True:
                print("¿Desea encadenar la operacio1n? (s/n)")
                if input().lower() == "s":
                    a = resultado
                    b = float(input("Ingrese el segundo numero: "))
                    resultado = a - b
                    print("\nEl resultado de la resta es: ", resultado)
                else:
                    break

def Multiplicacion():
    a, b = Numeros()
    if a is not None and b is not None:
        resultado = a * b
        print("El resultado de la multiplicacion es: ", resultado)

    while True:
                print("¿Desea encadenar la operacio1n? (s/n)")
                if input().lower() == "s":
                    a = resultado
                    b = float(input("Ingrese el segundo numero: "))
                    resultado = a * b
                    print("\nEl resultado de la multiplicacion es: ", resultado)
                else:
                    break

def Division():
    a, b = Numeros()
    if a is not None and b is not None:
        if b == 0:
            print("No se puede dividir entre cero")
        else:
            resultado = a / b
            print("El resultado de la division es: ", resultado)

        while True:
                    print("¿Desea encadenar la operacio1n? (s/n)")
                    if input().lower() == "s":
                        a = resultado
                        b = float(input("Ingrese el segundo numero: "))
                        resultado = a / b
                        print("\nEl resultado de la division es: ", resultado)
                    else:
                        break

def Potencia():
    a, b = Numeros()
    if a is not None and b is not None:
        resultado = a ** b
        print("El resultado de la potencia es: ", resultado)

    while True:
                print("¿Desea encadenar la operacio1n? (s/n)")
                if input().lower() == "s":
                    a = resultado
                    b = float(input("Ingrese el segundo numero: "))
                    resultado = a ** b
                    print("\nEl resultado de la potencia es: ", resultado)
                else:
                    break

def Modulo():
    a, b = Numeros()
    if a is not None and b is not None:
        resultado = a % b
        print("El resultado del modulo es: ", resultado)

    while True:
        print("¿Desea encadenar la operacio1n? (s/n)")
        if input().lower() == "s":
            a = resultado
            b = float(input("Ingrese el segundo numero: "))
            resultado = a % b
            print("\nEl resultado del modulo es: ", resultado)
        else:
            break



while True:
    Opciones()
    opcion = input("\nIngrese la opcion deseada: ")
    if opcion == "0":
        print("Gracias por usar la calculadora")
        break;
    if opcion == "1":
        Suma()
    elif opcion == "2":
        Resta()
    elif opcion == "3":
        Multiplicacion()
    elif opcion == "4":
        Division()
    elif opcion == "5":
        Potencia()
    elif opcion == "6":
        Modulo()
    else:
        print("Opcion no valida, por favor ingrese una opcion correcta")




    



