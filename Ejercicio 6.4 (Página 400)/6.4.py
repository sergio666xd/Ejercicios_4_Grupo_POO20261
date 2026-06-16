import tkinter as tk
from tkinter import scrolledtext

class AppExcepciones(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Excepciones (OOP) - Ejercicio 6.4")
        self.geometry("450x450")
        
        # UI
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)
        
        tk.Label(btn_frame, text="Ejercicio 6.4 - Pág. 400").pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Prueba Excepciones", command=self.ejecutar_prueba).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Excepción Límite", command=self.ejecutar_limite).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Excepción Formato", command=self.ejecutar_formato).pack(side=tk.LEFT, padx=5)
        
        self.log_area = scrolledtext.ScrolledText(self, width=50, height=20)
        self.log_area.pack(pady=10)

    def ejecutar_prueba(self):
        self.log_area.delete('1.0', tk.END)
        PruebaExcepciones().main(self.log_area)

    def ejecutar_limite(self):
        self.log_area.delete('1.0', tk.END)
        ExcepcionFueraLimite().main(self.log_area)

    def ejecutar_formato(self):
        self.log_area.delete('1.0', tk.END)
        ExcepcionFormatoNumero().main(self.log_area)

class PruebaExcepciones:
    def main(self, log):
        log.insert(tk.END, "--- Ejercicio 6.4 ---\n")
        # Bloque 1
        log.insert(tk.END, "Ingresando al primer try\n")
        try:
            10000 / 0
        except ZeroDivisionError:
            log.insert(tk.END, "División por cero\n")
        finally:
            log.insert(tk.END, "Ingresando al primer finally\n")
        # Bloque 2
        log.insert(tk.END, "Ingresando al segundo try\n")
        try:
            objeto = None
            objeto.toString()
        except Exception:
            log.insert(tk.END, "Ocurrió una excepción\n")
        finally:
            log.insert(tk.END, "Ingresando al segundo finally\n")

class ExcepcionFueraLimite:
    def main(self, log):
        try:
            texto = "Programación"
            log.insert(tk.END, texto[14])
        except IndexError:
            log.insert(tk.END, "Indice de string por fuera del límite\n")

class ExcepcionFormatoNumero:
    def main(self, log):
        try:
            int("Número")
        except ValueError:
            log.insert(tk.END, "Excepción de formato de número\n")
        finally:
            log.insert(tk.END, "Ingresando al finally\n")

if __name__ == "__main__":
    app = AppExcepciones()
    app.mainloop()