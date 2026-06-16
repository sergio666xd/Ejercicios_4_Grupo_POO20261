import tkinter as tk
from tkinter import messagebox

# ==========================================
# CLASES DE NEGOCIO (EJERCICIOS)
# ==========================================

class Vendedor:
    """Clase del Ejercicio 6.5 Principal"""
    def __init__(self, nombre: str, apellidos: str):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = 0

    def verificarEdad(self, edad: int):
        # Nota: Siguiendo la lógica exacta del libro, si la edad es < 18 salta primero.
        if edad < 0 or edad > 120:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        
        self.edad = edad

    def obtener_datos(self) -> str:
        return f"Nombre del vendedor = {self.nombre}\nApellidos del vendedor = {self.apellidos}\nEdad del vendedor = {self.edad}"


class ObjetoConConstructorInvalido:
    """Clase del Ejercicio Propuesto 1"""
    def __init__(self, parametro: str):
        if not parametro or parametro.strip() == "":
            raise ValueError("¡Error de inicialización! El parámetro del constructor no puede estar vacío.")
        self.parametro = parametro


class TablaASCII:
    """Clase del Ejercicio Propuesto 2"""
    def __init__(self):
        # Mapeo inicial básico de la tabla ASCII estándar
        self._tabla = {chr(i): i for i in range(32, 127)}

    def get(self, simbolo: str) -> int:
        if simbolo is None:
            raise TypeError("El símbolo pasado no puede ser nulo (None).")
        if simbolo not in self._tabla:
            raise KeyError(f"El símbolo '{simbolo}' no existe en el registro de la tabla.")
        return self._tabla[simbolo]

    def set(self, simbolo: str, numero: int):
        if simbolo is None:
            raise TypeError("El símbolo no puede ser nulo (None).")
        if not (0 <= numero <= 255):
            raise ValueError("El número ASCII debe estar en el rango de 0 a 255.")
        self._tabla[simbolo] = numero


# ==========================================
# INTERFAZ GRÁFICA (TKINTER)
# ==========================================

class AppLanzamientoExcepciones(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lanzamiento de Excepciones - Ejercicio 6.5")
        self.geometry("500x550")
        self.resizable(False, False)

        # --- SECCIÓN 1: EJERCICIO 6.5 (VENDEDOR) ---
        lbl_vendedor = tk.Label(self, text="Ejercicio 6.5: Registro de Vendedor", font=("Arial", 12, "bold"))
        lbl_vendedor.pack(pady=10)

        frame_vendedor = tk.Frame(self)
        frame_vendedor.pack(pady=5)

        tk.Label(frame_vendedor, text="Nombre:").grid(row=0, column=0, sticky="e", padx=5, pady=2)
        self.ent_nombre = tk.Entry(frame_vendedor, width=25)
        self.ent_nombre.grid(row=0, column=1, pady=2)

        tk.Label(frame_vendedor, text="Apellidos:").grid(row=1, column=0, sticky="e", padx=5, pady=2)
        self.ent_apellidos = tk.Entry(frame_vendedor, width=25)
        self.ent_apellidos.grid(row=1, column=1, pady=2)

        tk.Label(frame_vendedor, text="Edad:").grid(row=2, column=0, sticky="e", padx=5, pady=2)
        self.ent_edad = tk.Entry(frame_vendedor, width=25)
        self.ent_edad.grid(row=2, column=1, pady=2)

        btn_validar_vendedor = tk.Button(self, text="Instanciar y Verificar Vendedor", command=self.procesar_vendedor, bg="#d4edda")
        btn_validar_vendedor.pack(pady=10)

        tk.Frame(self, height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=10, pady=10)

        # --- SECCIÓN 2: PROPUESTO 1 (CONSTRUCTOR) ---
        lbl_prop1 = tk.Label(self, text="Propuesto 1: Excepción desde Constructor", font=("Arial", 11, "bold"))
        lbl_prop1.pack(pady=5)

        self.ent_constructor = tk.Entry(self, width=30)
        self.ent_constructor.pack(pady=2)
        self.ent_constructor.insert(0, "") # Por defecto vacío para provocar el error fácilmente

        btn_validar_const = tk.Button(self, text="Intentar Crear Objeto", command=self.procesar_constructor, bg="#fff3cd")
        btn_validar_const.pack(pady=5)

        tk.Frame(self, height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=10, pady=10)

        # --- SECCIÓN 3: PROPUESTO 2 (TABLA ASCII) ---
        lbl_prop2 = tk.Label(self, text="Propuesto 2: Registro Tabla ASCII", font=("Arial", 11, "bold"))
        lbl_prop2.pack(pady=5)

        frame_ascii = tk.Frame(self)
        frame_ascii.pack(pady=5)

        tk.Label(frame_ascii, text="Símbolo:").grid(row=0, column=0, padx=5)
        self.ent_simbolo = tk.Entry(frame_ascii, width=10)
        self.ent_simbolo.grid(row=0, column=1, padx=5)

        btn_get_ascii = tk.Button(frame_ascii, text="Buscar Código (GET)", command=self.procesar_get_ascii)
        btn_get_ascii.grid(row=0, column=2, padx=5)

        # Inicializamos la persistencia del objeto ASCII
        self.tabla_ascii = TablaASCII()

    # --- MANEJADORES DE EVENTOS ---
    
    def procesar_vendedor(self):
        nombre = self.ent_nombre.get()
        apellidos = self.ent_apellidos.get()
        edad_str = self.ent_edad.get()

        if not nombre or not apellidos or not edad_str:
            messagebox.showwarning("Campos Incompletos", "Por favor, rellene todos los campos del vendedor.")
            return

        try:
            edad = int(edad_str)
            # Instanciación del objeto
            vendedor = Vendedor(nombre, apellidos)
            # Validación que puede disparar la excepción personalizada
            vendedor.verificarEdad(edad)
            
            # Si pasa la validación con éxito:
            messagebox.showinfo("Éxito", f"¡Vendedor Creado Correctamente!\n\n{vendedor.obtener_datos()}")
        except ValueError as ex:
            # Captura tanto errores de formato numérico como las excepciones manuales de rango de edad
            messagebox.showerror("IllegalArgumentException (Error)", str(ex))

    def procesar_constructor(self):
        valor = self.ent_constructor.get()
        try:
            objeto = ObjetoConConstructorInvalido(valor)
            messagebox.showinfo("Éxito", f"Objeto creado exitosamente con el valor: '{objeto.parametro}'")
        except ValueError as ex:
            messagebox.showerror("Excepción Capturada", str(ex))

    def procesar_get_ascii(self):
        simbolo = self.ent_simbolo.get()
        
        # Simulación de paso de nulo si el campo de texto está vacío por completo bajo ciertas condiciones de prueba
        if simbolo == "NULO":
            simbolo = None

        try:
            resultado = self.tabla_ascii.get(simbolo)
            messagebox.showinfo("Resultado ASCII", f"El valor numérico del símbolo '{simbolo}' es: {resultado}")
        except (TypeError, KeyError) as ex:
            messagebox.showerror("Excepción de Tabla", str(ex))


if __name__ == "__main__":
    app = AppLanzamientoExcepciones()
    app.mainloop()