.open eggs.db

create table trainers(
	t_id int primary key not null,
	t_username char(32) not null 
) without rowid;

create table eggs(
	trainer_id integer not null,
	pokemon integer not null,
	distance integer not null,
	timestamp datetime default current_timestamp not null,
	foreign key(trainer_id) references trainer(t_id)
);