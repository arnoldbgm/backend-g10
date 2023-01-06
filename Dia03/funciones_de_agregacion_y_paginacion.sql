-- FUNCIONES DE AGREGACION
-- Funciones que permiten efectuar operaciones sobre algunas columnas para obtener resultados
-- https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html
USE minimarket;

SELECT * FROM productos;

-- Para realizar cualqr fnc se tiene que usar GROUP BY servira para indicar
-- como queremos que se realize la agrupacion
-- AVG (columna)
-- Aqui se agrupa por grupos y no te lanza de golpe
SELECT categoria_id, avg(precio) 
FROM productos
group by categoria_id;

-- MAX (columna)
SELECT categoria_id, max(precio) 
from productos;

-- MIN (columna)
SELECT min(precio)
from productos;

-- COIUNT(columna)
SELECT COUNT(precio)
FROM productos;

-- SUM (columna)
SELECT SUM(precio)
FROM productos;

-- PAGINACION
-- Aqui limitamos y señalamos cuantos queremos jalar y desde cuantos queremos que se salte
SELECT * FROM productos 
LIMIT 2
OFFSET 2;