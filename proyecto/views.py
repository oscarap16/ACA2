# Se importan las librerias para el template y los renders
from django.shortcuts import render
import json


# Librerias para operaciones matemáticas
import numpy as np
# Libreria para el manejo de datos
import pandas as pd

# Libreria para la conexión de PostgreSQL
from proyecto.connection import connection_postgresql

# -----------------------------------

def main(request):
    # Se genera la conexión con la base de datos
    cursor = connection_postgresql()

    # Consulta para Gráfica 1
    cursor.execute(""" SELECT total FROM compras """)
    record = cursor.fetchall()

    # Datos Gráfica 1
    datos_grafica1 = [float(item[0]) for item in record]
    #-----------------------------------------------------------

    # Consulta para Gráfica 3
    cursor.execute(""" SELECT CL.nombres, C.total 
                       FROM compras AS C, clientes AS CL
                       WHERE C.id_cliente = CL.id_cliente """)
    record = cursor.fetchall()

    # Datos Gráfica 3
    categorias_grafica3 = [item[0] for item in record]
    datos_grafica3 = [float(item[1]) for item in record]
    #-----------------------------------------------------------

    # Consulta para Gráfica 4
    cursor.execute(""" SELECT ciudad, id_ciudad 
                       FROM ciudades """)
    record = cursor.fetchall()

    # Datos Gráfica 4
    categorias_grafica4 = [item[0] for item in record]
    datos_grafica4 = [float(item[1]) for item in record]
   
    # Se envian los valores al contexto de todas las gráficas para renderizar
    context = {
                "datos_grafica1": datos_grafica1,
                "categorias_grafica3": categorias_grafica3,
                "datos_grafica3": datos_grafica3,
                "categorias_grafica4": categorias_grafica4,
                "datos_grafica4": datos_grafica4}

    # *** Plantilla ***
    return render(request, 'index.html', context=context)