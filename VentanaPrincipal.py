#coding=utf-8
import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
import Base as dbm
import cairo

import sys

"""#Creamos las listas:
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
"""

class VentanaInicio(Gtk.Window):






    def __init__(self):
        Gtk.Window.__init__(self,title="DelioGestor v1.0")
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_border_width(0)
        self.set_size_request(1,1)


        self.db = dbm.DBManager
        self.db.__init__(self.db, "BaseProyecto.db")
        #Creacion de cajas y tablas
        Caja = Gtk.Box()
        Caja1= Gtk.Box()
        Caja2 = Gtk.Box()
        Caja3 = Gtk.Box()
        Caja1.set_orientation(Gtk.Orientation.HORIZONTAL)
        TablaPrincipal = Gtk.Table()
        Tabla = Gtk.Table()
        Tabla2 = Gtk.Table(5, 5, False)
        Tabla3 = Gtk.Table()
        Tabla.set_size_request(5,5)

        #Tamaños para las imagenes



        # Creamos los objetos necesarios para la ventana



        #LabelPrincipal= Gtk.Label("El Warherdeliom")

        Imagen1=Gtk.Image()

        Imagen1.set_from_file("location-128.png")


        #Imagen2=Gtk.Image()
        #Imagen2.set_from_file("Tempestor_Prime_Whitelock_50th_Kappic_Eagles.png")

        #Imagen3= Gtk.Image()
        #Imagen3.set_from_file("50375_1155658124_large.jpg")


        #Imagen4 = Gtk.Image()
        #Imagen4.set_from_file("latest.jpg")

        labelnombreempresa = Gtk.Label("Nombre Empresa")
        nombreusuario = Gtk.Label("Usuario")
        contraseña = Gtk.Label("Contraseña")

        self.Entradausuario =Gtk.Entry()
        self.Entradacontraseña = Gtk.Entry()




        #Boton1 = Gtk.Button("Gestion de Clientes")
        Boton3 = Gtk.Button("Entrar")
        Boton4 = Gtk.Button("Salir")






            #if Boton1.set_focus_on_click:

            #Ventanaprincipal2.show_all

        # Creamos las conecsiones
        #Boton1.connect("clicked", self.do_clicked)
        #Boton2.connect("clicked", self.do_clicked2)
        Boton3.connect("clicked", self.do_clicked3)
        Boton4.connect("clicked", Gtk.main_quit)
        #Boton1.connect("clicked", Ventanaprincipal2)
        #Boton2.connect("clicked",Ventanaprincipal3)




        # Añadimos la tabla, le damos la orientacion yespaciados y la hacemos homogenea
        Caja.add(TablaPrincipal)
        Caja1.add(Tabla)
        Caja2.add(Tabla2)
        Caja3.add(Tabla3)

        Caja1.set_orientation(Gtk.Orientation.VERTICAL)
        TablaPrincipal.set_homogeneous(True)
        Tabla.set_row_spacings(25)
        Tabla.set_col_spacings(25)
        Tabla.set_homogeneous(True)

        # Damos las posiciones a los objetos

        Tabla2.attach(nombreusuario,0, 1, 0, 1)




        Tabla2.attach(self.Entradausuario, 0, 1, 1, 2)
        Tabla2.attach(contraseña, 0, 1, 2, 3)

        Tabla2.attach(self.Entradacontraseña, 0, 1, 3, 4)


        Tabla.attach(labelnombreempresa,0,3,0,1)

        #Tabla.attach(Imagen1, 0, 1, 1,2)

        #Tabla.attach(Imagen2, 2, 3, 1, 2)

        #Tabla.attach(Imagen3, 3, 4, 1, 2)

        #Tabla.attach(Imagen4,5, 6, 1, 2)

        #Tabla.attach(labelnombreempresa,0, 1, 0, 1)


        Tabla.attach(Caja2,1,2,1,2)

        #Tabla.attach(Caja3,0,1,1,1)

        #Tabla.attach(nombreusuario, 0, 1, 1, 0)


        #Tabla.attach(contraseña, 2, 4, 2, 1)

        #Tabla.attach(Boton1, 0, 1, 2, 3)

        #Tabla.attach(Boton2, 2, 3 , 2, 3)

        Tabla.attach(Boton4, 0, 1, 2,3)

        Tabla.attach(Boton3, 2, 3, 2,3)


        Tabla.attach(Caja3,0,1,0,1)

        Tabla3.attach(Imagen1, 1,3,3,4)


        # Añadimos la caja al self y mostramos todo
        self.add(Caja1)
        self.show_all()


    #def do_clicked(self,Ventana1):
        #VentanaGestionClientes()
        #self.set_visible(False)
    #def do_clicked2(self,Ventana2):
        #VentanaGestionProductos()
        #self.set_visible(False)




    def do_clicked3(self,Ventana3):

        nombre=self.Entradausuario.get_text()
        passw=self.Entradacontraseña.get_text()
        comando="select * from Usuarios where NOMBRE='"+nombre+"' and Contraseña='"+passw+"'"
        print(comando)
        result=self.db.ejecutar(self.db,comando).fetchone()
        if result is not None:
            #self.informacion.set_text("")
            print("encontrado")
            if result[1]=="True":
                #Visor tabla abre en modo administrador
                print("error")

            else:
                VentanaGestionProductos()
                self.set_visible(False)
        else:
            print("usuario no existe")
            self.Entradausuario.set_text("")
            self.Entradacontraseña.set_text("")
            """self.set_text("El usuario no existe o la contraseña no es correcta")"""


    #def do_clicked3(self,Ventana3):
    #conn = sqlite3.connect("BaseProyecto.db")
    #cursor = conn.cursor()
    #entrada1=cursor.execute("SELECT NOMBRE FROM Usuarios;")
    #entrada2=cursor.execute("SELECT CONTRASEÑA FROM Usuarios;")
    #if self.Entradausuario.get_text == entrada1.fetchall():
        #VentanaGestionProductos()
        #self.set_visible(False)

