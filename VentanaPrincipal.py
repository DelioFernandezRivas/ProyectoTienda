from gi.repository import Gtk
import sqlite3

class Ventanaprincipal(Gtk.Window):



#Esta sin terminar:


    def __init__(self):
        Gtk.Window.__init__(self,title="El Warherdeliom")
        self.set_border_width(0)
        #Creacion de cajas y tablas
        Caja1= Gtk.Box()
        Caja1.set_orientation(Gtk.Orientation.HORIZONTAL)
        Tabla = Gtk.Table(5, 5, False)
        Tabla2 = Gtk.Table(5, 5, False)


        # Creamos los objetos necesarios para la ventana

        Boton1 = Gtk.Button("")
        Boton2 = Gtk.Button("")
        Boton3 = Gtk.Button("")
        Boton4 = Gtk.Button("")
        Boton5 = Gtk.Button("")

        # Creamos las conecsiones

        Boton1.connect("clicked", Gtk.main_quit)

        # Añadimos la tabla, le damos la orientacion yespaciados y la hacemos homogenea
        Caja1.add(Tabla)
        Caja1.set_orientation(Gtk.Orientation.VERTICAL)
        Tabla.set_row_spacings(25)
        Tabla.set_col_spacings(25)
        Tabla.set_homogeneous(True)


        # Damos las posiciones a los objetos

        Tabla.attach(Boton1, 0, 1, 7, 8)

        Tabla.attach(Boton2, 3, 4, 7, 8)

        Tabla.attach(Boton3, 5, 6, 7, 8)

        Tabla.attach(Boton4, 5, 6, 1, 2)

        Tabla.attach(Boton5, 2, 3, 7, 8)

        # Añadimos la caja al self y mostramos todo
        self.add(Caja1)
        self.show_all()

# Realizamos el correspondiente if
if __name__ == "__main__":
     Ventanaprincipal()
     Gtk.main()
