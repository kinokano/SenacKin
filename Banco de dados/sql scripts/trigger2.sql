create database aulaTrigger2;

use aulaTrigger2;


create table produtos(
	referencia varchar(3) primary key,
    descricao varchar(50) unique,
    estoque int not null default 0

);

insert into produtos values ('001','Feijão',10);
insert into produtos values ('002','Arroz',5);
insert into produtos values ('003','Farinha',15);

create table itensvenda(
	venda int primary key,
    produto varchar(3),
    quantidade int not null

);

insert into itensvenda values(1,'001',3),(2,'002',1),(3,'003',5);

delimiter //
create trigger compra after insert
on itensvenda
for each row
begin 
	update produtos set estoque = (estoque - new.quantidade)
    where referencia = new.produto;
end;

create trigger deletar_compra after delete
on itensvenda 
for each row
begin
	update produtos set estoque = (estoque + old.quantidade)
    where referencia = old.produto;

end;
//
delimiter ;

select * from itensvenda;
select * from produtos;

delete from itensvenda where venda = 1;