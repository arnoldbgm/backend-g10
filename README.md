## Correr la aplicacion

Para corre r la aplicacion de flask ejecutamos

```
flask --debug run
```

## Para ejecutar las migraciones

```py
#Crear la carpeta mitraciones solo se ejecuta una vez
flask db init
flask db migrate -m "Comentario"
flask db upgrade
```
