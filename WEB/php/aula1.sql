create database aulaPhp;
use aulaPhp;



create table Usuario(
	id int not null primary key auto_increment,
	nome varchar(50) not null,
	senha varchar(100) not null
);


insert into usuario(nome, senha) values ("Kin", "123");
select * from usuario;
