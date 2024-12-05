import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import util.util_ventana as util_ventana
# busqueda"#f7f8fa"
#fondo
COLOR_FONDO = "#fff"
COLOR_FONDO_BUSQUEDA = "#dbd7d0"

class FormularioRegistroDesign(tk.Tk):
    def __init__(self): 
        super().__init__()
        self.config_window()
        self.crear_paneles()
        self.crear_controles()
        self.hacer_responsive()

    def config_window(self):
        self.title("Listado De Tareas")
        w, h = 900, 600
        util_ventana.centrar_ventana(self, w, h)
        self.configure(bg=COLOR_FONDO_BUSQUEDA)

    def crear_paneles(self):
        self.marco_titulo = tk.Frame(self, bg="red", height=40)
        self.marco_titulo.pack(side=tk.TOP, fill='x')

        self.marco_registro = tk.Frame(self, bg="#6a7894", height=50)
        self.marco_registro.pack(side=tk.TOP, fill='x', pady=10)

        self.marco_accion = tk.Frame(self, bg="#6a7894", height=50)
        self.marco_accion.pack(side=tk.TOP, fill='x')

        self.marco_tareas = tk.Frame(self, bg="black")
        self.marco_tareas.pack(side=tk.TOP, fill='both', padx=30, pady=15, expand=True)
        
    def crear_controles(self):
        # Título
        title = tk.Label(self.marco_titulo, text="LISTADO DE TAREAS",
                          font=('Roboto', 20), fg="#485159", bg=COLOR_FONDO_BUSQUEDA, pady=20)
        title.pack(expand=True, fill=tk.BOTH)

        # Controles del formulario
        self.marco_registro.columnconfigure(0, weight=1)
        self.marco_registro.columnconfigure(1, weight=2)

        etiqueta_id = tk.Label(self.marco_registro, text='Id:', font=('Times', 14), fg="#666a88", bg=COLOR_FONDO, width=5)
        etiqueta_id.grid(row=0, column=0, padx=5, pady=10, sticky="w")

        self.campo_id = ttk.Entry(self.marco_registro, font=('Times', 14), state="readonly", width=5)
        self.campo_id.grid(row=0, column=1, padx=5, pady=10, sticky="ew")

        etiqueta_nombre = tk.Label(self.marco_registro, text="Tarea:", font=('Times', 14), fg="#666a88", bg=COLOR_FONDO)
        etiqueta_nombre.grid(row=1, column=0, padx=5, pady=10, sticky="w")

        self.campo_nombre = ttk.Entry(self.marco_registro, font=('Times', 14))
        self.campo_nombre.grid(row=1, column=1, padx=5, pady=10, sticky="ew")

        etiqueta_fecha = tk.Label(self.marco_registro, text="Días Aproximados:", font=('Times', 14), fg="#666a88", bg=COLOR_FONDO)
        etiqueta_fecha.grid(row=2, column=0, padx=5, pady=10, sticky="w")

        self.campo_dia = ttk.Entry(self.marco_registro, font=('Times', 14))
        self.campo_dia.grid(row=2, column=1, padx=5, pady=10, sticky="ew")

        self.btn_registro = tk.Button(self.marco_accion, text="Registrar", font=(
            'Times', 13), bg= '#3cb580', bd= 0, fg="#fff", padx=15,command=self.registrar_tarea)
        self.btn_registro.pack(**self.obtener_conf_btn_pack())
        self.btn_registro.bind("<Return>" , (lambda event: self.registrar_tarea))


        self.btn_eliminar = tk.Button(self.marco_accion, text="Eliminar", font=(
            'Times',13), bg ="#b30909", bd=0, fg= "#fff", padx=15, command=self.eliminar_tarea)
        self.btn_eliminar.pack(**self.obtener_conf_btn_pack())
        self.btn_eliminar.bind(
            "<Return>", (lambda event: self.eliminar_tarea())) 
        self.btn_eliminar.pack_forget()

        self.btn_modificar = tk.Button(self.marco_accion, text="Modificar", font=(
            "Times", 13), bg="#d48908", bd=0, fg="#fff", padx=15, command=self.modificar_tarea)
        self.btn_modificar.pack(**self.obtener_conf_btn_pack())
        self.btn_modificar.bind(
            "<Return>", (lambda event: self.modificar_tarea()))
        self.btn_modificar.pack_forget()

        self.btn_limpiar = tk.Button(self.marco_accion, text="Limpiar Campos", font=(
            'Times',13), bg="#8c99ed",bd=0, fg="#fff", padx=15, command=self.limpiar_campos)
        self.btn_limpiar.pack(**self.obtener_conf_btn_pack())
        self.btn_limpiar.bind(
            "<Return>", (lambda event: self.limpiar_campos()))
        
        #tabla
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Treeview", background = "eafbea",
                        foreground ="#000")
        style.configure("Treeview.Heading", background= "#6f9a8d", foreground ="#fff")
        
        #se crea el scroll
        tree_scroll = ttk.Scrollbar(self.marco_tareas)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        #se activa scroll
        self.tree = ttk.Treeview(self.marco_tareas,
                                 show="headings",yscrollcommand=tree_scroll.set)
        

        self.tree['columns'] =('Id', 'Nombre', 'dia')
        self.tree.column("#0")
        self.tree.column('Id')
        self.tree.column('Nombre')
        self.tree.column("dia")
        
        self.tree.heading("#0", text="")
        self .tree.heading("Id", text= 'Id')
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("dia", text="Días a Utilizar")


        self.tree.pack(expand=True, fill='both')
        self.tree.bind("<<TreeviewSelect>>", self.al_seleccionar_treeview)

        self.tree.tag_configure('oddrow', background="#ffffe0")
        self.tree.tag_configure("evenrow",background="#eafbea")

        self.actualizar_lista()

    def actualizar_lista(self):
        pass

    def al_seleccionar_treeview(self, event):
        pass

    def registrar_tarea(self):
        pass
    
    def eliminar_tarea():
        pass

    def modificar_tarea():
        pass

    def obtener_conf_btn_pack(self):
        return{'side': tk.RIGHT,"padx":10, "pady": 10}
    


    def limpiar_campos(self):
        try:
            self.campo_nombre.delete(0,"end")
            self.campo_dia.delete(0,"end")
            self.campo_id.config(state="normal")
            self.campo_id.delete(0,"end")
            self.campo_id.config(state="readonly")
            self.btn_registro.pack(**self.obtener_conf_btn_pack())
            self.btn_eliminar.pack_forget()
            self.btn_modificar.pack_forget()
        except Exception as e:
            messagebox.showerror("Error", f"Error en la limpieza: {e}")


    def hacer_responsive(self):
        # Configurar pesos para que los paneles se expandan
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)

        # Marco tareas como responsivo
        self.marco_tareas.rowconfigure(0, weight=1)
        self.marco_tareas.columnconfigure(0, weight=1)
