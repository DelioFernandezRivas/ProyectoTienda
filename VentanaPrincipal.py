from gi.repository import Gtk
import sqlite3


class VentanaInicio(Gtk.Window):




#Esta sin terminar:


    def __init__(self):
        Gtk.Window.__init__(self,title="DelioGestor v1.0")
        self.set_border_width(0)
        self.set_size_request(1,1)


        #Creacion de cajas y tablas
        Caja1= Gtk.Box()
        Caja1.set_orientation(Gtk.Orientation.HORIZONTAL)
        Tabla = Gtk.Table()
        Tabla2 = Gtk.Table(5, 5, False)
        Tabla.set_size_request(5,5)

        #Tamaños para las imagenes



        # Creamos los objetos necesarios para la ventana



        #LabelPrincipal= Gtk.Label("El Warherdeliom")

        Imagen1=Gtk.Image()

        Imagen1.set_from_file("/home/local/DANIELCASTELAO/dfernandezrivas/PycharmProjects/ProyectoTienda/Cadiansmaspequeño.jpg")

        Imagen2=Gtk.Image()
        Imagen2.set_from_file("/home/local/DANIELCASTELAO/dfernandezrivas/PycharmProjects/ProyectoTienda/Tempestor_Prime_Whitelock_50th_Kappic_Eagles.png")

        Imagen3= Gtk.Image()
        Imagen3.set_from_file("/home/local/DANIELCASTELAO/dfernandezrivas/PycharmProjects/ProyectoTienda/50375_1155658124_large.jpg")


        Imagen4 = Gtk.Image()
        Imagen4.set_from_file("/home/local/DANIELCASTELAO/dfernandezrivas/PycharmProjects/ProyectoTienda/latest.jpg")

        labelprueva = Gtk.Label()

        Boton1 = Gtk.Button("Gestion de Clientes")
        Boton2 = Gtk.Button("Gestion de Productos")
        Boton3 = Gtk.Button("Gestion Trabajadores")
        Boton4 = Gtk.Button("Salir de DelioGestor ")





            #if Boton1.set_focus_on_click:

            #Ventanaprincipal2.show_all

        # Creamos las conecsiones
        Boton1.connect("clicked", self.do_clicked)
        Boton2.connect("clicked", self.do_clicked2)
        Boton3.connect("clicked", self.do_clicked3)
        Boton4.connect("clicked", Gtk.main_quit)
        #Boton1.connect("clicked", Ventanaprincipal2)
        #Boton2.connect("clicked",Ventanaprincipal3)




        # Añadimos la tabla, le damos la orientacion yespaciados y la hacemos homogenea
        Caja1.add(Tabla)
        Caja1.set_orientation(Gtk.Orientation.VERTICAL)
        #Tabla.set_row_spacings(25)
        #Tabla.set_col_spacings(25)
        #Tabla.set_homogeneous(True)


        # Damos las posiciones a los objetos


        #Tabla.attach(LabelPrincipal,2,3,0,1)

        Tabla.attach(Imagen1, 0, 1, 1,2)

        Tabla.attach(Imagen2, 2, 3, 1, 2)

        Tabla.attach(Imagen3, 3, 4, 1, 2)

        Tabla.attach(Imagen4,5, 6, 1, 2)

        #Tabla.attach(LabelPrincipal,2, 4, 0, 1)

        Tabla.attach(Boton1, 0, 1, 2, 3)

        Tabla.attach(Boton2, 2, 3 , 2, 3)

        Tabla.attach(Boton3, 3, 4, 2,3 )

        Tabla.attach(Boton4, 5, 6, 2,3 )


        # Añadimos la caja al self y mostramos todo
        self.add(Caja1)
        self.show_all()


    def do_clicked(self,Ventana1):
        VentanaGestionClientes()
        self.set_visible(False)
    def do_clicked2(self,Ventana2):
        VentanaGestionProductos()
        self.set_visible(False)
    def do_clicked3(self,Ventana3):
        VentanaGestionTrabajadores()
        self.set_visible(False)

