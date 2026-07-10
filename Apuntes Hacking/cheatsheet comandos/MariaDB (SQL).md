# MariaDB Cheatsheet

## Servicios y acceso

| Comando                 | Descripción                                       |
| ----------------------- | ------------------------------------------------- |
| `service mysql start`   | Inicia servicio de mysql                          |
| `service apache2 start` | Inicia servicio de apache                         |
| `sudo mysql -u root`    | Entrar en la consola de MariaDB como usuario root |

## Bases de datos

| Comando | Descripción |
|---|---|
| `show databases;` | Muestra las bases de datos |
| `use [nombre];`<br>`use mysql;` | Usar una bd<br>Usar la bd de mysql |
| `create database [nombre];`<br>`create database SQLI;` | Crea una base de datos<br>Crea una base de datos llamada SQLI |
| `drop database [nombre];`<br>`drop database SQLI;` | Elimina una base de datos completa<br>Elimina la base de datos SQLI |

## Tablas

| Comando | Descripción |
|---|---|
| `show tables;` | Muestra las tablas de la bd actual |
| `describe [tabla];`<br>`describe user;` | Ver la descripción/estructura de una tabla<br>Ver la descripción de la tabla user |
| `create table [nombre]([valores]);`<br>`create table users(id int(32), username varchar(32), password varchar(32));` | Crea una tabla con sus columnas y tipos de dato<br>Crea la tabla users con columnas id, username, password |
| `alter table [tabla] add [campo] [tipo];`<br>`alter table users add email varchar(64);` | Agrega una nueva columna a una tabla existente<br>Agrega la columna email a users |
| `alter table [tabla] drop column [campo];`<br>`alter table users drop column email;` | Elimina una columna de una tabla<br>Elimina la columna email de users |
| `alter table [tabla] modify [campo] [nuevo_tipo];`<br>`alter table users modify username varchar(64);` | Cambia el tipo de dato de una columna<br>Cambia username a varchar(64) |
| `alter table [tabla] rename to [nuevo_nombre];`<br>`alter table users rename to usuarios;` | Renombra una tabla<br>Renombra users a usuarios |
| `drop table [tabla];`<br>`drop table users;` | Elimina una tabla completa (estructura y datos)<br>Elimina la tabla users |

## Consultas (SELECT)

| Comando | Descripción |
|---|---|
| `select [campo1][, campo2] from [tabla];`<br>`select user,password from user;` | Selecciona una o más columnas de una tabla<br>Selecciona user y password de la tabla user |
| `select * from [tabla];`<br>`select * from users;` | Selecciona todos los campos de una tabla<br>Selecciona la tabla users completa |
| `select [campo] from [tabla] where [campo]='[valor]';`<br>`select user,password from user where user = 'root';` | Busca un valor específico en una columna<br>Muestra user y password del usuario "root" |
| `select * from [tabla] where [campo] like '%valor%';`<br>`select * from users where username like '%admin%';` | Busca coincidencias parciales en un campo<br>Busca usernames que contengan "admin" |
| `select * from [tabla] where [campo] in ([valor1],[valor2]);`<br>`select * from users where id in (1,2,3);` | Busca registros que coincidan con varios valores<br>Muestra usuarios con id 1, 2 o 3 |
| `select * from [tabla] where [campo] between [valor1] and [valor2];`<br>`select * from users where id between 1 and 10;` | Busca registros dentro de un rango<br>Muestra usuarios con id entre 1 y 10 |
| `select * from [tabla] where [campo] is null;`<br>`select * from users where email is null;` | Busca registros donde un campo esté vacío (nulo)<br>Muestra usuarios sin email |
| `select * from [tabla] where [campo] is not null;`<br>`select * from users where email is not null;` | Busca registros donde un campo NO esté vacío<br>Muestra usuarios con email registrado |
| `select distinct [campo] from [tabla];`<br>`select distinct username from users;` | Muestra valores únicos, sin repetir<br>Muestra usernames sin duplicados |
| `select * from [tabla] order by [campo] asc/desc;`<br>`select * from users order by id desc;` | Ordena resultados ascendente o descendente<br>Muestra usuarios ordenados por id descendente |
| `select * from [tabla] limit [n];`<br>`select * from users limit 5;` | Limita el número de resultados mostrados<br>Muestra solo los primeros 5 registros |
| `select count(*) from [tabla];`<br>`select count(*) from users;` | Cuenta el número de registros<br>Cuenta cuántos usuarios hay |
| `select [campo], count(*) from [tabla] group by [campo];`<br>`select username, count(*) from logins group by username;` | Agrupa resultados y cuenta por grupo<br>Cuenta cuántos logins tiene cada username |