class VentanaGestionClientes(Gtk.Window):
    def __init__(self):
        self.db = dbm.DBManager
        self.db.__init__(self.db, "BaseProyecto.db")

        Gtk.Window.__init__(self, title="DelioGestor v1.0")
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_border_width(0)
        # Creacion de cajas y tablas
        Caja1 = Gtk.Box()
        Caja1.set_orientation(Gtk.Orientation.HORIZONTAL)
        Tabla = Gtk.Table(5, 5, False)
        Tabla2 = Gtk.Table(5, 5, False)

    # Creamos los objetos necesarios para la ventana

    #NombreVentana = Gtk.Label("Ingreso de Clientes")

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
        #self.Boton4.connect("clicked", self.do_clicked)
        #self.Boton2.connect("clicked", self.do_clicked)
        self.Boton3.connect("clicked", self.do_clicked5)
        self.Boton5.connect("clicked",self.do_clicked)
        TextoBoton1 = Gtk.Label("Este label cambia")

        # Añadimos la tabla, le damos la orientacion yespaciados y la hacemos homogenea
        Caja1.add(Tabla)
        Caja1.set_orientation(Gtk.Orientation.VERTICAL)
        Tabla.set_row_spacings(25)
        Tabla.set_col_spacings(25)
        Tabla.set_homogeneous(True)

        # Damos las posiciones a los objetos

        #Tabla.attach(NombreVentana, 2, 4, 0, 1)

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
        VentanaGestionProductos()
        self.set_visible(False)

    def do_clicked4(self, Ventana4):
            self.DNI.set_text("")
            self.Nombre.set_text("")
            self.Apellidos.set_text("")
            self.NumeroTelefono.set_text("")
            self.Pedidos.set_text("")

    def do_clicked2(self, Ventana2):
        VentanaGestionProductos()
        self.set_visible(False)
        self.set_position(Gtk.WindowPosition.CENTER)

    def do_clicked3(self, Ventana3):
        VentanaGestionTrabajadores()
        self.set_visible(False)
        self.set_position(Gtk.WindowPosition.CENTER)

    def do_clicked5(self, Ventana4):
        comando = "INSERT INTO   Clientes values ('" + self.DNI.get_text() + "','" + self.Nombre.get_text() + "','" + self.Apellidos.get_text() + "','" + self.NumeroTelefono.get_text() + "','" + self.Pedidos.get_text() + "')"
        print(comando)
        result = self.db.ejecutar(self.db, comando)
        if result is not None:
            # self.informacion.set_text("")
            print("insertado")

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
        else:
            print("no se pudo insertar por alguna razon")
            self.informacion.set_text("No se pudo insertar el trabajador ")
            self.Ventanasalida = Gtk.Window()
            Cajaventana = Gtk.Box()
            self.Ventanasalida.add(Cajaventana)
            Tablaventana = Gtk.Table()
            Tablaventana.set_homogeneous(True)
            BotonAceptar = Gtk.Button("Aceptar")
            LabelVentanasalida = Gtk.Label("No se a añadido con exito")
            Tablaventana.attach(BotonAceptar, 1, 2, 1, 2)
            Tablaventana.attach(LabelVentanasalida, 0, 3, 0, 1)
            Cajaventana.add(Tablaventana)
            BotonAceptar.connect("clicked", self.do_clicked7)
            self.Ventanasalida.show_all()
    def do_clicked6(self, Ventana6):
        self.Ventanasalida.set_visible(False)
        





