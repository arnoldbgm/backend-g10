## CREAR EL ENTORNO VIRTUAL

```py
 python -m venv venv
```

## ACTIVAR EL ENTORNO VIRTUAL

```py
source venv/Scripts/activate
```

## Instalamos django
```py
pip install django
```
## Ahora creamos nuestro proyecto con django
Creamos el proyecto con el nombre "django_intro"
```py
django-admin startproject django_intro
```
Ahora corremos django
```py
python manage.py runserver
```

## Migrar los modelos
```
python manage.py migrate
```

## Crear un superusuario 

```py
python manage.py createsuperuser
```

## Crear una app

```py
python manage.py startapp "nombre"
```

## Registramos nuestra app en INSTALLED_APPS

```py
INSTALLED_APPS = [
    ...,
    'almacen'
]
```

## Crear nuestro nuevo model y migrar
```
python manage.py makemigrations
python manage.py migrate
```

## Aora instalamos Django Rest Framework

```py
pip install djangorestframework
```

## Agregar DRF a INSTALLED_APPS

```py
INSTALLED_APPS = [
    ...,
    'rest_framework'
]
```


## Documentar nuestra API con Swagger y Redoc

```py
pip install drf-yasg
```

## Configuramos `drf-yasg`
```py
```