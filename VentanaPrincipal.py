import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
import sqlite3


#Creamos las listas:
#Lista prodcutos con 5 datos: Identificador,Nombre,precio,tipo
store = Gtk.ListStore(str, str, int,str)
Listaproductos = [
("VDE5","Figura1",65,"WarhammerType"),
("VAD3","Figura2",32,"Warhammer40Type"),
("HYH5","MaquetaTank1",48,"TanksWII"),
("ACE2","Pinturas1",67,"PinturasType"),
("HTR5", "Figura3",21,"WarhammerType"),
]

treeView = Gtk.TreeView(Listaproductos)
cellRenderer = Gtk.CellRendererText()
column = Gtk.TreeViewColumn("Title", renderer, text=0)


class VentanaInicio(Gtk.Window):




#Esta sin terminar:


    def __init__(self):
        Gtk.Window.__init__(self,title="DelioGestor v1.0")
        self.set_position(Gtk.WindowPosition.CENTER)
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

        Imagen1.set_from_file("Cadiansmaspequeño.jpg")

        Imagen2=Gtk.Image()
        Imagen2.set_from_file("Tempestor_Prime_Whitelock_50th_Kappic_Eagles.png")

        Imagen3= Gtk.Image()
        Imagen3.set_from_file("50375_1155658124_large.jpg")


        Imagen4 = Gtk.Image()
        Imagen4.set_from_file("latest.jpg")

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

        Gtk.Window.__init__(self, title="DelioGestor v1.0")
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_border_width(0)
        # Creacion de cajas y tablas
        Caja1 = Gtk.Box()
        Caja1.set_orientation(Gtk.Orientation.HORIZONTAL)
        Tabla = Gtk.Table(5, 5, False)
        Tabla2 = Gtk.Table(5, 5, False)

        # Creamos los objetos necesarios para la ventana

        NombreVentana = Gtk.Label("Ingreso de Clientes")

        self.DNI = Gtk.Entry()
        self.DNI2 = Gtk.Label("DNI:")

        self.Nombre = Gtk.Entry()
        self.Nombre2 = Gtk.Label("Nombre:")

        self.Apellidos = Gtk.Entry()
        self.Apellidos2 = Gtk.Label("Apellidos:")

        self.NumeroTelefono = Gtk.Entry()
        self.NumeroTelefono2 = Gtk.Label("Numero de Teléfono:")

        self.Pedidos = Gtk.Entry()
        self.Pedidos2 = Gtk.Label("Pedidos:")

        self.Boton1 = Gtk.Button("Salir")
        self.Boton2 = Gtk.Button("Borrar")
        self.Boton3 = Gtk.Button("Aceptar")
        self.Boton5 = Gtk.Button("Volver al menu")

        # Creamos las conecsiones

        self.Boton1.connect("clicked", Gtk.main_quit)
        self.Boton5.connect("clicked", self.do_clicked)
        self.Boton2.connect("clicked", self.do_clicked4)
        self.Boton3.connect("clicked", self.do_clicked5)

        TextoBoton1 = Gtk.Label("Este label cambia")

        # Añadimos la tabla, le damos la orientacion yespaciados y la hacemos homogenea
        Caja1.add(Tabla)
        Caja1.set_orientation(Gtk.Orientation.VERTICAL)
        Tabla.set_row_spacings(25)
        Tabla.set_col_spacings(25)
        Tabla.set_homogeneous(True)

        # Damos las posiciones a los objetos

        Tabla.attach(NombreVentana, 2, 4, 0, 1)

        Tabla.attach(self.DNI2, 0, 1, 1, 2)
        Tabla.attach(self.DNI, 1, 2, 1, 2)

        Tabla.attach(self.Nombre2, 0, 1, 2, 3)
        Tabla.attach(self.Nombre, 1, 2, 2, 3)

        Tabla.attach(self.Apellidos2, 0, 1, 3, 4)
        Tabla.attach(self.Apellidos, 1, 2, 3, 4)

        Tabla.attach(self.NumeroTelefono2, 0, 1, 4, 5)
        Tabla.attach(self.NumeroTelefono, 1, 2, 4, 5)

        Tabla.attach(self.Pedidos2, 0, 1, 5, 6)
        Tabla.attach(self.Pedidos, 1, 2, 5, 6)

        Tabla.attach(self.Boton1, 0, 1, 7, 8)

        Tabla.attach(self.Boton2, 3, 4, 7, 8)

        Tabla.attach(self.Boton3, 5, 6, 7, 8)

        Tabla.attach(self.Boton5, 2, 3, 7, 8)

        # Añadimos la caja al self y mostramos todo
        self.add(Caja1)
        self.show_all()
