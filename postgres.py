import psycopg2
import time
import tkinter as tk

# Función para ejecutar la consulta y mostrar el resultado en la ventana
def execute_query():
    # Configurar la conexión a la base de datos
    conn = psycopg2.connect(
        host="localhost",
        database="mydb",
        user="myuser",
        password="mypass"
    )

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
    result_label.config(text=f"La consulta devolvió {result[0]} registros en {execution_time_ms:.2f} ms")

    # Cerrar el cursor y la conexión a la base de datos
    cur.close()
    conn.close()

# Crear la ventana y los widgets
root = tk.Tk()
root.title("Testeo de velocidad de base de datos")
root.geometry("400x200")

query_button = tk.Button(root, text="Ejecutar consulta", command=execute_query)
query_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

# Iniciar el bucle principal de la ventana
root.mainloop()

