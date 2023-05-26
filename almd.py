import time
import tkinter as tk
import psycopg2
import sqlite3
import pymysql

# Función para ejecutar la consulta y mostrar el resultado en la ventana
def execute_query(conn):
    # Crear un cursor para ejecutar consultas
    cur = conn.cursor()

    # Ejecutar la consulta de prueba y medir su tiempo de ejecución
    start_time = time.time()
    cur.execute("SELECT COUNT(*) FROM inventario")
    result = cur.fetchone()
    end_time = time.time()

    # Calcular el tiempo de ejecución en milisegundos
    execution_time_ms = (end_time - start_time) * 1000

    # Actualizar la etiqueta con el resultado y el tiempo de ejecución
    result_label.config(text=f"La consulta (lmd) devolvió {result[0]} registros en {execution_time_ms:.2f} ms")

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
    
    execute_query(conn)
    
    # Cerrar la conexión a la base de datos
    conn.close()

# Función para configurar y ejecutar la consulta en MySQL
def mysql_query():
    # Configurar la conexión a la base de datos
    conn = pymysql.connect(
        host="localhost",
        database="mydb",
        user="root",
        password="pass123"
    )
    
    execute_query(conn)
    
    # Cerrar la conexión a la base de datos
    conn.close()

# Función para configurar y ejecutar la consulta en MariaDB
def mariadb_query():
    # Configurar la conexión a la base de datos
    conn = pymysql.connect(
        host="localhost",
        database="mydb",
        user="root",
        password="pass123"
    )
    
    execute_query(conn)
    
    # Cerrar la conexión a la base de datos
    conn.close()
    
# Función para configurar y ejecutar la consulta en SQLite
def sqlite_query():
    # Configurar la conexión a la base de datos
    conn = sqlite3.connect('mydb.db')
    
    execute_query(conn)
    
    # Cerrar la conexión a la base de datos
    conn.close()

# Crear la ventana y los widgets
root = tk.Tk()
root.title("Testeo de velocidad de base de datos")
root.geometry("400x300")

postgres_button = tk.Button(root, text="PostgreSQL", command=postgres_query)
postgres_button.pack(pady=10)

mysql_button = tk.Button(root, text="MySQL", command=mysql_query)
mysql_button.pack(pady=10)

mysql_button = tk.Button(root, text="MariaDB", command=mariadb_query)
mysql_button.pack(pady=10)

sqlite_button = tk.Button(root, text="SQLite", command=sqlite_query)
sqlite_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

# Iniciar el bucle principal de la ventana
root.mainloop()
