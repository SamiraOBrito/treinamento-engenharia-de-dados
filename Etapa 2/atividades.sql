-- Atividade 1 - Listar os nomes e cidades de todos os clientes em uma só consulta

SELECT nome, cidade FROM Clientes;

-- Atividade 2 - Listar os pedidos com valor acima de R$100
SELECT id_pedido, valor FROM Pedidos WHERE valor > 100; 

-- Atividade 3 - Listar os pedidos ordenados pelo valor (decrescente)
SELECT * FROM Pedidos ORDER BY valor DESC;

-- Atividade 4 - Listar os 3 primeiros produtos cadastrados
SELECT * FROM Pedidos ORDER BY data_pedido ASC LIMIT 3;

-- Atividade 5 - Listar o total de valor gasto por cada cliente em pedidos.
SELECT id_cliente, SUM(valor) AS total_gasto FROM Pedidos GROUP BY id_cliente;

-- Atividade 6 - Encontrar o cliente com o maior valor gasto
SELECT id_cliente, SUM(valor) AS total_gasto
FROM Pedidos
GROUP BY id_cliente
ORDER BY total_gasto DESC
LIMIT 1;

-- Atividade 7 - Utilizar CTE para calcular o total de vendas por produto
WITH TotalVendas AS (
    SELECT id_pedido, SUM(valor) AS total_vendido
    FROM Pedidos
    GROUP BY id_pedido
)
SELECT * FROM TotalVendas;

-- Atividade 8 - Listar todos os produtos comprados por cada cliente
SELECT 
	c.nome,
	p.nome_produto,
	SUM(ip.quantidade) AS Qtd_Produtos
FROM Pedidos pd
INNER JOIN ItensPedido ip ON pd.id_pedido = ip.id_pedido 
INNER JOIN Produtos p ON ip.id_produto = p.id_produto
INNER JOIN Clientes c ON pd.id_cliente = c.id_cliente 
GROUP BY p.nome_produto, c.nome
ORDER BY c.id_cliente; 
-- Atividade 9 - Ranquear clientes pelo valor total gasto começando pelo rank 1 para o maior valor.
SELECT 
    id_cliente, 
    SUM(valor) AS total_gasto,
    RANK() OVER (ORDER BY SUM(valor) DESC) AS ranking
FROM Pedidos
GROUP BY id_cliente;

-- Atividade 10 - Número de pedidos por cliente, considerando apenas aqueles com mais de 1 pedido
SELECT 
    c.id_cliente, 
    c.nome, 
    COUNT(DISTINCT p.id_pedido) AS total_pedidos
FROM Clientes c
JOIN Pedidos p ON c.id_cliente = p.id_cliente
JOIN ItensPedido ip ON p.id_pedido = ip.id_pedido
GROUP BY c.id_cliente, c.nome
HAVING COUNT(DISTINCT p.id_pedido) > 1
ORDER BY total_pedidos DESC;

-- Atividade 11 - Calcular para cada cliente a quantidade de dias entre um pedido e o pedido imediatamente anterior
SELECT 
    id_cliente,
    id_pedido,
    data_pedido,
    LAG(data_pedido) OVER (PARTITION BY id_cliente ORDER BY id_pedido) AS qtd_dias_pedido_anterior
FROM Pedidos;
-- Atividade 12 - Crie uma consulta que retorne um relatórios contedo as seguintes colunas (obs: use o padrão que preferir para nomear as colunas)

WITH PrecoSemDesconto AS (
    SELECT 
        ip.id_pedido, 
        SUM(ip.quantidade * pr.preco) AS preco_sem_desconto
    FROM ItensPedido ip
    JOIN Produtos pr ON ip.id_produto = pr.id_produto
    GROUP BY ip.id_pedido
)