## Modificación de datos (INSERT / UPDATE / DELETE)

| Comando                                                                                                                                                         | Descripción                                                                                |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| `insert into [tabla]([campo1],[campo2]...) values ([valor1],[valor2]...);`<br>`insert into users(id, username, password) values(1, 'admin', 'admin123$!p@$$');` | Inserta datos en las columnas de una tabla<br>Inserta id, username y password en users     |
| `update [tabla] set [campo]=[valor] where [campo2]=[valor2];`<br>`update users set id = 2 where username = 'FabCA06';`                                          | Modifica un registro de una tabla<br>Modifica el id del usuario FabCA06                    |
| `delete from [tabla] where [campo] = [valor];`<br>`delete from users where username = 'FabCA06';`                                                               | Elimina un registro de una tabla<br>Elimina el registro donde username = FabCA06           |
| `truncate table [tabla];`<br>`truncate table users;`                                                                                                            | Elimina todos los registros de una tabla, sin borrar la estructura<br>Vacía la tabla users |

## Usuarios y privilegios

| Comando | Descripción |
|---|---|
| `create user '[nombre]'@'[ip]' identified by '[contraseña]';`<br>`create user 'FabCA06'@'localhost' identified by 'FABRICIO06';` | Crea un usuario con contraseña para acceder al servidor<br>Crea el usuario FabCA06 con contraseña FABRICIO06 |
| `grant all privileges on [base_de_datos].* to '[nombre]'@'[ip]';`<br>`grant all privileges on SQLI.* to 'FabCA06'@'localhost';` | Da todos los permisos a un usuario sobre una bd<br>Da todos los permisos a FabCA06 en la bd SQLI |
| `grant select,insert on [base_de_datos].* to '[nombre]'@'[ip]';`<br>`grant select,insert on SQLI.* to 'FabCA06'@'localhost';` | Da permisos específicos a un usuario<br>Da permisos de select e insert a FabCA06 |
| `revoke all privileges on [base_de_datos].* from '[nombre]'@'[ip]';`<br>`revoke all privileges on SQLI.* from 'FabCA06'@'localhost';` | Quita permisos a un usuario<br>Quita todos los permisos a FabCA06 en SQLI |
| `flush privileges;` | Recarga los privilegios para que los cambios surtan efecto |
| `show grants for '[nombre]'@'[ip]';`<br>`show grants for 'FabCA06'@'localhost';` | Muestra los privilegios de un usuario<br>Muestra los privilegios de FabCA06 |
| `drop user '[nombre]'@'[ip]';`<br>`drop user 'FabCA06'@'localhost';` | Elimina un usuario<br>Elimina al usuario FabCA06 |
| `select user();` | Muestra el usuario actualmente conectado |
| `select version();` | Muestra la versión de MariaDB |

## Utilidades varias

| Comando | Descripción |
|---|---|
| `status;` | Muestra el estado de la conexión y del servidor |
| `\q` o `exit;` | Sale de la consola de MariaDB |
| `source [ruta_archivo.sql];` | Ejecuta un archivo .sql (útil para importar dumps) |
| `mysqldump -u [usuario] -p [bd] > backup.sql` | Exporta (respalda) una base de datos a un archivo .sql (desde la terminal, no desde la consola de MariaDB) |
| `mysql -u [usuario] -p [bd] < backup.sql` | Importa una base de datos desde un archivo .sql (desde la terminal) |