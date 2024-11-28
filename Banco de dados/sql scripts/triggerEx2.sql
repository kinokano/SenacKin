create database triggerEx2;
use triggerEx2;

CREATE TABLE Total_Vendas (
 id_total_vendas INT PRIMARY KEY, 
total DECIMAL(10, 2)
);

CREATE TABLE Produtos ( 
id_produto INT PRIMARY KEY, 
nome VARCHAR(100), 
quantidade INT, 
preco DECIMAL(10, 2) 
);

CREATE TABLE Vendas(
 id_venda INT PRIMARY KEY, 
fk_id_produto INT, 
valor DECIMAL(10, 2), 
FOREIGN KEY (fk_id_produto) REFERENCES
Produtos(id_produto)
);

delimiter ||
create trigger attValorVenda after update 
on vendas
for each row 
begin 
	update total_vendas set total = new.valor;

end;
||
delimiter ;

insert into produtos values (1, 'teste', 1, 9.99);
insert into vendas values(1,1, 9.99);
insert into total_vendas values (1, 9.99);

update vendas set valor = 33.33 where id_venda = 1;
select * from total_vendas;