#Vamos unidendo las ventanas con estos metodos y creando otros metodos necesarios
    def do_clicked(self, Ventana1):
            VentanaInicio()
            self.set_visible(False)
            self.set_position(Gtk.WindowPosition.CENTER)
    def do_clicked2(self, Ventana2):
            VentanaGestionProductos()
            self.set_visible(False)
            self.set_position(Gtk.WindowPosition.CENTER)
    def do_clicked3(self, Ventana3):
            VentanaGestionTrabajadores()
            self.set_visible(False)
            self.set_position(Gtk.WindowPosition.CENTER)
    def do_clicked4(self,Ventana4):
            self.DNI.set_text("")
            self.Nombre.set_text("")
            self.Apellidos.set_text("")
            self.NumeroTelefono.set_text("")
            self.Pedidos.set_text("")
    def do_clicked5(self, Ventana4):
        self.Ventanasalida=Gtk.Window()
        Cajaventana=Gtk.Box()
        self.Ventanasalida.add(Cajaventana)
        Tablaventana=Gtk.Table()
        Tablaventana.set_homogeneous(True)
        BotonAceptar = Gtk.Button("Aceptar")
        LabelVentanasalida = Gtk.Label("Se a Añadido con exito")
        Tablaventana.attach(BotonAceptar, 1,2, 1, 2)
        Tablaventana.attach(LabelVentanasalida, 0, 3, 0, 1)
        Cajaventana.add(Tablaventana)
        BotonAceptar.connect("clicked",self.do_clicked6)
        self.Ventanasalida.show_all()
    def do_clicked6(self,Ventana6):
        self.Ventanasalida.set_visible(False)


