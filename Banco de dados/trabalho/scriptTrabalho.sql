CREATE DATABASE Sistema;
USE Sistema;

CREATE TABLE Usuarios(
	id int not null auto_increment primary key,
    nome VARCHAR(255) NOT NULL,
    login VARCHAR(255) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL
);

CREATE TABLE Produtos(
	id int not null auto_increment primary key,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    estoque int not null,
    valor decimal(10,2) not null
);

CREATE TABLE Vendas(
	id int not null auto_increment primary key,
    idVendedor int not null,
    foreign key (idVendedor) references Usuarios(id),
    nomeCliente VARCHAR(255) NOT NULL,
    cpf VARCHAR(14) NOT NULL,
    endereco TEXT NOT NULL,
    formaPagamento ENUM('à vista', 'parcelado') NOT NULL,
    idProduto INT NOT NULL,
    foreign key (idProduto) references Produtos(id),
    entrada DECIMAL(10,2) DEFAULT 0,
    quantidadeParcelas INT DEFAULT 0,
    valorParcela DECIMAL(10,2) DEFAULT 0,
    quantidade INT NOT NULL,
    valorTotal DECIMAL(10, 2) NOT NULL,
    dataVenda DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP

);


delimiter ||

CREATE TRIGGER TotalVenda
BEFORE INSERT ON Vendas
FOR EACH ROW
BEGIN
    DECLARE valor_produto DECIMAL(10,2);

    -- Buscar o valor do produto na tabela Produto
    SELECT valor INTO valor_produto
    FROM Produtos
    WHERE id = NEW.idProduto;

    -- Calcular o total e atribuir ao campo 'total'
    SET NEW.valorTotal = valor_produto * NEW.quantidade;
    
   
   IF NEW.formaPagamento =  'à vista' THEN
        SET NEW.entrada = NEW.valorTotal;
    END IF;
    
    IF NEW.formaPagamento =  'parcelado' THEN
		SET NEW.valorParcela = (NEW.valorTotal- NEW.entrada)/NEW.quantidadeParcelas;
    END IF;
    
END;

CREATE TRIGGER AtualizarEstoque
AFTER INSERT ON Vendas
FOR EACH ROW
BEGIN
    
    UPDATE Produtos
    SET estoque = estoque - NEW.quantidade
    WHERE id = NEW.idProduto;
    
    
END;

||
DELIMITER ;

INSERT INTO Usuarios(nome, login, senha) Values ('admin','admin','admin'),('vendedor1','vendedor1','vendedor1'),('vendedor2','vendedor2','vendedor2'),('vendedor3','vendedor3','vendedor3');
SELECT * FROM Usuarios;
INSERT INTO Produtos(nome, descricao, estoque, valor) VALUES ('AGUA', 'GARRAFA DE AGUA', 20, 2.99),("CHOCOLATE","BARRA DE CHOCOLATE", 50, 5.99),("BOLACHA", "BOLACHA PASSATEMP", 60, 3.99);
SELECT * FROM Produtos;
INSERT INTO Vendas(idVendedor, nomeCliente, cpf, endereco, formaPagamento, idProduto, quantidade) VALUES (2, 'Calebe','999.999.999-00', 'Rua 12', 'à vista', 1, 2);
INSERT INTO Vendas(idVendedor, nomeCliente, cpf, endereco, formaPagamento, idProduto, entrada, quantidadeParcelas, quantidade) VALUES (3, 'Derek','999.999.999-01', 'Rua 13', 'parcelado', 2, 10.00 ,4, 5);
INSERT INTO Vendas(idVendedor, nomeCliente, cpf, endereco, formaPagamento, idProduto, quantidadeParcelas, quantidade) VALUES (4, 'Arthur','999.999.999-02', 'Rua 14', 'parcelado', 3, 6, 10);
SELECT * FROM Produtos;
SELECT * FROM Vendas;

SELECT u.nome as Vendedor, v.nomeCliente as Cliente, v.cpf as CPF, v.endereco as Endereço, v.formaPagamento as Pagamento, v.quantidadeParcelas as Parcelas, p.nome as Produto, v.quantidade as Quantidade, v.valorTotal as Total, v.dataVenda as DataVenda
FROM Vendas v JOIN Usuarios u ON u.id = v.idVendedor JOIN Produtos p ON p.id = v.idProduto;

SELECT u.nome as Vendedor, v.nomeCliente as Cliente, v.cpf as CPF, v.endereco as Endereço, v.formaPagamento as Pagamento, v.entrada as Entrada, v.quantidadeParcelas as Parcelas, v.valorParcela as ValorParcela,p.nome as Produto, v.quantidade as Quantidade, v.valorTotal as Total, v.dataVenda as DataVenda
FROM Vendas v JOIN Usuarios u ON u.id = v.idVendedor JOIN Produtos p ON p.id = v.idProduto WHERE MONTH(dataVenda) = 12;
