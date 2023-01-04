
-- Un comentario se crea con '--' ^-^
-- Asi se crea una base de datos
-- No imporat CreatE IGUAL FUNCIONA	
CREATE DATABASE IF NOT EXISTS practicas;

-- Indicamos que vamos a usar la bd
USE practicas;


-- Ahora vamos a crear nustrea primera table
-- TIPOS DE DATOS https://dev.mysql.com/doc/refman/8.0/en/data-types.html
-- Doc de como crear una tabla https://dev.mysql.com/doc/refman/8.0/en/create-table.html
-- La lleva primaria señala que no se puede repetir
CREATE TABLE usuarios(
-- nombre datatype [cofig__adic]
	id INT          auto_increment unique PRIMARY KEY,
    nombre TEXT     NOT NULL,
    dni CHAR(8) UNIQUE
);

-- cuando no entra, nos vamos a mysql80 y le damos en iniciar

create table tareas(
	id 			INT 	auto_increment primary key,
    titulo  	varchar(100) 	unique,
    descripcion text,
    usuario_id INT,
    -- Creo la relacion entre las tablas
    -- en foreing digo que prop de mi tabla va tener el foreign key
    -- el reference señala que columna de la tb usuarios me voy a jalar
    foreign key (usuario_id) references usuarios(id)
);

-- sub lenguajes
-- DDL (DATA DEFINITION LANGUAGE)
-- Eliminar tablas bd, crear tb
-- 	 Create (crear)
--	ALTER (actualizar)
--  DROP (ELIMINAR TODO)
-- DML  (DATA MANIPULATE LANGUAGE)
-- es un lng que sirve que para definir la infromacion que ira dentro de las estructuras
-- insertar datos, actualizar datos, eliminar datos y leer datos
-- INSERT (insertar)
-- select (visualizar)
-- upadte (actualizar)
-- delete (eliminar)

insert into usuarios (nombre, dni) values ('Arnold', '70036504');

insert into usuarios (id, nombre, dni) values(default, 'Juana', '12345678');

-- Si queremos ingresar varios registros
insert into usuarios (id, nombre, dni) values(default, 'Diego', '12345671'), 
											(default, 'Pablo', '12345679'),
											(default, 'Vicente', '12345670');

insert into tareas(id, titulo, descripcion, usuario_id) values(default, 'Ir a la playa', 'Ire a la playa fin de semana', 1),
															  (default, 'Ir a la piscina', 'Ire a la piscina a mis clases de natacion', 2);

-- Esto sirve para visualizar la informacion
select nombre from usuarios;
-- Visualizar todas las columnas
select * from usuarios;

insert into usuarios(id, nombre, dni) values (default, 'Juana','01234567'), (default, 'Pablo','01234667');

select * from usuarios;

select * from usuarios where nombre = 'Juana';

select * from usuarios where nombre = 'Juana' and id =2;

-- Visualizar todas las tareas del usuario 1
select * from tareas where usuario_id = 1 or usuario_id = 2;

INSERT INTO tareas (id, titulo, descripcion, usuario_id) VALUES (DEFAULT, 'Ir a comer', 'Comer un sabroso pollito a la brasa', 1),
                                                                (DEFAULT, 'Comer pizza', 'Comer una sabrosa pizza con peperoni', 1);
                                                                
select * from tareas where usuario_id = 1;

select * from tareas where usuario_id = 1 and titulo like '%comer%';
							
-- Si queremos hacer la distincion entre mays y min antes de colocar el texto usaremos
-- BINARY y esto sirve para que compare a nivel de numeros de caracteres usando el ASCII
select * from usuarios where nombre like binary 'a%'; 

-- Con el '_' indico cuantos caracteres debe de saltar, para que busque el caracter indicado
select * from usuarios where nombre like binary '_r%';

select * from tareas;

-- inner join, es como juntar ambas tablas

INSERT INTO tareas (id, titulo, descripcion, usuario_id) VALUES (DEFAULT, 'no hacer nada', 'no hacer nada porque es domingo', null);

select * from tareas;

insert into tareas (id, titulo, descripcion, usuario_id) VALUES (DEFAULT, 'Jugar LOL', 'Jugar con mis amigos pros', 3);

-- interesecion entre usuarios y tareas donde id sea igual a usuario_id
select * from usuarios INNER JOIN tareas ON usuarios.id = tareas.usuario_id;
-- Trae a toda la tabla usuarios y me muestra que tareas tienen y si no tiene sale null
select * from usuarios left join tareas ON usuarios.id = tareas.usuario_id;
-- Trae a la tabla tareas a todo y me muestra al id y su nombre 
select * from usuarios right join tareas ON usuarios.id = tareas.usuario_id;

-- Full outer join 
select * from usuarios left join tareas ON usuarios.id = tareas.usuario_id UNION
select * from usuarios right join tareas ON usuarios.id = tareas.usuario_id;

-- UNION mezcla las 2 o mas consultas en una sola tabla virtual pero estas consultas tienen
-- que tener el mismo numero de columans, sino la union es incorrecta
SELECT id from usuarios UNION
SELECT titulo from tareas;

-- CONCACTENAR > juntar combinar
select concat(titulo,' ', descripcion) AS 'Nombre Completo' FROM tareas;

-- 1. Devolver todos los usuarios cuyo DNI contengan el numero 5
Select * from usuarios where dni like '%5%';
-- 2. Devolver todos los usuarios cuyo DNI tengan el tercer digito 8
Select * from usuarios where dni like '__0%';
-- 3. Devolver todas las tareas del usuario 'Eduardo'
select * from usuarios INNER JOIN tareas ON usuarios.id = tareas.usuario_id where nombre = 'Eduardo';
