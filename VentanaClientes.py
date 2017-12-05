from gi.repository import Gtk
import sqlite3

class Ventanaprincipal(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self,title="El Warherdeliom")
        self.set_border_width(0)
        #Creacion de cajas y tablas
        Caja1= Gtk.Box()
        Caja1.set_orientation(Gtk.Orientation.HORIZONTAL)
        Tabla = Gtk.Table(5, 5, False)
        Tabla2 = Gtk.Table(5, 5, False)

        #Creamos los objetos necesarios para la ventana

        NombreVentana = Gtk.Label("Ingreso de Clientes")


        DNI= Gtk.Entry()
        DNI2= Gtk.Label("DNI:")

        Nombre = Gtk.Entry()
        Nombre2 = Gtk.Label("Nombre:")

        Apellidos= Gtk.Entry()
        Apellidos2= Gtk.Label("Apellidos:")

        NumeroTelefono= Gtk.Entry()
        NumeroTelefono2 = Gtk.Label("Numero de Teléfono:")

        Pedidos=Gtk.Entry()
        Pedidos2= Gtk.Label("Pedidos:")



        Boton1 = Gtk.Button("Salir")
        Boton2 = Gtk.Button("Borrar ingreso")
        Boton3 = Gtk.Button("Aceptar")
        Boton4= Gtk.Button("Ver Clientes")
        Boton5 = Gtk.Button("Volver al menu")





        #Creamos las conecsiones

        Boton1.connect("clicked", Gtk.main_quit)




        TextoBoton1 = Gtk.Label("Este label cambia")

        #Añadimos la tabla, le damos la orientacion yespaciados y la hacemos homogenea
        Caja1.add(Tabla)
        Caja1.set_orientation(Gtk.Orientation.VERTICAL)
        Tabla.set_row_spacings(25)
        Tabla.set_col_spacings(25)
        Tabla.set_homogeneous(True)

        #Damos las posiciones a los objetos
        
        Tabla.attach(NombreVentana, 2 , 4, 0 , 1)

        Tabla.attach(DNI2, 0, 1, 1, 2)
        Tabla.attach(DNI,1,2,1,2)

        Tabla.attach(Nombre2, 0, 1, 2, 3)
        Tabla.attach(Nombre, 1, 2, 2, 3)

        Tabla.attach(Apellidos2, 0, 1, 3, 4)
        Tabla.attach(Apellidos, 1, 2, 3, 4)

        Tabla.attach(NumeroTelefono2, 0, 1, 4, 5)
        Tabla.attach(NumeroTelefono, 1, 2, 4, 5)

        Tabla.attach(Pedidos2, 0, 1, 5, 6)
        Tabla.attach(Pedidos, 1, 2, 5, 6)

        Tabla.attach(Boton1, 0, 1, 7, 8)

        Tabla.attach(Boton2, 3, 4, 7, 8)

        Tabla.attach(Boton3, 5, 6, 7, 8)

        Tabla.attach(Boton4, 5,6,1,2)

        Tabla.attach(Boton5, 2,3,7,8)



        #Añadimos la caja al self y mostramos todo
        self.add(Caja1)
        self.show_all()





#Realizamos el correspondiente if
if __name__=="__main__":
  Ventanaprincipal()
  Gtk.main()
