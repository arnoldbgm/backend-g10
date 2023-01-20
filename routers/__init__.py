# Creacion de un modulo para llamar a los rutas en todo el sistema
from os import listdir
from pathlib import Path

path_parent = Path("./routers")

for module in listdir(path_parent):
    if 'router' in module:
        __import__(
            # El -3 es por que en la salida sale
            # module.categorias-router.py 
            # Y el -3 hace que salga sin el .py
            # module.categorias-router
            f'routers.{module[0:-3]}',
            locals(),
            globals()
        )