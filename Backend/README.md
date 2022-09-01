### Execute Project

1. Create/Activate a virtual development environment with Python
2. Install dependencies

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

3. Database:

Postgresql: Open SQL Shell from postgresql and create a new database

```bash
CREATE DATABASE db_name;
CREATE USER db_user;
\c
ALTER USER db_user WITH PASSWORD 'db_password';
```

4. Change the file sensitive_data.json

```
"NAME": "db_name"
"USER": "db_user"
"PASSWORD": "db_password"
```

In this same file, edit the SMTP mail connection, taking into account that SSL and TLS cannot be True at the same time, the default port on many servers for smtp ssl is 465 and for smtp tls it is 587.

```
"EMAIL_USE_SSL": "True",
"EMAIL_USE_TLS": "False",
"EMAIL_BACKEND": "django_smtp_ssl.SSLEmailBackend",
"EMAIL_HOST": "example@domain.com",
"EMAIL_PORT": 465,
"EMAIL_HOST_USER": "example@domain.com",
"EMAIL_HOST_PASSWORD": "example_password",
```

5. Migrate and add data to the database

```bash
python manage.py migrate
python manage.py loaddata initial_data.json
```

6. Run the project

```bash
cd Backend
python manage.py runserver
```
