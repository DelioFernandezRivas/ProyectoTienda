import sqlite3

conn = sqlite3.connect('')

cursor=conn.cursor()

print("La base de datos se abrio correctamente")
def creartabla():
    cursor.execute('''CREATE TABLE tablaproductos(
               Identifacador VARCHAR(20) PRIMARY   KEY  NOT NULL,
               Nombre    TEXT    NOT NULL,
               Precio    INT     NOT NULL,
               Imagen   BLOB     NOT NULL)''')

    conn.commit()
    print("Se guardo correctamente ")

def insertar():
    cursor.execute("INSERT INTO tablaproductos(Identificador,Nombre,Precio,Imagen) VALUES('1234A','Warhammer Quest',25.4,"")")

    cursor.execute("INSERT INTO tablaproductos(Identificador,Nombre,Precio,Imagen) VALUES('2234A','Figura Space marine de los Ultramarines',28.4,"")")

    cursor.execute("INSERT INTO tablaproductos(Identificador,Nombre,Precio,Imagen) VALUES('3234A','Tanque de batalla version leman Russ Guardia imperial',100.4,"")")

    cursor.execute("INSERT INTO tablaproductos(Identificador,Nombre,Precio,Imagen) VALUES('4234A','Primarca Roboute Guilliman Ultramarines',75.4,"")")
creartabla()
insertar()

conn.close()