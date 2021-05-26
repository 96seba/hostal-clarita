
--CREACIÓN DEL ESQUEMA

create user c##clarita identified by clarita;
grant connect, resource to c##clarita;
alter user c##clarita default tablespace users quota unlimited on users;

