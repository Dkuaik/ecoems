# ui/generic_window.py
import tkinter as tk
from tkinter import Toplevel, messagebox

class GenericPromptWindow:
    def __init__(self, master, title, fields_config, generate_prompt_fn):
        """
        master: widget padre.
        title: título de la ventana.
        fields_config: diccionario con la configuración de los campos.
        generate_prompt_fn: función que recibe un diccionario de parámetros y devuelve el prompt.
        """
        self.master = master
        self.fields_config = fields_config
        self.generate_prompt_fn = generate_prompt_fn
        self.widgets = {}  # Almacenará referencias a los widgets para cada campo.
        self.window = Toplevel(master)
        self.window.title(title)
        self.window.geometry("800x800")
        self.setup_widgets()

    def setup_widgets(self):
        # Configurar las columnas para que sean responsivas
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=3)

        row = 0
        for field_key, field_data in self.fields_config.items():
            # Etiqueta del campo
            label_text = field_data.get("label", field_key)
            tk.Label(self.window, text=f"{label_text}:").grid(row=row, column=0, sticky="e", padx=5, pady=5)

            widget_type = field_data.get("type", "entry")
            if widget_type == "entry":
                entry_widget = tk.Entry(self.window)
                entry_widget.grid(row=row, column=1, sticky="ew", padx=5, pady=5)
                default_val = field_data.get("default", "")
                entry_widget.insert(0, default_val)
                self.widgets[field_key] = entry_widget
            elif widget_type == "optionmenu":
                options = field_data.get("options", [])
                var = tk.StringVar(self.window)
                default_val = field_data.get("default", options[0] if options else "")
                var.set(default_val)
                tk.OptionMenu(self.window, var, *options).grid(row=row, column=1, sticky="ew", padx=5, pady=5)
                self.widgets[field_key] = var
            else:
                # Si se necesita otro tipo de widget se puede ampliar aquí
                pass
            row += 1

        # Botón para generar el prompt
        tk.Button(self.window, text="Generar Prompt", command=self.submit_prompt)\
            .grid(row=row, column=0, columnspan=2, pady=10, sticky="ew")

        # Hacer que las filas se expandan de manera responsiva
        for i in range(row+1):
            self.window.grid_rowconfigure(i, weight=1)

    def submit_prompt(self):
        params = {}
        for key, widget in self.widgets.items():
            field_data = self.fields_config.get(key, {})
            widget_type = field_data.get("type", "entry")
            if widget_type == "entry":
                value = widget.get()
            elif widget_type == "optionmenu":
                value = widget.get()
            else:
                value = widget.get()  # Por defecto
            # Si se requiere conversión, se aplica la función de casting
            cast_fn = field_data.get("cast", None)
            if cast_fn is not None:
                try:
                    value = cast_fn(value)
                except Exception as e:
                    messagebox.showerror("Error", f"Error en el campo '{key}': {e}")
                    return
            params[key] = value

        # Generar el prompt usando la función suministrada
        prompt_text = self.generate_prompt_fn(params)
        self.display_prompt(prompt_text)

    def display_prompt(self, prompt_text):
        # Muestra el prompt generado en una nueva ventana
        display_window = Toplevel(self.window)
        display_window.title("Prompt Generado")
        prompt_display = tk.Text(display_window, wrap='word', width=60, height=20)
        prompt_display.insert('1.0', prompt_text)
        prompt_display.config(state='disabled')
        prompt_display.pack(expand=True, fill='both', padx=10, pady=10)
