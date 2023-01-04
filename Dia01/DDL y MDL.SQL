
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
                                                                G