class VentanaGestionProductos(Gtk.Window):
    # Esta sin terminar:


    def __init__(self):
        self.db = dbm.DBManager
        self.db.__init__(self.db, "BaseProyecto.db")

        Gtk.Window.__init__(self, title="DelioGestor v1.0")

        self.set_position(Gtk.WindowPosition.CENTER)

        # Creacion de cajas y tablas

        Caja1 = Gtk.Box()

        Caja1.set_orientation(Gtk.Orientation.HORIZONTAL)

        Tabla = Gtk.Table(5, 5, False)

        Tabla2 = Gtk.Table(5, 5, False)

        #NombreVentana = Gtk.Label("Ingreso Productos")

        #Imagen1 = Gtk.Image("")

        #Imagen2 = Gtk.Image("")

        #Imagen3 = Gtk.Image("")

        self.Identificador = Gtk.Entry()

        self.Identificador2 = Gtk.Label("Identificador:")

        self.Nombre = Gtk.Entry()

        self.Nombre2 = Gtk.Label("Nombre:")

        self.Precio = Gtk.Entry()

        self.Precio2 = Gtk.Label("Precio:")

        self.Tipo = Gtk.Entry()

        self.Tipo2= Gtk.Label("Tipo:")

        self.Boton1 = Gtk.Button("Gestion Clientes")

        self.Boton4 = Gtk.Button("Añadir usuarios ")

        self.Boton3 = Gtk.Button("Volver al menu")

        self.Boton2 = Gtk.Button("Gestion trabajadores")



        # Creamos las conecsiones

        self.Boton1.connect("clicked", self.do_clicked)

        self.Boton2.connect("clicked", self.do_clicked2)

        self.Boton3.connect("clicked", self.do_clicked3)

        self.Boton4.connect("clicked",self.do_clicked4)


        # Añadimos la tabla, le damos la orientacion yespaciados y la hacemos homogenea
        Caja1.add(Tabla)

        Caja1.set_orientation(Gtk.Orientation.VERTICAL)

        Tabla.set_row_spacings(25)

        Tabla.set_col_spacings(25)

        Tabla.set_homogeneous(True)


        #Tabla.attach(NombreVentana, 2, 3, 0, 1)


        #Tabla.attach(self.Nombre, 1, 2, 2, 3)


        #Tabla.attach(self.Precio, 1, 2, 3, 4)


        #Tabla.attach(self.Tipo, 1, 2, 4, 5)


        Tabla.attach(self.Boton1, 1, 2, 2, 3)


        Tabla.attach(self.Boton2, 2, 3, 2, 3)


        Tabla.attach(self.Boton3, 3, 4, 2, 3)


        Tabla.attach(self.Boton4, 4, 5, 2, 3)


        # Añadimos la caja al self y mostramos todo
        self.add(Caja1)
        self.show_all()

    def do_clicked(self, Ventana1):
        VentanaGestionClientes()
        self.set_visible(False)
        self.set_position(Gtk.WindowPosition.CENTER)

        #VentanaGestionProductos()
        #self.set_visible(False)
        #self.set_position(Gtk.WindowPosition.CENTER)

    def do_clicked4(self, Ventana1):
        Gestionusuarios()
        self.set_visible(False)
        self.set_position(Gtk.WindowPosition.CENTER)

    def do_clicked2(self, Ventana2):
        VentanaGestionTrabajadores()
        self.set_visible(False)
        self.set_position(Gtk.WindowPosition.CENTER)
    def do_clicked3(self, Ventana3):
        VentanaInicio()
        self.set_visible(False)
        self.set_position(Gtk.WindowPosition.CENTER)

    def do_clicked6(self, Ventana4):
        comando = "INSERT INTO   Trabajadores values ('" + self.DNI.get_text() + "','" + self.Nombre.get_text() + "','" + self.Apellidos.get_text() + "','" + self.NumeroTelefono.get_text() + "','" + self.Pedidos.get_text() + "')"
        print(comando)
        result = self.db.ejecutar(self.db, comando)
        if result is not None:
            # self.informacion.set_text("")
            print("insertado")

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
        else:
            print("no se pudo insertar por alguna razon")
            self.informacion.set_text("No se pudo insertar el trabajador ")
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

    """def do_clicked4(self, Ventana4):
                VentanaverProductos()
                self.set_visible(False)
                self.set_position(Gtk.WindowPosition.CENTER)

            def do_clicked5(self, Ventana4):
                    self.Identificador.set_text("")
                    self.Nombre.set_text("")
                    self.Precio.set_text("")
                    self.Tipo.set_text("")
                    """


