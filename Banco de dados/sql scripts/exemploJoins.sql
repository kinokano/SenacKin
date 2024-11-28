create database exemploJoins;
use exemploJoins;

create table clientes(
	clienteID int primary key,
    nome varchar(50)
);

create table pedidos(
	pedidoId int primary key,
    clienteId int,
    dataPedido date,
    foreign key (clienteId) references clientes(clienteId)
);

create table categorias(
	categoriaId int primary key,
    nomeCategorias varchar(50)
);

create table produtos(
	produtoId int primary key,
    nomeProduto varchar(50),
    categoriaId int,
    preco decimal(10,2),
    foreign key (categoriaId) references categorias(categoriaId)
);

create table detalhesPedidos(
	detalheId int primary key,
    pedidoId int,
    produtoId int,
    quantidade int,
    foreign key (pedidoId) references pedidos(pedidoId),
    foreign key (produtoId) references produtos(produtoId)
);

insert into clientes(clienteId, nome) values (1, 'João'), (2,'Maria'),
(3,'Carlos'),(4,'Ana');

insert into pedidos(pedidoId, clienteId, dataPedido) values 
(101,1,'2023-01-10'),
(102,2,'2023-01-15'),
(103,3, '2023-02-05'),
(104,2,'2023-02-10');

insert into categorias (categoriaId, nomeCategorias) values
(1,'Roupas'),
(2,'Acessórios');

insert into produtos (produtoId, nomeProduto, categoriaId, preco) values
(201,'Camiseta',1,29.99),
(202,'Calça Jeans',1,39.99),
(203,'Tênis',2,59.99),
(204,'Boné',2,19.99);

insert into detalhesPedidos (detalheId, pedidoId, produtoId, quantidade) values
(1,101,201,2),
(2,101,203,1),
(3,102,202,1),
(4,103,204,3);

#Exercicio 1
select c.nome, p.pedidoId from clientes c join pedidos p on c.clienteId = p.clienteId;

#Exercicio 2
select p.nomeProduto, d.pedidoId, d.quantidade from produtos p left join detalhesPedidos d on p.produtoId = d.produtoId;

#exercicio 3
select p.pedidoId, p.dataPedido, c.nome from pedidos p left join clientes c on c.clienteId = p.clienteId;

#exercicio 4
select p.nomeProduto, c.nomeCategorias from produtos p join categorias c on c.categoriaId = p.categoriaId;

#exercicio 5
select p.pedidoId, p.clienteId, p.dataPedido, d.produtoId, d.quantidade from pedidos p left join detalhesPedidos d on d.pedidoId = p.pedidoId;

#exercicio 6
select c.nomeCategorias, p.nomeProduto from categorias c left join produtos p on p.categoriaId = c.categoriaId;

#exercicio 7
select d.detalheId, d.produtoId, d.quantidade, p.nomeProduto from detalhesPedidos d left join produtos p on d.produtoId = p.produtoId;

#exercicio 8 
select p.nomeProduto from produtos p left join detalhesPedidos d on d.produtoId = p.produtoId;

#exercicio 9
select c.nomeCategorias, p.nomeProduto from categorias c join produtos p on c.categoriaId = p.categoriaId;

