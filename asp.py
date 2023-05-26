import time
import tkinter as tk
import psycopg2
import sqlite3
import pymysql

# Función para ejecutar el procedimiento almacenado y mostrar el resultado en la ventana
def execute_query(conn):
    # Crear un cursor para ejecutar el procedimiento almacenado
    cur = conn.cursor()

    # Ejecutar el procedimiento almacenado y medir su tiempo de ejecución
    start_time = time.time()
    
    if isinstance(conn, sqlite3.Connection):
        cur.execute("SELECT COUNT(*) FROM inventario")
    else:
        cur.callproc('count_inventario')
        
    result = cur.fetchone()
    end_time = time.time()

    # Calcular el tiempo de ejecución en milisegundos
    execution_time_ms = (end_time - start_time) * 1000

    # Actualizar la etiqueta con el resultado y el tiempo de ejecución
    result_label.config(text=f"El procedimiento (sp) devolvió {result[0]} registros en {execution_time_ms:.2f} ms")

    # Cerrar el cursor
    cur.close()

# Función para crear el procedimiento almacenado en PostgreSQL
def create_count_inventario_procedure_postgres(conn):
    # Crear un cursor para ejecutar comandos
    cur = conn.cursor()

    # Definir el código del procedimiento almacenado
    procedure_code = """
    CREATE OR REPLACE FUNCTION count_inventario()
    RETURNS INTEGER AS $$
    DECLARE
        count_result INTEGER;
    BEGIN
        SELECT COUNT(*) INTO count_result FROM inventario;
        RETURN count_result;
    END;
    $$ LANGUAGE plpgsql;
    """

    # Ejecutar el comando para crear el procedimiento almacenado
    cur.execute(procedure_code)

    # Confirmar los cambios en la base de datos
    conn.commit()

    # Cerrar el cursor
    cur.close()

# Función para crear el procedimiento almacenado en MariaDB y MySQL
def create_count_inventario_procedure(conn):
    # Crear un cursor para ejecutar comandos
    cur = conn.cursor()

    # Definir el código del procedimiento almacenado
    procedure_code = """
    CREATE PROCEDURE count_inventario()
    BEGIN
        SELECT COUNT(*) FROM inventario;
    END
    """

    # Ejecutar el comando para crear el procedimiento almacenado
    cur.execute(procedure_code)

    # Cerrar el cursor
    cur.close()

# Función para configurar y ejecutar la consulta en PostgreSQL
def postgres_query():
    # Configurar la conexión a la base de datos
    conn = psycopg2.connect(
        host="localhost",
        database="mydb",
        user="myuser",
        password="mypass"
    )
    
    # Crear el procedimiento almacenado en PostgreSQL
    create_count_inventario_procedure_postgres(conn)
    
    # Ejecutar el procedimiento almacenado
    execute_query(conn)
    
    # Cerrar la conexión a la base de datos
    conn.close()

# Función para configurar y ejecutar la consulta en MySQL y MariaDB
def mariadb_query():
    # Configurar la conexión a la base de datos
    conn = pymysql.connect(
        host="localhost",
        database="mydb",
        user="root",
        password="pass123"
    )
    
    # Crear el procedimiento almacenado en MySQL/MariaDB
    create_count_inventario_procedure(conn)
    
    # Ejecutar el procedimiento almacenado
    execute_query(conn)
    
    # Cerrar la conexión a la base de datos
    conn.close()

def mysql_query():
    # Configurar la conexión a la base de datos
    conn = pymysql.connect(
        host="localhost",
        database="mydb",
        user="root",
        password="pass123"
    )
    
    # Crear el procedimiento almacenado en MySQL/MariaDB
    create_count_inventario_procedure(conn)
    
    # Ejecutar el procedimiento almacenado
    execute_query(conn)
    
    # Cerrar la conexión a la base de datos
    conn.close()

# Función para configurar y ejecutar la consulta en SQLite
def sqlite_query():
    # Configurar la conexión a la base de datos
    conn = sqlite3.connect('mydb.db')
    
    # Ejecutar la consulta directamente en SQLite
    execute_query(conn)
    
    # Cerrar la conexión a la base de datos
    conn.close()

# Crear la ventana y los widgets
root = tk.Tk()
root.title("Testeo de velocidad de base de datos")
root.geometry("400x300")

postgres_button = tk.Button(root, text="PostgreSQL", command=postgres_query)
postgres_button.pack(pady=10)

mariadb_button = tk.Button(root, text="MariaDB", command=mariadb_query)
mariadb_button.pack(pady=10)

mysql_button = tk.Button(root, text="MySQL", command=mysql_query)
mysql_button.pack(pady=10)

sqlite_button = tk.Button(root, text="SQLite", command=sqlite_query)
sqlite_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

# Iniciar el bucle principal de la ventana
root.mainloop()