class VentanaGestionTrabajadores(Gtk.Window):

            def __init__(self):
                self.db = dbm.DBManager
                self.db.__init__(self.db, "BaseProyecto.db")

                columnas = ["DNI",
                           "Nombre",
                           "Apellidos",
                           "NumeroTelefono",
                           "DIRECCION"
                           ]

                datos = [["Jurg", "Billeter", "555-0123", "688574957", "Vigo"],
                             ["Johannes", "Schmid", "555-1234", "399364855", "Pontevedra"],
                             ["Julita", "Inca", "555-2345", "687968554", "A Coruña"],
                             ["Javier", "Jardon", "555-3456", "697047858", "Madrid"],
                             ["Jason", "Clinton", "555-4567", "685968436", "Ourense"],
                             ["Random J.", "Hacker", "555-5678", "689403565", "Lugo"]]

                Gtk.Window.__init__(self, title="DelioGestor v1.0")
                self.set_position(Gtk.WindowPosition.CENTER)
                # Creacion de cajas y tablas
                Caja1 = Gtk.Box()
                Caja1.set_orientation(Gtk.Orientation.HORIZONTAL)
                Tabla = Gtk.Table(5, 5, False)
                Tabla2 = Gtk.Table(5, 5, False)


                # Creamos los objetos necesarios para la ventana

                # NombreVentana = Gtk.Label("Ingreso de Clientes")

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
                # self.Boton4.connect("clicked", self.do_clicked)
                # self.Boton2.connect("clicked", self.do_clicked)
                self.Boton3.connect("clicked", self.do_clicked5)
                self.Boton5.connect("clicked", self.do_clicked)
                TextoBoton1 = Gtk.Label("Este label cambia")

                # Añadimos la tabla, le damos la orientacion yespaciados y la hacemos homogenea
                Caja1.add(Tabla)
                Caja1.set_orientation(Gtk.Orientation.VERTICAL)
                Tabla.set_row_spacings(25)
                Tabla.set_col_spacings(25)
                Tabla.set_homogeneous(True)

                # Damos las posiciones a los objetos

                # Tabla.attach(NombreVentana, 2, 4, 0, 1)

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

                # the data in the model (three strings for each row, one for each
                # column)
                listmodel = Gtk.ListStore(str, str, str, str , str)
                # append the values in the model
                for i in range(len(datos)):
                    listmodel.append(datos[i])

                # a treeview to see the data stored in the model
                self.view = Gtk.TreeView(model=listmodel)
                # for each column
                for i, column in enumerate(columnas):
                    # cellrenderer to render the text
                    cell = Gtk.CellRendererText()
                    # the text in the first column should be in boldface
                    if i == 0:
                        cell.props.weight_set = True
                        cell.props.weight = Pango.Weight.BOLD
                    # the column is created
                    col = Gtk.TreeViewColumn(column, cell, text=i)
                    # and it is appended to the treeview
                    self.view.append_column(col)

                # when a row is selected, it emits a signal
                self.view.get_selection().connect("changed", self.on_changed)



                # the label we use to show the selection
                self.label = Gtk.Label()
                self.label.set_text("")



            def do_clicked(self, Ventana1):
                VentanaGestionProductos()
                self.set_visible(False)
                self.set_position(Gtk.WindowPosition.CENTER)




            def do_clicked4(self, Ventana1):
                VentanaInicio()
                self.set_visible(False)
                self.set_position(Gtk.WindowPosition.CENTER)

            def do_clicked5(self, Ventana1):
                comando = "INSERT INTO   Trabajadores values ('"+self.DNI.get_text()+"','"+self.Nombre.get_text()+"','"+self.Apellidos.get_text()+"','"+self.NumeroTelefono.get_text()+"','"+self.Pedidos.get_text()+"')"
                print(comando)
                result = self.db.ejecutar(self.db, comando)
                if result is not None:
                    # self.informacion.set_text("")
                    print("insertado")


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
                else:
                    print("no se pudo insertar por alguna razon")
                    self.informacion.set_text("No se pudo insertar el trabajador ")

                """self.Ventanasalida = Gtk.Window()
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
                self.Ventanasalida.show_all()"""

            def do_clicked7(self, Ventana6):
                self.Ventanasalida.set_visible(False)


