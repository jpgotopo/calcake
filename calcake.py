import tkinter as tk
from tkinter import messagebox
from ttkthemes import ThemedTk
import ttkthemes
from ttkthemes import ThemedTk


# Función para calcular los ingredientes
def calcular_ingredientes(tamaño):
    base = (1/3) * tamaño - 1
    factores = {
        "Huevos": 1,
        "Harina": 25,
        "Azúcar": 5,
        "Cacao": 30
    }
    return {ing: round(factores[ing] * base) for ing in factores}


# Función que se ejecuta al presionar el botón
def on_calcular():
    try:
        tamaño = int(entry_tamaño.get())
        if tamaño < 15:
            messagebox.showwarning("Advertencia", "El tamaño debe ser al menos 15.")
            return
        resultados = calcular_ingredientes(tamaño)
        texto_resultado.config(state='normal')
        texto_resultado.delete('1.0', tk.END)
        texto_resultado.insert(tk.END, f"Tamaño {tamaño}:\n")
        for ing, cant in resultados.items():
            texto_resultado.insert(tk.END, f"{ing+':':<7} {cant}\n")
        texto_resultado.config(state='disabled')
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un número válido.")


# Crear ventana principal con tema moderno
ventana = ThemedTk(theme="adapta")  # Puedes probar otros temas: 'adapta', 'radiance', 'equilux', etc.
ventana.title("Calculadora de Ingredientes por Tamaño")
ventana.geometry("450x350")
ventana.resizable(False, False)

# Etiqueta y entrada para el tamaño
label_tamaño = tk.Label(ventana, text="Ingresa el tamaño:", font=("Segoe UI", 12))
label_tamaño.pack(pady=8)

entry_tamaño = tk.Entry(ventana, font=('Segoe UI', 14), justify='center')
entry_tamaño.pack(pady=5, padx=20, ipadx=10, ipady=4)

# Botón para calcular
boton_calcular = tk.Button(ventana, text="Calcular Ingredientes", command=on_calcular, font=("Segoe UI", 11), bg="#4CAF50", fg="white")
boton_calcular.pack(pady=10)

# Área de texto para mostrar resultados
texto_resultado = tk.Text(ventana, height=9, width=35, state='disabled', font=('Consolas', 12))
texto_resultado.pack(pady=10)

# Iniciar la aplicación
ventana.mainloop()