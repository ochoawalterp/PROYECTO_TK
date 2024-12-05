from tkinter import messagebox
from app.servicio_tarea import ServicioTarea
from form.registro_form_desing import FormularioRegistroDesign

class FormularioRegistro(FormularioRegistroDesign):
    def __init__(self):
        self.servicio_tarea = ServicioTarea()
        super().__init__()
    

    def registrar_tarea(self):
        nombre = self.campo_nombre.get()
        dia = self.campo_dia.get()

        if not nombre or not dia:
            messagebox.showerror(
                "Error", "Por favor Ingrese el nombre y La cantidad de dias que te llevara la tarea"
            )
            return

        try:
            self.servicio_tarea.registro(nombre, dia)
            messagebox.showinfo("Exito", "Tarea Registrada correctamente")
            self.actualizar_lista()
            self.limpiar_campos()
        except Exception as e:
            messagebox.showerror(
                "Error", f"No se pudo registrar tarea la tarea {e}"
            )



    def actualizar_lista(self):
        registros = self.tree.get_children()
        for registro in registros:
            self.tree.delete(registro)
        tareas = self.servicio_tarea.obtener_tareas()

        for ref, tarea in enumerate(tareas):
            color =('evenrow',) if ref % 2 else ('oddrow',) 
            self.tree.insert(parent="", index=ref, iid=ref, text="", tags=color, values=(
                tarea.id, tarea.nombre, tarea.dia))
            
    
    def al_seleccionar_treeview(self, event):


        seleccion = event.widget.selection()
        if seleccion:
            item = event.widget.item(seleccion[0], 'values')
            if item:
                self.limpiar_campos()
                self.campo_id.config(state="normal")
                self.campo_id.insert(0, item[0])
                self.campo_id.config(state="readonly")
                self.campo_nombre.insert(0,item[1])
                self.campo_dia.insert(0, item[2])
                self.btn_eliminar.pack(**self.obtener_conf_btn_pack())
                self.btn_modificar.pack(**self.obtener_conf_btn_pack())
                self.btn_registro.pack_forget()


    def modificar_tarea(self):
        try:
            id = self.tree.item(self.tree.selection())["values"][0]
            nombre  = self.campo_nombre.get()
            dia = self.campo_dia.get()
            self.servicio_tarea.modificar(nombre,dia,id)
            self.limpiar_campos()
            self.actualizar_lista()
        except IndexError as e:
            messagebox.showerror(
                "Error", f"Por favor selecciona una fila: {e}"
            )

    def  eliminar_tarea(self):
        try:
            id = self.tree.item(self.tree.selection())["values"][0]
            self.servicio_tarea.eliminar_tareas(id)
            self.actualizar_lista()
            self.limpiar_campos()

        except IndexError as e:
            messagebox.showerror(
                "Error", f"Por favor selecciona una fila: {e}"
            )
