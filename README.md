# django_ml

Visualización de Datos con Python y Django

Autor: José M. Llanos M.

Fecha: 07-julio-2025


## Paso 1: Instalación de Django

#### Linux / macOS:

python3 -m pip install Django==5.2.4

#### Windows:

pip install Django==5.2.4

## Paso 2: Verificar la versión del Django

python -m django --version

## Paso 3: Listalar las librerias a utilizar

pip install numpy pandas matplotlib

## Paso 4: Correr la aplicación para verificar que Django está en funcionamiento

nombre_proyecto$ python manage.py runserver

## Paso 5: Clone la plantilla de Django dentro de la carpeta del proyecto

git clone https://github.com/jose-llanos/django_ml.git

## Paso 6: Modifique el archivo views.py

Aquí deben ir todos los elementos de visualización que se pretende mostrar en el dashboard en el lenguaje de programación Python.

## Paso 7: Modifique el archivo index.html

Este es el Dashboard, aquí se toman los datos enviados por el Python y se muestran a través de html al usuario.

## Paso 8: Ejecute la aplicación en el navegador para visualizar el dashboard

nombre_proyecto$ python manage.py runserver

Y al final el Django genera una URL para la visualización de la aplicación

## --------------------------------------------------

#### Si el proyecto es nuevo, se debe ejecutar estos pasos después de instalar las librerias (Paso 3)

## Paso 3.1: Crear un proyecto en Django

django-admin startproject nombre_proyecto

## Paso 3.2: Crear migraciones en Django

python manage.py migrate