class VerTablas(Gtk.Window):
            def __init__(self):
                Gtk.Window.__init__(self, title="Ejemplo de TreeView")
                self.set_default_size(400, 800)
                self.set_border_width(20)
                self.set_position(Gtk.WindowPosition.CENTER)

                 # Inicializamos la conexion con la bd
                self.db = dbm.DBManager
                self.db.__init__(self.db, "BaseProyecto.db")

                # Creamos un box como layout principal
                box = Gtk.Box()
                box.set_orientation(Gtk.Orientation.VERTICAL)
                box.set_halign(Gtk.Align.CENTER)

                # Creamos el notebook que contrendra cada tabla y lo añadimos a la ventana
                notebook = Gtk.Notebook()
                box.add(notebook)

                listaTabla = self.db.consultarNombreTablas(self.db)
                for x in listaTabla:
                    print(x)
                    nombreTabla = x
                    # coge los nombres de las columnas de la tabla
                    columnas = self.db.columnas(self.db, nombreTabla)
                    # coge los valores de cada fila
                    agenda = self.db.valores(self.db, nombreTabla)
                    # coge el tipo de dato de la columna
                    ct = self.db.columnasTipo(self.db, nombreTabla)

                    # Este metodo si que vale para cualquier tabla

                    modelo = Gtk.ListStore.new(ct)

                    for persona in agenda:
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





                # Añadimos la tabla, le damos la orientacion y espaciados y la hacemos homogenea
                Caja1.add(Tabla)
                Caja1.set_orientation(Gtk.Orientation.VERTICAL)

                #Tabla.attach(NombreVentana, 2, 4, 0, 1)

                Tabla.set_row_spacings(25)
                Tabla.set_col_spacings(25)
                #Tabla.set_homogeneous(True)
                Tabla.set_margin_left(25)
                Tabla.set_margin_right(25)

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

                Tabla.attach(self.view, 4, 5, 3, 4)
                Tabla.attach(self.Boton5, 2, 3, 7, 8)

                # Añadimos la caja al self y mostramos todo
                self.add(Caja1)
                self.show_all()

            def on_changed(self, selection):
                # get the model and the iterator that points at the data in the model
                (model, iter) = selection.get_selected()
                 # set the label to a new value depending on the selection
                self.label.set_text("\n %s %s %s" %
                                    (model[iter][0], model[iter][1], model[iter][2]))
                return True







            def do_clicked(self, Ventana1):
                VentanaGestionProductos()
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
                #self.view.append_column.


            def do_clicked6(self, Ventana6):
                self.Ventanasalida.set_visible(False)

