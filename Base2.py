import sqlite3 as dbapi

try:
        conn = dbapi.connect("BaseProyecto.db")
        cursor = conn.cursor()
        sentencia = "SELECT * FROM Trabajadores"
        sentencia2 = "SELECT * FROM Usuarios"
except conn.DatabaseError as erroBaseDatos:
        print("Erro en conexionDB (DataBaseError):" + str(erroBaseDatos))
except conn.OperationalError as erroBaseDatos:
        print("Erro en conexionDB (operationalerror):" + str(erroBaseDatos))
else:
        print("Conexion realizada con exito")


# Creamos la tabla de Direcciones
cursor.execute("CREATE TABLE  Clientes(DNI TEXT, NOMBRE TEXT, APELLIDOS TEXT, NUMEROTELEFONO TEXT, PEDIDOS TEXT)")
print("Creada con exito")


conn.commit()

cursor.close()

conn.close()