class VentanaGestionClientes(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="El Warherdeliom")
        self.set_border_width(0)
        # Creacion de cajas y tablas
        Caja1 = Gtk.Box()
        Caja1.set_orientation(Gtk.Orientation.HORIZONTAL)
        Tabla = Gtk.Table(5, 5, False)
        Tabla2 = Gtk.Table(5, 5, False)

        # Creamos los objetos necesarios para la ventana

        NombreVentana = Gtk.Label("Ingreso de Clientes")

        DNI = Gtk.Entry()
        DNI2 = Gtk.Label("DNI:")

        Nombre = Gtk.Entry()
        Nombre2 = Gtk.Label("Nombre:")

        Apellidos = Gtk.Entry()
        Apellidos2 = Gtk.Label("Apellidos:")

        NumeroTelefono = Gtk.Entry()
        NumeroTelefono2 = Gtk.Label("Numero de Teléfono:")

        Pedidos = Gtk.Entry()
        Pedidos2 = Gtk.Label("Pedidos:")

        Boton1 = Gtk.Button("Salir")
        Boton2 = Gtk.Button("Borrar ingreso")
        Boton3 = Gtk.Button("Aceptar")
        Boton4 = Gtk.Button("Ver Clientes")
        Boton5 = Gtk.Button("Volver al menu")

        # Creamos las conecsiones

        Boton1.connect("clicked", Gtk.main_quit)
        Boton5.connect("clicked", self.do_clicked)

        TextoBoton1 = Gtk.Label("Este label cambia")

        # Añadimos la tabla, le damos la orientacion yespaciados y la hacemos homogenea
        Caja1.add(Tabla)
        Caja1.set_orientation(Gtk.Orientation.VERTICAL)
        Tabla.set_row_spacings(25)
        Tabla.set_col_spacings(25)
        Tabla.set_homogeneous(True)

        # Damos las posiciones a los objetos

        Tabla.attach(NombreVentana, 2, 4, 0, 1)

        Tabla.attach(DNI2, 0, 1, 1, 2)
        Tabla.attach(DNI, 1, 2, 1, 2)

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

        Tabla.attach(Boton4, 5, 6, 1, 2)

        Tabla.attach(Boton5, 2, 3, 7, 8)

        # Añadimos la caja al self y mostramos todo
        self.add(Caja1)
        self.show_all()

    def do_clicked(self, Ventana1):
            VentanaInicio()
            self.set_visible(False)

    def do_clicked2(self, Ventana2):
            VentanaGestionProductos()
            self.set_visible(False)

    def do_clicked3(self, Ventana3):
            VentanaGestionTrabajadores()
            self.set_visible(False)


class VentanaGestionProductos(Gtk.Window):
            # Esta sin terminar:


            def __init__(self):
                Gtk.Window.__init__(self, title="DelioGestor v1.0")
                # Creacion de cajas y tablas
                Caja1 = Gtk.Box()
                Caja1.set_orientation(Gtk.Orientation.HORIZONTAL)
                Tabla = Gtk.Table(5, 5, False)
                Tabla2 = Gtk.Table(5, 5, False)

                DNI = Gtk.Entry()
                DNI2 = Gtk.Label("DNI:")

                Nombre = Gtk.Entry()
                Nombre2 = Gtk.Label("Nombre:")

                Apellidos = Gtk.Entry()
                Apellidos2 = Gtk.Label("Apellidos:")

                NumeroTelefono = Gtk.Entry()
                NumeroTelefono2 = Gtk.Label("Numero de Teléfono:")

                Pedidos = Gtk.Entry()
                Pedidos2 = Gtk.Label("Pedidos:")

                Boton1 = Gtk.Button("Salir")
                Boton2 = Gtk.Button("Borrar ingreso")
                Boton3 = Gtk.Button("Aceptar")
                Boton4 = Gtk.Button("Ver Clientes")
                Boton5 = Gtk.Button("Volver al menu")

                # Creamos las conecsiones

                Boton1.connect("clicked", Gtk.main_quit)

                # Añadimos la tabla, le damos la orientacion yespaciados y la hacemos homogenea
                Caja1.add(Tabla)
                Caja1.set_orientation(Gtk.Orientation.VERTICAL)
                Tabla.set_row_spacings(25)
                Tabla.set_col_spacings(25)
                Tabla.set_homogeneous(True)
                Tabla.attach(DNI2, 0, 1, 1, 2)
                Tabla.attach(DNI, 1, 2, 1, 2)

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

                Tabla.attach(Boton4, 5, 6, 1, 2)

                Tabla.attach(Boton5, 2, 3, 7, 8)

                # Añadimos la caja al self y mostramos todo
                self.add(Caja1)
                self.show_all()

