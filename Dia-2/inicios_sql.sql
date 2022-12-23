
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

