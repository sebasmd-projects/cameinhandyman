### Ejecutar Proyecto

1. Crear/Activar un entorno virtual de desarrollo con Python
2. Instalar dependencias

```bash
cd Backend\requirements
```

Linux:

```bash
pip install -r linux_reqs.txt
```

Windows:

```bash
pip install -r windows_reqs.txt
```

3. Base de datos:

Postgresql: Abrir SQL Shell de postgresql y crear una nueva base de datos

```bash
CREATE DATABASE db_nombre;
CREATE USER db_user;
\c
ALTER USER db_user WITH PASSWORD 'db_pass';
```

4. Cambiar el archivo sensitive_data.json

```
"NAME": "db_nombre"
"USER": "db_user"
"PASSWORD": "db_pass"
```

en este mismo archivo editar la conección SMTP del correo, teniendo en cuenta que el SSL y el TLS no pueden estar en True al mismo tiempo, el puerto por defecto en muchos servidores para smtp ssl es 465 y para smtp tls es 587.

```
"EMAIL_USE_SSL": "True",
"EMAIL_USE_TLS": "False",
"EMAIL_BACKEND": "django_smtp_ssl.SSLEmailBackend",
"EMAIL_HOST": "",
"EMAIL_PORT": 465,
"EMAIL_HOST_USER": "",
"EMAIL_HOST_PASSWORD": ""
```

5. Migrar y añadir datos a la base de datos

```bash
python manage.py migrate
python manage.py loaddata initial_data.json
```

6. Ejecutar el proyecto

```bash
cd Backend
python manage.py runserver
```
