from tkinter import Tk, Label, Entry, Button, messagebox, StringVar, IntVar
from functools import reduce

# --- Funciones puras (sin efectos secundarios) ---
def promedio_aspecto(aspecto, datos):
    """Calcula el promedio de un aspecto usando map y reduce"""
    return reduce(lambda x, y: x + y, map(lambda e: e[aspecto], datos)) / len(datos)

def promedio_general_asignatura(datos):
    """Calcula el promedio general de una asignatura"""
    total = 0
    count = 0
    for encuesta in datos:
        total += encuesta["actividades"] + encuesta["herramientas"] + encuesta["contenido"]
        count += 3  # 3 aspectos por encuesta
    return total / count

def filtrar_asignatura(asignatura, datos):
    """Filtra encuestas por asignatura usando filter"""
    return list(filter(lambda e: e["asignatura"] == asignatura, datos))

def mejor_aspecto(asignatura, datos):
    """Encuentra el aspecto mejor calificado usando reduce"""
    aspectos = ["actividades", "herramientas", "contenido"]
    return reduce(
        lambda a, b: a if promedio_aspecto(a, datos) > promedio_aspecto(b, datos) else b,
        aspectos
    )

# --- Interfaz gráfica mínima ---
class EncuestaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Encuesta de Asignaturas")
        
        # Variables
        self.asignatura = StringVar()
        self.actividades = IntVar()
        self.herramientas = IntVar()
        self.contenido = IntVar()
        
        # Widgets
        Label(root, text="Asignatura:").pack()
        Entry(root, textvariable=self.asignatura).pack()
        
        Label(root, text="Actividades (1-5):").pack()
        Entry(root, textvariable=self.actividades).pack()
        
        Label(root, text="Herramientas (1-5):").pack()
        Entry(root, textvariable=self.herramientas).pack()
        
        Label(root, text="Contenido (1-5):").pack()
        Entry(root, textvariable=self.contenido).pack()
        
        Button(root, text="Guardar", command=self.guardar).pack()
        Button(root, text="Resultados", command=self.mostrar).pack()
        
        # Base de datos en memoria
        self.encuestas = []
    
    def guardar(self):
        """Guarda una nueva encuesta (única función con efecto secundario)"""
        nueva = {
            "asignatura": self.asignatura.get(),
            "actividades": self.actividades.get(),
            "herramientas": self.herramientas.get(),
            "contenido": self.contenido.get()
        }
        self.encuestas.append(nueva)
        messagebox.showinfo("Éxito", "Encuesta guardada!")
    
    def mostrar(self):
        """Muestra resultados usando funciones de orden superior"""
        if not self.encuestas:
            messagebox.showerror("Error", "No hay encuestas")
            return
        
        # Procesamiento con map/filter/reduce
        asignaturas = list(set(map(lambda e: e["asignatura"], self.encuestas)))
        resultados = "RESULTADOS: "
        
        for asignatura in asignaturas:
            datos = filtrar_asignatura(asignatura, self.encuestas)
            resultados += f"ASIGNATURA: {asignatura}"
            resultados += f"  Promedio actividades: {promedio_aspecto('actividades', datos):.1f}"
            resultados += f"  Promedio herramientas: {promedio_aspecto('herramientas', datos):.1f}"
            resultados += f"  Promedio contenido: {promedio_aspecto('contenido', datos):.1f}"
            resultados += f"  Promedio general: {promedio_general_asignatura(datos):.1f}"
            resultados += f"  Mejor aspecto: {mejor_aspecto(asignatura, datos)}"
        
        messagebox.showinfo("Análisis", resultados)

# --- Ejecutar app ---
if __name__ == "__main__":
    root = Tk()
    app = EncuestaApp(root)
    root.mainloop()