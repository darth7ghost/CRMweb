# CRMweb
Es un sistema CRM (Gestión de Relaciones con el Cliente) desarrollado para el curso de Introducción a la Computación y Programación II (IPC2).

## ¿Cómo hacerlo funcionar?
Puedes usar la base de datos ´´´sqlite3´´´ que está ya en funcionamiento, o conectar directamente una base de datos que tengas en MYSQL o PostrgreSQL.
También, para tener una base de datos completamente vacía y desde 0, puedes eliminar el archivo ´´´sqlite3´´´ y crear uno nuevo con el siguiente comando en la consola de tu IDE favorito o CMD/terminal.
> Debes primero acceder a la carpeta en donde está clonado el repositorio, para poder hacer uso de los comandos de Django.
```python
# Crear migraciones a la base de datos:
python manage.py makemigrations

# Crear la base de datos:
python mamage.py migrate

# Inicializar el servidor:
python mamage.py runserver
```

Si la inicialización del servidor se ha realizado sin problemas, deberás acceder a la siguiente dirección en tu navegador de preferencia:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## ¿Cómo se usa?
Lo primero que debes tener, es un superusuario en la base de datos, para poder configurar el panel de administración y obtener todos los permisos que otorga Django.
Para crearlo (si tienes una base de datos vacía) debes hacerlo con el siguiente comando:
> Debes primero acceder a la carpeta en donde está clonado el repositorio, para poder hacer uso de los comandos de Django.
```python
python manage.py createsuperuser
```
Y deberás rellenar los campos que te solicita Django para la creación del superusuario.

#### El CRM funciona de la siguiente manera:
Debes crear a tus propios agentes de ventas. Puedes acceder a ese apartado fácilmente desde el navbar (solo si eres superusuario).
Cuando estés creando un agente, puedes dictarles un nombre de usuario, y un correo electrónico. Te darás cuenta que al crear un nuevo agente, en la consola de tu editor o CMD/terminal te mostrará una contraseña generada automáticamente. Con ella el nuevo usuario podrá acceder al CRM con su nombre de usuario y contraseña.

Una vez creados los agentes, todos los demás apartados quedarán disponibles para crear un entorno de negocios adaptado a tu empresa.

## ¿Cómo obtenerlo?
Puedes obenerlo con el siguiente comando en la consola de tu IDE de preferencia:
```bash
gh repo clone darth7ghost/CRMweb
```
