
import sqlite3 as dbapi
#Creamos la conexion y la base realizamos try para pruevas


class DBManager:



    def __init__(self,databasePath):
        self.conn=dbapi.connect(databasePath)



    def insertar(self, nombreTabla, campos):
            comando = "insert into " + nombreTabla + " values('"
            for campo in range(len(campos)):
                if (campo < len(campos) - 1):
                    comando += campos[campo] + "','"
                else:
                    comando += campos[campo] + "')"
            print(comando)
            self.conn.execute(comando)

            self.conn.commit()



    def ejecutar(self, comando):
        return self.conn.execute(comando)

        # METODOS GENERICOS

        # Estos metodos los voy a usar para generar el modelo del treeview
    """
        leer los nombres de todas las tablas de la base de datos
        """

    def consultarNombreTablas(self):
            nombres = []
            nombre_tablas = self.ejecutar(self, "select name from sqlite_master where type='table'")
            for x in nombre_tablas:
                nombres += [x[0]]

            return nombres

    """
       leer la informacion de las columnas de una tabla"""

    def consultarColumnasTabla(self, nombreTabla):
        nombre_columnas = self.ejecutar(self, "pragma table_info(" + nombreTabla + ")")
        for x in nombre_columnas:
            print("Columna: ", x[0], ", Nombre: ", x[1], ", Tipo de dato: ", x[2])
        # x[3],x[4] y x[5] tengo que averiguar lo que son



    """
               Este metodo me devuelve una lista con los nombres de las columnas para crear el modelo en el treeView"""

    def columnas(self, nombreTabla):
        cols = []
        for x in self.ejecutar(self, "pragma table_info(" + nombreTabla + ")"):
            cols += [x[1]]
        return cols

    """
            dependiendo del tipo de columna tiene que devolver un tipo u otro (por ejemplo si es text debe devolver str)"""

    # TODO faltan tipos de datos por definir, hay que tener cuidado de comprobar mayusculas y minisculas
    def columnasTipo(self, nombreTabla):
                columnTypes = []
                for x in self.ejecutar(self, "pragma table_info(" + nombreTabla + ")"):
                    if (x[2] == "text" or x[2] == "TEXT" or x[2] == "string" or x[2] == "STRING"):
                        columnTypes += [str]
                    elif (x[2] == "integer" or x[2] == "INTEGER" or x[2] == "int" or x[2] == "INT"):
                        columnTypes += [int]
                    elif (x[2] == "number" or x[2] == "NUMBER" or x[2] == "real" or x[2] == "REAL"):
                        columnTypes += [float]
                    elif (x[2] == "BOOLEAN" or x[2] == "boolean"):
                        columnTypes += [bool]
                    else:
                        columnTypes += [None]
                return columnTypes

    """
            Este metodo me devuelve una lista de tuplas con los valores de cada fila para pasarle al modelo"""

    def valores(self, nombreTabla):
                vals = []
                for x in self.ejecutar(self, "select * from " + nombreTabla):
                    vals += [x]
                return vals

                #def insertardatospruevas ():
        #try:
            #conn = sqlite3.connect("BaseProyecto.db")
            #cursor = conn.cursor()
            #sentencia= "SELECT * FROM Trabajadores"
            #sentencia2= "SELECT * FROM Usuarios"
        #except conn.DatabaseError as erroBaseDatos:
            #print("Erro en conexionDB (DataBaseError):" + str(erroBaseDatos))
        #except conn.OperationalError as erroBaseDatos:
            #print("Erro en conexionDB (operationalerror):" + str(erroBaseDatos))
        #else:
            #print("Conexion realizada con exito")


        # Creamos la tabla de Direcciones
        #cursor.execute("CREATE TABLE Usuarios (NOMBRE TEXT, CONTRASEÑA TEXT)")
        #Agregamos dos direcciones
        #cursor.execute("INSERT INTO Trabajadores VALUES ('53612030L','Delio','Fernandez',691831678,'Vilaboa' )")
        #cursor.execute("INSERT INTO Trabajadores VALUES ('37622656Ñ','Pedro','Collazo',656446452,'Vigo' )")
        #cursor.execute("INSERT INTO Usuarios VALUES ('Pedro','141546161' )")
        #cursor.execute("INSERT INTO Usuarios VALUES ('Delio','113464524' )")
        #cursor.execute(sentencia2)
        #trabajadores = cursor.fetchall()
        #Usuarios = cursor.fetchall()
        #print(trabajadores)
        #print(Usuarios)

        #cursor.execute("SELECT nombre  FROM Usuarios")

        #Sentencia para eliminar
        #conn.commit()

        #cursor.close()

        #conn.close()


    """def eliminarpruevas(self,nombreTabla,keyName,keyValue):

        conn = sqlite3.connect("BaseProyecto.db")
        cursor = conn.cursor()

        fetchall = cursor.fetchall()
        #eliminar = " DELETE FROM Trabajadores WHERE NOMBRE = ?;"
        eliminar2 = " DELETE FROM Usuarios WHERE NOMBRE = ?;"
        cursor.execute(eliminar2,["Delio"])
        cursor.execute(eliminar2,["Pedro"])

        print(fetchall)



        conn.commit()

        cursor.close()

        conn.close()"""

    #insertardatos()

    #eliminar()