class VentanaGestionProductos(Gtk.Window):
            # Esta sin terminar:


            def __init__(self):

                Gtk.Window.__init__(self, title="DelioGestor v1.0")
                self.set_position(Gtk.WindowPosition.CENTER)
                # Creacion de cajas y tablas
                Caja1 = Gtk.Box()
                Caja1.set_orientation(Gtk.Orientation.HORIZONTAL)
                Tabla = Gtk.Table(5, 5, False)
                Tabla2 = Gtk.Table(5, 5, False)
                NombreVentana = Gtk.Label("Ingreso Productos")

                self.Identificador = Gtk.Entry()
                self.Identificador2 = Gtk.Label("Identificador:")

                self.Nombre = Gtk.Entry()
                self.Nombre2 = Gtk.Label("Nombre:")

                self.Precio = Gtk.Entry()
                self.Precio2 = Gtk.Label("Precio:")

                self.Tipo = Gtk.Entry()
                self.Tipo2= Gtk.Label("Tipo:")

                self.Boton1 = Gtk.Button("Salir")
                self.Boton2 = Gtk.Button("Borrar")
                self.Boton3 = Gtk.Button("Aceptar")
                self.Boton5 = Gtk.Button("Volver al menu")

                # Creamos las conecsiones

                self.Boton1.connect("clicked", Gtk.main_quit)
                self.Boton5.connect("clicked", self.do_clicked)
                self.Boton2.connect("clicked", self.do_clicked5)
                self.Boton3.connect("clicked", self.do_clicked6)

                # Añadimos la tabla, le damos la orientacion yespaciados y la hacemos homogenea
                Caja1.add(Tabla)
                Caja1.set_orientation(Gtk.Orientation.VERTICAL)
                Tabla.set_row_spacings(25)
                Tabla.set_col_spacings(25)
                Tabla.set_homogeneous(True)

                Tabla.attach(NombreVentana, 2, 4, 0, 1)

                Tabla.attach(self.Identificador2, 0, 1, 1, 2)
                Tabla.attach(self.Identificador, 1, 2, 1, 2)

                Tabla.attach(self.Nombre2, 0, 1, 2, 3)
                Tabla.attach(self.Nombre, 1, 2, 2, 3)

                Tabla.attach(self.Precio2, 0, 1, 3, 4)
                Tabla.attach(self.Precio, 1, 2, 3, 4)

                Tabla.attach(self.Tipo2, 0, 1, 4, 5)
                Tabla.attach(self.Tipo, 1, 2, 4, 5)

                Tabla.attach(self.Boton1, 0, 1, 7, 8)

                Tabla.attach(self.Boton2, 3, 4, 7, 8)

                Tabla.attach(self.Boton3, 5, 6, 7, 8)

                Tabla.attach(self.Boton5, 2, 3, 7, 8)

                # Añadimos la caja al self y mostramos todo
                self.add(Caja1)
                self.show_all()

            def do_clicked(self, Ventana1):
                    VentanaInicio()
                    self.set_visible(False)
                    self.set_position(Gtk.WindowPosition.CENTER)

            def do_clicked2(self, Ventana2):
                    VentanaGestionProductos()
                    self.set_visible(False)
                    self.set_position(Gtk.WindowPosition.CENTER)

            def do_clicked3(self, Ventana3):
                    VentanaGestionTrabajadores()
                    self.set_visible(False)
                    self.set_position(Gtk.WindowPosition.CENTER)

            #def do_clicked4(self, Ventana4):
                #VentanaverProductos()
                #self.set_visible(False)
                #self.set_position(Gtk.WindowPosition.CENTER)

            def do_clicked5(self, Ventana4):
                    self.Identificador.set_text("")
                    self.Nombre.set_text("")
                    self.Precio.set_text("")
                    self.Tipo.set_text("")

            def do_clicked6(self, Ventana4):
                self.Ventanasalida = Gtk.Window()
                Cajaventana = Gtk.Box()
                self.Ventanasalida.add(Cajaventana)
                Tablaventana = Gtk.Table()
                Tablaventana.set_homogeneous(True)
                BotonAceptar = Gtk.Button("Aceptar")
                LabelVentanasalida = Gtk.Label("Se a Añadido con exito")
                Tablaventana.attach(BotonAceptar, 1, 2, 1, 2)
                Tablaventana.attach(LabelVentanasalida, 0, 3, 0, 1)
                Cajaventana.add(Tablaventana)
                BotonAceptar.connect("clicked", self.do_clicked7)
                self.Ventanasalida.show_all()

            def do_clicked7(self, Ventana6):
                self.Ventanasalida.set_visible(False)



