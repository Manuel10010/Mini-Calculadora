import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        op = operacion.get()
        
        if op == "+": r = a + b
        elif op == "-": r = a - b
        elif op == "*": r = a * b
        elif op == "/": 
            if b == 0: raise ZeroDivisionError
            r = a / b
        elif op == "%": 
            if b == 0: raise ZeroDivisionError
            r = a % b
        elif op == "**": r = a ** b
        else: raise ValueError("Operación no válida")
        
        label_resultado.config(text=f"Resultado: {r}")
    except ValueError:
        messagebox.showerror("Error", "Ingrese números válidos")
    except ZeroDivisionError:
        messagebox.showerror("Error", "No se puede dividir entre cero")



ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("500x400")



tk.Label(ventana, text="Primer número:").pack()
entry_a = tk.Entry(ventana)
entry_a.pack()

tk.Label(ventana, text="Segundo número:").pack()
entry_b = tk.Entry(ventana)
entry_b.pack()

tk.Label(ventana, text="Presione para desplegar: ").pack()
operacion = tk.StringVar(value="+")
tk.OptionMenu(ventana, operacion, "+", "-", "*", "/", "%", "**").pack()


tk.Button(ventana, text="Calcular", command=calcular).pack(pady=20)



label_resultado = tk.Label(ventana, text="Resultado: ", font=("Arial", 20, "bold"))
label_resultado.pack(pady=10)



ventana.mainloop()




    



