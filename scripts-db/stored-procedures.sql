------ stored procedures
--- productos

drop procedure insertar_producto;

DELIMITER //
create procedure insertar_producto(in _nombre varchar(50), in _tamaño varchar(50), in _sabor varchar(50), in _precio int(11))
begin
    INSERT INTO productos (nombre, tamaño, sabor, precio)
    VALUES (_nombre, _tamaño, _sabor, _precio);
end//


call insertar_producto('Brownie', 'Grande', 'Vainilla', 100);




drop procedure eliminar_producto;

DELIMITER //
create procedure eliminar_producto(in _id int)
begin
    DELETE FROM productos where id = _id;
end//

call eliminar_producto(4);