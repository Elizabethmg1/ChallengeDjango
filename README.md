# ChallengeDjango

En primer lugar se creo el proyecto con django-admin startproject,

luego se descargo postgresSQL y se creo una base de datos para visualizar las tablas creadas,

luego se hiso la conexion a la base de datos en el archivo settings del proyecto en la parte DATABASES especificando engine, name, user, password, host y port

## Para la tarea 1:
En primer lugar se creo la app con nombre "app" con el comando python manage.py startapp y se la agrego al archivo settings en la parte APPS,

luego se comenzo a editar el archivo modelos con la tabla especificada para la API requerida,

se creo el archivo API la cual toma la API especificada y extrae su informacion.

Luego se empezo a trabajar en el archivo views en donde se guarda la informacion obtenida de la api y se relaciona con el template llamado template.html

Despues de esto se edito el archivo urls del proyecto para que se pueda visualizar en la web con http://127.0.0.1:8000/network/,

se descargo un archivo de boostrap y se lo relaciono con el template

cada vez que se realiza el comando python manage.py runserver se guardan los datos de la API y se lo puede visualizar desde la web,

tambien se edito el archivo admin de la app para que al crear el usuario con python manage.py createsuperuser se pueda visualizar los objetos network guardados.

## Para la tarea 2:
En primer lugar se creo la app con nombre "app1" con el comando python manage.py startapp y se la agrego al archivo settings en la parte APPS,

luego se comenzo a editar el archivo modelos con la tabla especificada para la data requerida,

se creo el archivo "scraping" el cual scrapea los datos de la pagina solicitada, esta editado para que solo traiga datos de solo 3 paginas para probar pero se puede quitar esta linea y hace scraping de todas las paginas, este scraping utiliza threads para que sea mas rapido el proceso,

Luego se empezo a trabajar en el archivo views en donde se guarda la informacion obtenida del scraping y se relaciona con el template llamado template1.html

Despues de esto se edito el archivo urls del proyecto para que se pueda visualizar en la web con http://127.0.0.1:8000/proyecto/

cada vez que se realiza el comando python manage.py runserver se guardan los datos del scraping y se lo puede visualizar desde la web

tambien se edito el archivo admin de la app para que al crear el usuario con python manage.py createsuperuser se pueda visualizar los objetos proyecto guardados.