class Gestionusuarios(Gtk.Window):
            def __init__(self):
                self.db = dbm.DBManager
                self.db.__init__(self.db, "BaseProyecto.db")

                Gtk.Window.__init__(self, title="DelioGestor v1.0")
                self.set_position(Gtk.WindowPosition.CENTER)
                self.set_border_width(0)
                # Creacion de cajas y tablas
                Caja1 = Gtk.Box()
                Caja1.set_orientation(Gtk.Orientation.HORIZONTAL)
                Tabla = Gtk.Table(5, 5, False)
                Tabla2 = Gtk.Table(5, 5, False)

                # Creamos los objetos necesarios para la ventana

                # NombreVentana = Gtk.Label("Ingreso de Clientes")

                self.Nombre = Gtk.Entry()
                self.Nombre2 = Gtk.Label("Nombre Usuario:")

                self.Contraseña = Gtk.Entry()
                self.Contraseña2 = Gtk.Label("Contraseña:")



                self.Boton1 = Gtk.Button("Salir")
                self.Boton2 = Gtk.Button("Borrar")
                self.Boton3 = Gtk.Button("Aceptar")
                self.Boton5 = Gtk.Button("Volver al menu")

                # Creamos las conecsiones

                self.Boton1.connect("clicked", Gtk.main_quit)
                # self.Boton4.connect("clicked", self.do_clicked)
                # self.Boton2.connect("clicked", self.do_clicked)
                self.Boton3.connect("clicked", self.do_clicked5)
                self.Boton5.connect("clicked", self.do_clicked)
                TextoBoton1 = Gtk.Label("Este label cambia")

                # Añadimos la tabla, le damos la orientacion yespaciados y la hacemos homogenea
                Caja1.add(Tabla)
                Caja1.set_orientation(Gtk.Orientation.VERTICAL)
                Tabla.set_row_spacings(25)
                Tabla.set_col_spacings(25)
                Tabla.set_homogeneous(True)

                # Damos las posiciones a los objetos

                # Tabla.attach(NombreVentana, 2, 4, 0, 1)

                Tabla.attach(self.Nombre2, 0, 1, 1, 2)
                Tabla.attach(self.Nombre, 1, 2, 1, 2)

                Tabla.attach(self.Contraseña2, 0, 1, 2, 3)
                Tabla.attach(self.Contraseña, 1, 2, 2, 3)



                Tabla.attach(self.Boton1, 0, 1, 7, 8)

                Tabla.attach(self.Boton2, 3, 4, 7, 8)

                Tabla.attach(self.Boton3, 5, 6, 7, 8)

                Tabla.attach(self.Boton5, 2, 3, 7, 8)

                # Añadimos la caja al self y mostramos todo
                self.add(Caja1)
                self.show_all()
                # Vamos unidendo las ventanas con estos metodos y creando otros metodos necesarios

            def do_clicked(self, Ventana1):
                VentanaGestionProductos()
                self.set_visible(False)


            def do_clicked3(self, Ventana3):
                VentanaGestionTrabajadores()
                self.set_visible(False)
                self.set_position(Gtk.WindowPosition.CENTER)

            def do_clicked5(self, Ventana4):
                comando = "INSERT INTO Usuarios values ('" + self.Nombre.get_text() + "','" + self.Contraseña.get_text() + "')"
                print(comando)
                result = self.db.ejecutar(self.db, comando)
                print(comando)
                if result is not None:
                    # self.informacion.set_text("")
                    print("insertado")

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
                else:
                    print("no se pudo insertar por alguna razon")
                    self.informacion.set_text("No se pudo insertar el usuario ")
                    self.Ventanasalida = Gtk.Window()
                    Cajaventana = Gtk.Box()
                    self.Ventanasalida.add(Cajaventana)
                    Tablaventana = Gtk.Table()
                    Tablaventana.set_homogeneous(True)
                    BotonAceptar = Gtk.Button("Aceptar")
                    LabelVentanasalida = Gtk.Label("No se a añadido con exito")
                    Tablaventana.attach(BotonAceptar, 1, 2, 1, 2)
                    Tablaventana.attach(LabelVentanasalida, 0, 3, 0, 1)
                    Cajaventana.add(Tablaventana)
                    BotonAceptar.connect("clicked", self.do_clicked7)
                    self.Ventanasalida.show_all()

            def do_clicked6(self, Ventana6):
                self.Ventanasalida.set_visible(False)


# Realizamos el correspondiente if
if __name__ == "__main__":
     VentanaInicio()
     Gtk.main()




