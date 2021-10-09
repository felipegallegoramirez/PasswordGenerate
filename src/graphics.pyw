import tkinter as tk
import Main as fun
from pathlib import Path

my_dir = Path(__file__).parent


ventana = tk.Tk()
ventana.iconbitmap(my_dir / "src/key.ico")
ventana.geometry("500x400")
ventana.title("Passwor Generate")


etiqueta = tk.Label(ventana, text="Name page (lowercase)", width=20, height=5)
etiqueta.grid(row=0, column=0)
pag = tk.Entry(ventana, width=50)
pag.grid(row=0, column=1)
etiqueta = tk.Label(ventana, text="Password basic", width=20, height=5)
etiqueta.grid(row=1, column=0)
contr = tk.Entry(ventana, width=50)
contr.grid(row=1, column=1)

etiqueta = tk.Label(ventana, text="Password 32C:", width=20, height=5)
etiqueta.grid(row=3, column=0)
resul32 = tk.Entry(ventana, width=50)
resul32.grid(row=3, column=1)
etiqueta = tk.Label(ventana, text="Password 16C:", width=20, height=5)
etiqueta.grid(row=4, column=0)
resul16 = tk.Entry(ventana, width=50)
resul16.grid(row=4, column=1)

fun.verify()


def send():
    pagt = pag.get()
    contrt = contr.get()
    re = fun.Basic(pagt, contrt)
    resul16.delete(0, tk.END)
    resul32.delete(0, tk.END)
    resul32.insert(0, re)
    resul16.insert(0, re[0:16])


boton1 = tk.Button(ventana, text="Generate password", command=send)
boton1.grid(row=2, column=1)
ventana.mainloop()
