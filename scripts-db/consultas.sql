select * from clientes;

select * from pedidos;


select clientes.nombre, pedidos.descripcion_tematica, pedidos.fecha_pedido, pedidos.fecha_entrega, pedidos_productos.pedido_id, productos.nombre
from clientes, pedidos, pedidos_productos, productos
where clientes.id = pedidos.cliente_id and pedidos.id = pedidos_productos.pedido_id and productos.id = pedidos_productos.producto_id;


select clientes.nombre, pedidos.descripcion_tematica, pedidos.fecha_pedido, pedidos.fecha_entrega, pedidos_productos.pedido_id, productos.nombre, productos.precio
from clientes, pedidos, pedidos_productos, productos
where clientes.id = pedidos.cliente_id and pedidos.id = pedidos_productos.pedido_id and productos.id = pedidos_productos.producto_id;




select clientes.nombre as 'Nombre cliente', pedidos.descripcion_tematica as 'Tematica del pedido', pedidos.fecha_pedido as 'Fecha del pedido', pedidos.fecha_entrega as 'Fecha de entrega', pedidos_productos.pedido_id, productos.nombre 'Nombre del producto', productos.precio as 'Precio del producto'
from clientes, pedidos, pedidos_productos, productos
where clientes.id = pedidos.cliente_id and pedidos.id = pedidos_productos.pedido_id and productos.id = pedidos_productos.producto_id;