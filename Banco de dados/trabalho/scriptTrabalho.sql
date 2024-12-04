CREATE DATABASE TrabalhoT31;
USE TrabalhoT31;

CREATE TABLE usuarios(
	id int primary key not null auto_increment,
    nome varchar(50) not null unique,
    senha varchar(50) not null
    
);

CREATE TABLE produtos(
	id int primary key not null auto_increment,
    nome varchar(50) not null,
    descricao text,
    estoque int,
    valor decimal(10,2)
);

CREATE TABLE vendas(
	id int primary key not null auto_increment,
    nomeCliente varchar(50) not null,
    cpfCliente varchar(15) not null,
    formaPagamento varchar(10) not null,
    parcelas int,
    idProduto int not null,
    foreign key (idProduto) references produtos(id),
    qtdProduto int,
    idVendedor int not null,     
    foreign key (idVendedor) references usuarios(id),
    dataVenda date,
    valorVenda decimal(10,2) default 0
);


delimiter |

CREATE TRIGGER atualizarQtdProduto
AFTER INSERT ON vendas 
FOR EACH ROW 
BEGIN 
	UPDATE vendas SET valorVenda = (qtdProduto * valor) 
    WHERE idProduto = produtos.id;
	UPDATE produtos SET estoque = (estoque - new.qtdProduto)
	WHERE id = new.idProduto;
END;
|

delimiter ;

INSERT INTO usuarios(nome,senha) VALUES ('admin','admin'), ('vendedor1','vendedor1');
INSERT INTO produtos(nome,descricao,estoque,valor) VALUES ("Garrafa d'água","Garrafa d'água Crystal 500ml", 50, 2.99);
INSERT INTO produtos(nome,descricao,estoque,valor) VALUES ("Chocolate","Chocolate 100gr", 10, 5.99);
INSERT INTO vendas(nomeCliente, cpfCliente, formaPagamento, parcelas, idProduto, qtdProduto, idVendedor, dataVenda) 
VALUES ("Calebe", "000.000.000-00", "À vista", 1, 1,1,2,"2024-12-03");
INSERT INTO vendas(nomeCliente, cpfCliente, formaPagamento, parcelas, idProduto, qtdProduto, idVendedor, dataVenda) 
VALUES ("Calebe", "000.000.000-00", "À vista", 1, 2,2,2,"2024-12-03");

SELECT * FROM produtos;
SELECT * FROM vendas;









