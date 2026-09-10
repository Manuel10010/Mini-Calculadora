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
        messagebox.showerror("Error", "Ingrese números válidos y seleccione una operación")
    except ZeroDivisionError:
        messagebox.showerror("Error", "No se puede dividir entre cero")

    chk_var.set(False)


def usar_anterior():
    if chk_var.get():
        texto_resultado = label_resultado.cget("text")
        partes = texto_resultado.split(": ")
        
        # Verificar si existe un resultado numérico calculado
        if len(partes) > 1 and partes[1].strip() != "":
            entry_a.delete(0, tk.END)
            entry_a.insert(0, partes[1])
        else:
            messagebox.showinfo("Información", "Aún no hay un resultado previo para cargar")
            chk_var.set(False)
    else:
        entry_a.delete(0, tk.END)
        entry_b.delete(0, tk.END)
        label_resultado.config(text="Resultado: ")


ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("500x400")
ventana.configure(bg="lightblue")



tk.Label(ventana, text="Primer número:", bg="lightblue").pack()
entry_a = tk.Entry(ventana)
entry_a.pack()


tk.Label(ventana, text="Segundo número:", bg="lightblue").pack()
entry_b = tk.Entry(ventana)
entry_b.pack()


tk.Label(ventana, text="Presione para desplegar: ", bg="lightblue").pack()
operacion = tk.StringVar(value="Operaciones")
tk.OptionMenu(ventana, operacion, "+", "-", "*", "/", "%", "**").pack()



chk_var = tk.BooleanVar()
tk.Checkbutton(ventana, text="Usar anterior", variable=chk_var, command=usar_anterior).pack()


tk.Button(ventana, text="Calcular", command=calcular, bg="lightblue").pack(pady=20)


label_resultado = tk.Label(ventana, text="Resultado: ", font=("Arial", 20, "bold"), bg="lightgreen")
label_resultado.pack(pady=10)



ventana.mainloop()




    



