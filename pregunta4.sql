-- 1. Left join entre Shippings y Orders
SELECT o.*, s.*
FROM Orders o
LEFT JOIN Shippings s ON o.customer_id = s.customer;

-- 2. Filtrar Customers con edad entre 21 y 28
SELECT *
FROM Customers
WHERE age >= 21 AND age <= 28;

-- 3. Filtrar Orders donde item comienza con 'K'
SELECT *
FROM Orders
WHERE item LIKE 'K%';

-- 4. Crear tabla clientes
CREATE TABLE clientes (
    id INT PRIMARY KEY,
    nombre_cliente VARCHAR(100),
    edad_cliente INT,
    area_del_cliente VARCHAR(100),
    fecha_inicio DATE
);
