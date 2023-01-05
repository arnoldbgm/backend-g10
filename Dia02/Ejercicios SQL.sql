-- 1. CREAR UNA BASE DE DATOS LLAMADA MINIMARKET
CREATE DATABASE minimarket;
-- 2. CREAR UNA TABLA LLAMADA PRODUCTOS en la cual tengamos lo siguiente:
-- id entero llave primaria y auto incrementable
-- nombre text
-- imagen text
-- fecha_vencimiento date
-- precio float
-- disponible boolean defecto (verdadero)
use minimarket;

create table productos(
	id int primary key auto_increment,
    nombre text,
    imagen text,
    fecha_vencimiento date,
    precio float,
    disponible boolean default true,
    categoria_id  int,
    foreign key (categoria_id) references categoria(id)
);
-- 3. CREAR UNA TABLA LLAMADA CATEGORIA:
-- id entero llave primaria y auto incrementable
-- nombre text
create table categoria(
	id int primary key auto_increment,
    nombre text
);

-- 4. CREAR UNA TABLA LLAMADA ALMACEN en la cual seria de la sgte manera:
-- id entero llave primaria y auto incrementable
-- nombre text
-- direccion text
create table almacen(
	id int primary key auto_increment,
    nombre text,
    direccion text
);

-- Una categoria puede tener varios productos pero un producto pertenece a una sola categoria

-- TIP: COMO MODIFICAR LA TABLA PARA AGREGAR UNA KEY
alter table productos add column categoria_id int;
alter table productos add foreign key (categoria_id) references categoria(id);	

-- Un prodcuto puede estar en varios almacenes y a su vez cada almacen puede tener varios productos

create table almacen_producto(
	id int primary key auto_increment,
    almacen_id int not null,
    producto_id int not null,
    foreign key (almacen_id) references almacen(id),
    foreign key (producto_id) references productos(id)
);

INSERT INTO categoria (id, nombre) VALUES     (DEFAULT, 'Frutas'), 
                                            (DEFAULT, 'Legumbres'), 
                                            (DEFAULT, 'Snacks'),
                                            (DEFAULT, 'Otros');

INSERT INTO productos (id, nombre, imagen, fecha_vencimiento, precio, disponible, categoria_id) VALUES (DEFAULT, 'Lechuga Carola', 'https://google.com','2022-01-10',2.90, true, 2),
                                                                                                       (DEFAULT, 'Beterraga', 'https://google.com','2022-02-14',1.90, true, 2),
                                                                                                       (DEFAULT, 'Papitas fritas', 'https://google.com','2025-01-10',2.90, true, 3),
                                                                                                       (DEFAULT, 'Platano de seda', 'https://google.com','2022-01-10',4.75, true, 1),
                                                                                                       (DEFAULT, 'Short playero', 'https://google.com','2022-12-31',39.90, true, 4),
                                                                                                       (DEFAULT, 'Mandarina', 'https://google.com','2022-05-23',2.90, true, 1);
                                                                                                       
INSERT INTO almacenes (id, nombre, direccion ) VALUES (DEFAULT, 'ALMACEN A', 'Calle los ruiseñores 1080'),
                                                      (DEFAULT, 'ALMACEN B', 'Calle los girasoles 570'),
                                                      (DEFAULT, 'ALMACEN C', 'Av Venezuela 3040');

INSERT INTO almacen_producto (id, almacen_id, producto_id) VALUES (DEFAULT, 1, 1),
                                                                  (DEFAULT, 1, 2),
                                                                  (DEFAULT, 2, 2),
                                                                  (DEFAULT, 2, 3),
                                                                  (DEFAULT, 3, 4),
                                                                  (DEFAULT, 1, 5),
                                                                  (DEFAULT, 2, 6),
                                                                  (DEFAULT, 3, 5);																								
                                                                  
-- Ejercicios
-- 1. Mostrar todos los productos que tenga n un precio mayor o igual a 3
SELECT * FROM productos where precio >= 3;
-- 2. Mostrar todos los productos cuya fecha de vencimiento sea menor al 1  de agosto del 2022
SELECT * FROM productos where fecha_vencimiento < '2022-08-01';
-- 3. Mostrar los nombres de los productos concatenados con su url de imagen en una sola columna que se llame producto
SELECT CONCAT(nombre,'',imagen) AS 'Producto imagen' from productos;

-- 4. Devolver todos los prd de la catf 'Frutas'
SELECT * FROM categorias INNER JOIN productos ON categorias.id = productos.categoria_id WHERE categorias.nombre = 'Frutas';
-- 5. Devolver el nombre de la categoria, nombre del producto y el precio del producto si es mayor que 10
SELECT categorias.nombre, productos.nombre, productos.precio FROM categorias INNER JOIN productos ON categorias.id = productos.categoria_id WHERE  productos.precio > 10;
-- 6. Devolver los almacenes con sus productos
SELECT almacenes.*, productos.* FROM almacen_producto INNER JOIN almacenes ON almacenes.id = almacen_producto.almacen_id INNER JOIN productos ON almacen_producto.producto_id = productos.id;

-- 7. Mostrar lo sgt
SELECT categorias.nombre, productos.nombre, productos.precio, almacenes.nombre, almacenes.direccion from productos 
		inner join categorias on productos.categoria_id = categorias.id
        inner join almacen_producto on almacen_producto.producto_id = productos.id
        inner join almacenes on almacenes.id = almacen_producto.almacen_id;