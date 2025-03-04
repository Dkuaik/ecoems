# ui/main_window.py
import tkinter as tk
from ui.generic_window import GenericPromptWindow

# Funciones dummy para generar el prompt (lógica de negocio pendiente)
def dummy_generate_prompt_question(params):
    return f"Prompt para Question Generator:\n{params}"

def dummy_generate_prompt_mental_health(params):
    return f"Prompt para Mental Health:\n{params}"

# Diccionario de configuración para Question Generator
question_fields_config = {
    "materia": {
        "label": "Materia",
        "type": "entry",
        "default": "Matemáticas"
    },
    "subtopico": {
        "label": "Subtópico",
        "type": "entry",
        "default": "Ecuaciones de primer grado"
    },
    "numero_preguntas": {
        "label": "Número de preguntas",
        "type": "entry",
        "default": "10",
        "cast": int
    },
    "nivel_bloom": {
        "label": "Nivel de Bloom",
        "type": "optionmenu",
        "options": ["Conocimiento", "Comprensión", "Aplicación", "Análisis", "Síntesis", "Evaluación"],
        "default": "Aplicación"
    },
    "dificultad": {
        "label": "Dificultad",
        "type": "optionmenu",
        "options": ["Baja", "Media", "Alta"],
        "default": "Media"
    },
    "estilo_pregunta": {
        "label": "Estilo de pregunta",
        "type": "entry",
        "default": "Práctico"
    },
    "entrenamiento_habilidades": {
        "label": "Entrenamiento de habilidades",
        "type": "entry",
        "default": "Resolución de problemas"
    },
    "tipo_retroalimentacion": {
        "label": "Retroalimentación (Sí/No)",
        "type": "optionmenu",
        "options": ["Sí", "No"],
        "default": "Sí"
    },
    "ejemplos_vida_real": {
        "label": "Ejemplos de la vida real (Sí/No)",
        "type": "optionmenu",
        "options": ["Sí", "No"],
        "default": "No"
    }
}

# Diccionario de configuración para Mental Health
mental_health_fields_config = {
    "nombre": {
        "label": "Nombre",
        "type": "entry",
        "default": "Usuario"
    },
    "edad": {
        "label": "Edad",
        "type": "entry",
        "default": "30",
        "cast": int
    },
    "estado_animo": {
        "label": "Estado de ánimo",
        "type": "optionmenu",
        "options": ["Feliz", "Triste", "Ansioso", "Estresado"],
        "default": "Feliz"
    },
    "nivel_estres": {
        "label": "Nivel de estrés (1-10)",
        "type": "entry",
        "default": "5",
        "cast": int
    }
}


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Generador de Prompts Avanzado")
        self.setup_widgets()

    def setup_widgets(self):
        # Etiqueta para mostrar mensajes o estado (opcional)
        self.result_label = tk.Label(self.root, text="", wraplength=400)
        self.result_label.pack(pady=10)

        # Botón para abrir la ventana de Question Generator
        tk.Button(
            self.root,
            text="Question Generator",
            command=lambda: GenericPromptWindow(
                self.root,
                "Configuración de Question Generator",
                question_fields_config,
                dummy_generate_prompt_question
            )
        ).pack(pady=10)

        # Botón para abrir la ventana de Mental Health
        tk.Button(
            self.root,
            text="Mental Health",
            command=lambda: GenericPromptWindow(
                self.root,
                "Configuración de Mental Health",
                mental_health_fields_config,
                dummy_generate_prompt_mental_health
            )
        ).pack(pady=10)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = MainWindow()
    app.run()
