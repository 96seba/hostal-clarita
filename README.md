# Instrucciones para recrear el espacio de trabajo

## Requerimientos

* Base de datos: [Oracle 18c Express](https://www.oracle.com/database/technologies/xe-downloads.html)
* Enlace al epositorio: https://github.com/kappedro/hostal-clarita


## Instalación de la BD

* ⋯


## Creación de usuario

* Ejecutar el script `1_creacion_esquema.sql`.


## Preparación del Ambiente

* Descomprimir el archivo `codigo_fuente_solucion_iteracion_2.zip`
* Dentro de la carpeta descomprimida, crear un ambiente virtual de Python usando `python -m venv myenv` y activar (?).
* Instalar las dependencias usando el comando `python pip install -r requeriments.txt`.


## Carga de datos

* El código fuente tiene configurado los siguientes datos de conexión. Si el host, el puerto o el SID son diferentes en la máquina anfitriona, modificarlos en el archivo `hostal_clarita\settings.py`. 
    * Host: localhost
    * Puerto: 1521
    * SID/Service Name: xe
    * Usuario: c##clarita
    * Contraseña: clarita
* Abrir una terminal dentro de la carpeta del código fuente y ejecutar `python manage.py makemigrations` seguido de `python manage.py migrate`.
* En la base de datos, ejecutar el script `2_poblado_tablas.sql`.

## Ejecución
* Para iniciar la aplicación web, ejecutar `python manage.py runserver`.
* Usar los siguientes datos de prueba:
    * Administrador
        * Correo: clarita@hostalclarita.cl
        * Contraseña: clarita
    * Empleado
        * Correo: juan@hostalclarita.cl
        * Contraseña: empleado
    * Cliente 1
        * Correo: ceo@polpaico.cl
        * Contraseña: cliente
    * Cliente 2
        * Correo: ceo@heladosyork.cl
        * Contraseña: cliente
    * Cliente 3
        * Correo: ceo@avon.cl
        * Contraseña: cliente
    * Proveedor 1:
        * RUT: 91753234-6
    * Proveedor 2:
        * RUT: 92945753-6
    * Proveedor 3:
        * RUT: 93459283-2

