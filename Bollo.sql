create table Bollo(
	PLATE_NO varchar(20) not null primary key,
	DEPARTEMENT varchar(20) not null,
  	REMARK varchar(250) not null
);

-- test data

insert into Bollo(PLATE_NO,DEPARTEMENT,remark) values('12-23sas','bole','have broken the window')



-- update remark


create table updateBollo(
	REMARK_DATE varchar(19) not null primary key,
  	REMARK varchar(250) not null,
  	PLATE_NO varchar(20) not null,
	foreign key (PLATE_NO) references Bollo(PLATE_NO)

);


-- don't forget the foreign key must exist to be used


insert into updateBollo(remark_date,remark,plate_no) values('2023-08-29 21:07:57','hello','3AAA32')


-- getting date data

select  REMARK_DATE from updateBollo where PLATE_NO='' 


