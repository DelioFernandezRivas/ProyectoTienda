from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle

import VentanaPrincipal
import gi

gi.require_version("Gtk","3.0")
from gi.repository import Gtk
import Base as dbm
from reportlab.platypus import Table, SimpleDocTemplate, Paragraph, PageBreak
from reportlab.lib import colors



class VisorTablas(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="Ejemplo de TreeView")
        self.set_default_size(400,800)
        self.set_border_width(20)
        self.set_position(Gtk.WindowPosition.CENTER)

        #Inicializamos la conexion con la bd
        self.db = dbm.DBManager
        self.db.__init__(self.db, "BaseProyecto.db")


    #Creamos un box como layout principal
        box = Gtk.Box()
        box.set_orientation(Gtk.Orientation.VERTICAL)
        box.set_halign(Gtk.Align.CENTER)

    #Creamos el notebook que contrendra cada tabla y lo añadimos a la ventana
        notebook = Gtk.Notebook()
        box.add(notebook)

        listaTabla = self.db.consultarNombreTablas(self.db)
        for x in listaTabla:
            print(x)
            nombreTabla=x
        #coge los nombres de las columnas de la tabla
            columnas = self.db.columnas(self.db,nombreTabla)
        #coge los valores de cada fila
            agenda = self.db.valores(self.db,nombreTabla)
        #coge el tipo de dato de la columna
            ct= self.db.columnasTipo(self.db,nombreTabla)

        #Este metodo si que vale para cualquier tabla

            modelo = Gtk.ListStore.new(ct)

            for persona  in agenda:
                modelo.append(persona)

            vista = Gtk.TreeView(model=modelo, enable_search=False)
            for i in range(len(columnas)):
                celda = Gtk.CellRendererText(editable=True)
                columna = Gtk.TreeViewColumn(columnas[i], celda, text=i)
                # Para poder usar ciertos valores, como la columna o el nombre hay que pasarselos al metodo
                celda.connect("edited", self.on_celda_edited, modelo, i, columnas[i], nombreTabla)
                vista.append_column(columna)

            vista.connect("key_press_event", self.borrarFila, nombreTabla)

            cajaH = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
            cajaH.pack_start(vista, False, False, 0)

            # boton insertar
            boton_insertar = Gtk.Button("nueva fila")
            boton_insertar.connect("clicked", self.insertar, nombreTabla)

            cajaH.add(boton_insertar)

            notebook.append_page(cajaH, Gtk.Label(nombreTabla))

            boton_print = Gtk.Button("Imprimir PDF")
            boton_print.connect("clicked", self.printTabla, nombreTabla)
            cajaH.add(boton_print)
        # añado botones salir/volver al login

        boton_volver = Gtk.Button("Volver")
        boton_salir = Gtk.Button("Salir")

        boton_volver.connect("clicked", self.volver)
        boton_salir.connect("clicked", Gtk.main_quit)

        box.add(boton_volver)
        box.add(boton_salir)

        self.add(box)
        self.connect("delete_event", Gtk.main_quit)
        self.show_all()


if __name__=="__main__":
    VisorTablas()
    Gtk.main()