class VentanaGestionTrabajadores(Gtk.Window):
            def __init__(self):

                Gtk.Window.__init__(self, title="DelioGestor v1.0")
                self.set_position(Gtk.WindowPosition.CENTER)
                # Creacion de cajas y tablas
                Caja1 = Gtk.Box()
                Caja1.set_orientation(Gtk.Orientation.HORIZONTAL)
                Tabla = Gtk.Table(5, 5, False)
                NombreVentana = Gtk.Label("Ingreso Trabajadores")

                self.DNI = Gtk.Entry()
                self.DNI2 = Gtk.Label("DNI:")

                self.Nombre = Gtk.Entry()
                self.Nombre2 = Gtk.Label("Nombre:")

                self.Apellidos = Gtk.Entry()
                self.Apellidos2 = Gtk.Label("Apellidos:")

                self.NumeroTelefono = Gtk.Entry()
                self.NumeroTelefono2 = Gtk.Label("Numero de Teléfono:")

                self.Direccion = Gtk.Entry()
                self.Direccion2 = Gtk.Label("Direccion:")

                self.Boton1 = Gtk.Button("Salir")
                self.Boton2 = Gtk.Button("Borrar")
                self.Boton3 = Gtk.Button("Aceptar")
                self.Boton5 = Gtk.Button("Volver al menu")

                # Creamos las conecsiones

                self.Boton1.connect("clicked", Gtk.main_quit)
                self.Boton5.connect("clicked", self.do_clicked)
                self.Boton2.connect("clicked", self.do_clicked4)
                self.Boton3.connect("clicked", self.do_clicked5)

                # Añadimos la tabla, le damos la orientacion y espaciados y la hacemos homogenea
                Caja1.add(Tabla)
                Caja1.set_orientation(Gtk.Orientation.VERTICAL)

                Tabla.attach(NombreVentana, 2, 4, 0, 1)

                Tabla.set_row_spacings(25)
                Tabla.set_col_spacings(25)
                Tabla.set_homogeneous(True)

                Tabla.attach(self.DNI2, 0, 1, 1, 2)
                Tabla.attach(self.DNI, 1, 2, 1, 2)

                Tabla.attach(self.Nombre2, 0, 1, 2, 3)
                Tabla.attach(self.Nombre, 1, 2, 2, 3)

                Tabla.attach(self.Apellidos2, 0, 1, 3, 4)
                Tabla.attach(self.Apellidos, 1, 2, 3, 4)

                Tabla.attach(self.NumeroTelefono2, 0, 1, 4, 5)
                Tabla.attach(self.NumeroTelefono, 1, 2, 4, 5)

                Tabla.attach(self.Direccion2, 0, 1, 5, 6)
                Tabla.attach(self.Direccion, 1, 2, 5, 6)

                Tabla.attach(self.Boton1, 0, 1, 7, 8)

                Tabla.attach(self.Boton2, 3, 4, 7, 8)

                Tabla.attach(self.Boton3, 5, 6, 7, 8)


                Tabla.attach(self.Boton5, 2, 3, 7, 8)

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

            def do_clicked4(self, Ventana4):
                    self.DNI.set_text("")
                    self.Nombre.set_text("")
                    self.Apellidos.set_text("")
                    self.NumeroTelefono.set_text("")
                    self.Direccion.set_text("")

            def do_clicked5(self, Ventana4):
                self.Ventanasalida = Gtk.Window()
                Cajaventana = Gtk.Box()
                self.Ventanasalida.add(Cajaventana)
                Tablaventana = Gtk.Table()
                Tablaventana.set_homogeneous(True)
                BotonAceptar = Gtk.Button("Aceptar")
                LabelVentanasalida = Gtk.Label("Se a Añadido con exito")
                Tablaventana.attach(BotonAceptar, 1, 2, 1, 2)
                Tablaventana.attach(LabelVentanasalida, 0, 3, 0, 1)
                Cajaventana.add(Tablaventana)
                BotonAceptar.connect("clicked", self.do_clicked6)
                self.Ventanasalida.show_all()

            def do_clicked6(self, Ventana6):
                self.Ventanasalida.set_visible(False)







# Realizamos el correspondiente if
if __name__ == "__main__":
     VentanaInicio()
     Gtk.main()



#Creamos la base de Datos
conn = sqlite3.connect('Base.')

cursor=conn.cursor()

print("La base de datos se abrio correctamente")
def creartabla(self):

    cursor.execute('''CREATE TABLE tablaproductos(
               DNI VARCHAR(20) PRIMARY   KEY  NOT NULL,
               Nombre    TEXT    NOT NULL,
               Apellidos    INT     NOT NULL,
               NumeroTelefono   BLOB     NOT NULL
               Pedidos  INT NOT NULL)''')

    conn.commit()
    print("Se guardo correctamente ")

def insertar(self):

    cursor.execute("INSERT INTO tablaproductos VALUES(?, ?, ?, ?, ?)")






conn.close()