class GestionTrabajadores(Gtk.Window):
        def __init__(self):
                    Gtk.Window.__init__(self, title="El Warherdeliom")
                    self.set_border_width(0)
                    # Creacion de cajas y tablas
                    Caja1 = Gtk.Box()
                    Caja1.set_orientation(Gtk.Orientation.HORIZONTAL)
                    Tabla = Gtk.Table(5, 5, False)
                    Tabla2 = Gtk.Table(5, 5, False)

                    # Creamos los objetos necesarios para la ventana

                    NombreVentana = Gtk.Label("Ingreso de Clientes")

                    DNI = Gtk.Entry()
                    DNI2 = Gtk.Label("DNI:")

                    Nombre = Gtk.Entry()
                    Nombre2 = Gtk.Label("Nombre:")

                    Apellidos = Gtk.Entry()
                    Apellidos2 = Gtk.Label("Apellidos:")

                    NumeroTelefono = Gtk.Entry()
                    NumeroTelefono2 = Gtk.Label("Numero de Teléfono:")

                    Pedidos = Gtk.Entry()
                    Pedidos2 = Gtk.Label("Pedidos:")

                    Boton1 = Gtk.Button("Salir")
                    Boton2 = Gtk.Button("Borrar ingreso")
                    Boton3 = Gtk.Button("Aceptar")
                    Boton4 = Gtk.Button("Ver Clientes")
                    Boton5 = Gtk.Button("Volver al menu")

                    # Creamos las conecsiones



                    # Añadimos la tabla, le damos la orientacion yespaciados y la hacemos homogenea
                    Caja1.add(Tabla)
                    Caja1.set_orientation(Gtk.Orientation.VERTICAL)
                    Tabla.set_row_spacings(25)
                    Tabla.set_col_spacings(25)
                    Tabla.set_homogeneous(True)

                    Tabla.attach(NombreVentana, 2, 4, 0, 1)

                    Tabla.attach(DNI2, 0, 1, 1, 2)
                    Tabla.attach(DNI, 1, 2, 1, 2)

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

                    Tabla.attach(Boton4, 5, 6, 1, 2)

                    Tabla.attach(Boton5, 2, 3, 7, 8)

                    # Añadimos la caja al self y mostramos todo
                    self.add(Caja1)
                    self.show_all()

class VentanaGestionTrabajadores(Gtk.Window):
            def __init__(self):
                Gtk.Window.__init__(self, title="DelioGestor v1.0")
                # Creacion de cajas y tablas
                Caja1 = Gtk.Box()
                Caja1.set_orientation(Gtk.Orientation.HORIZONTAL)
                Tabla = Gtk.Table(5, 5, False)
                Tabla2 = Gtk.Table(5, 5, False)

                DNI = Gtk.Entry()
                DNI2 = Gtk.Label("DNI:")

                Nombre = Gtk.Entry()
                Nombre2 = Gtk.Label("Nombre:")

                Apellidos = Gtk.Entry()
                Apellidos2 = Gtk.Label("Apellidos:")

                NumeroTelefono = Gtk.Entry()
                NumeroTelefono2 = Gtk.Label("Numero de Teléfono:")

                Pedidos = Gtk.Entry()
                Pedidos2 = Gtk.Label("Pedidos:")

                Boton1 = Gtk.Button("Salir")
                Boton2 = Gtk.Button("Borrar ingreso")
                Boton3 = Gtk.Button("Aceptar")
                Boton4 = Gtk.Button("Ver Clientes")
                Boton5 = Gtk.Button("Volver al menu")

                # Creamos las conecsiones

                Boton1.connect("clicked", Gtk.main_quit)

                # Añadimos la tabla, le damos la orientacion y espaciados y la hacemos homogenea
                Caja1.add(Tabla)
                Caja1.set_orientation(Gtk.Orientation.VERTICAL)
                Tabla.set_row_spacings(25)
                Tabla.set_col_spacings(25)
                Tabla.set_homogeneous(True)
                Tabla.attach(DNI2, 0, 1, 1, 2)
                Tabla.attach(DNI, 1, 2, 1, 2)

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

                Tabla.attach(Boton4, 5, 6, 1, 2)

                Tabla.attach(Boton5, 2, 3, 7, 8)

                # Añadimos la caja al self y mostramos todo
                self.add(Caja1)
                self.show_all()



# Realizamos el correspondiente if
if __name__ == "__main__":
     VentanaInicio()
     Gtk.main()
