# Tercera-pre-entrega-Delvitto
Creador de notas
# Descripción breve del proyecto.
App para crear notas y buscarlas en una base de datos. 

## Requisitos Previos

Python 3.9.13
    django==4.2
    pillow==9.0

## Configuración del Entorno

### Entorno virtual.
1. Creamos la carpeta donde trabajaremos en nuestro proyecto de Django.
2. Abrimos VsCode posicionándonos en dicha carpeta.
3. Si no tenemos instalado el gestor de entornos virtuales **pipenv**, abrimos la termina desde VsCode `ctrl + j` y lo instalamos:<br>
    `pip install pipenv`
4. Si queremos seleccionar una versión de Python específica para nuestro proyecto debemos tenerla instalada en la PC. Luego podemos crear el entorno con el siguiente comando:<br>
    `pipenv --python 3.9.13`
5. Usamos un mismo comando para crear o activar el entorno virtual:<br>
    `pipenv shell`<br>
    El entorno virtual queda indicado en la consola con un prefijo similar a esto:<br>`(nombre_entorno_virtual) C:\path_donde_estamos_ubicados`<br>
    De no ser así, hay varias formas de solucionarlo, ver: **(1) Problemas**
---

### Instalaciones
1. Creamos el archivo de **requirements.txt**, el cuál por el momento sólo va a tener la versión de Django que deseemos. También es buena práctica indicar a modo de comentario la versión de Python que usamos para el proyecto.
    ```
    # Python 3.9.13
    django==4.2
    ```
2. lo ejecutamos con pipenv:<br>
    `pipenv install -r requirements.txt`

Como utilizar la app
Nombre del Proyecto: Mi Aplicación de Notas

Funcionalidades Principales:

Crear notas:

Ve a la página de creación de notas haciendo con la url: http://127.0.0.1:8000/AppNotas/crear_nota_form/
Escribe el contenido de tu nota en el campo de texto proporcionado.
Haz clic en el botón "Enviar" para guardar tu nota en la base de datos.
Buscar Notas: Si deseas encontrar una nota específica o ver una lista de notas existentes, puedes hacerlo de la siguiente manera:

Ve a la página de búsqueda de notas haciendo clic aquí.
Ingresa una palabra clave o término de búsqueda en el campo de búsqueda y presiona el botón "Buscar".
Verás una lista de notas que coinciden con tu término de búsqueda. Si no hay coincidencias, se mostrará un mensaje indicando que no se encontraron notas.
