create database triggerEx1;
use triggerEx1;

CREATE TABLE Estatisticas_Postagem (
 id_postagem INT PRIMARY KEY,
 titulo VARCHAR(100),
 contador_comentarios INT DEFAULT 0
);

CREATE TABLE Comentarios (
 id_comentario INT PRIMARY KEY,
 fk_id_postagem INT,
 comentario TEXT,
 FOREIGN KEY (fk_id_postagem) REFERENCES Estatisticas_Postagem(id_postagem)
);

delimiter |
create trigger apagarComentario after delete 
on Comentarios
for each row 
begin 
	update Estatisticas_Postagem set contador_comentarios = (contador_comentarios - 1);
end;
|

delimiter ;

insert into Estatisticas_Postagem values(1,'teste',1);
select * from Estatisticas_Postagem;

insert into Comentarios values(1,1,'teste teste');
select * from Comentarios;

delete from Comentarios where id_comentario = 1;



