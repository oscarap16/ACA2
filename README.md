# django_ml-ACA 3 – Dashboard de Visualización de Datos con Django y PostgreSQL

Visualización de Datos con Python y Django

Docente: José M. Llanos M.

# Autores

María Catalina Rodríguez Uricoechea
Oscar Andres Paez Villamil

Especialización en Visualización de Datos
Enero 2026

# Descripción del proyecto

Este proyecto corresponde al desarrollo del ACA 3, donde se implementa un dashboard interactivo utilizando Django bajo el patrón MVT (Modelo–Vista–Template), conectado a una base de datos PostgreSQL.

El dashboard permite visualizar, filtrar y analizar datos provenientes de cinco tablas relacionadas, mediante gráficos dinámicos e interactivos construidos con Chart.js y Highcharts.

# Tecnologías utilizadas

Python 3
Django 5.x
PostgreSQL
Chart.js
Highcharts
HTML5 / CSS3
Git & GitHub

# Modelo de datos

La base de datos fue diseñada en PostgreSQL y contiene 5 tablas relacionadas mediante llave primaria y llaves foráneas:

Clientes
Pedidos
Productos
Pagos
Detalle_Pedidos

Cada tabla contiene 30 registros.

# Patrón arquitectónico (MVT)

El proyecto sigue el patrón Modelo–Vista–Template (MVT) de Django:

Modelos (models.py):
Definen la estructura de las tablas existentes en PostgreSQL.

Vistas (views.py):
Contienen la lógica del dashboard, filtros, KPIs y consultas agregadas.

Templates (index.html):
Renderizan la información y los gráficos dinámicos.

# Conexión Django – PostgreSQL

La conexión se configuró en el archivo settings.py usando el motor django.db.backends.postgresql, permitiendo que Django interactúe directamente con la base de datos creada.

# Visualizaciones implementadas
Gráficos con Chart.js
Clientes por ciudad (barras)
Pedidos por estado (pie)
Productos por categoría (barras)
Pagos por método (doughnut)
Gráfico con Highcharts
Pagos por método (Highcharts)

# Filtros dinámicos

El dashboard incluye filtros que afectan automáticamente todas las visualizaciones:

Filtro global por ciudad
Filtro por categoría de producto
Los gráficos y KPIs se actualizan automáticamente según los filtros seleccionados, sin necesidad de recargar manualmente la página.

# KPIs mostrados

Total de clientes
Total de pedidos
Suma del subtotal de pedidos
Suma del costo de envío
Todos los KPIs están afectados por los filtros activos.

# Operaciones CRUD (Base de datos)

Se realizaron operaciones directamente sobre la base de datos:

Inserción de nuevos registros en distintas tablas
Actualización de registros existentes
Eliminación de registros

Los cambios se reflejan automáticamente en el dashboard al recargar la vista, demostrando la integración completa entre Django y PostgreSQL.

# Cómo ejecutar el proyecto

Clonar el repositorio:

git clone https://github.com/oscarap16/ACA2.git


Ingresar al proyecto:

cd ACA2


Instalar dependencias:

pip install django psycopg2


Configurar la base de datos PostgreSQL en settings.py.

Ejecutar el servidor:

python manage.py runserver


Abrir en el navegador:

http://127.0.0.1:8000/
