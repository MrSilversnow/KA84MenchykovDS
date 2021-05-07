drop database if exists autoparts_store;
# создадим базу данных
create database autoparts_store;
use autoparts_store;
# создаем таблицу НоменклатураПоставщиков
create table Supplier_Nomenclature(
	id integer primary key,  # PK
    name varchar(30),  # name of supplier
    country varchar(30),  # name of suplier's country
    type varchar(15)  # type of supplier // дилери, дрібні постачальники і магазини
);
# создаем таблицу НоменклатураПроизводителей
create table Manufacturer_Nomenclature(
	id integer primary key,  # PK
    name varchar(30),  # name of manufacturer
    country varchar(30),  # name of manufacturer's country
    type varchar(15)  # type of manufacturer // фірми, невеликі виробництва
);
# создаем таблицу КаталогДеталей
create table Parts_Catalog(
	id integer primary key,  # PK
    supplier integer,  # FK to Supplier_Nomenclature
    manufacturer integer, # FK to Manufacturer_Nomenclature
    name varchar(30),  # name of part
    price integer,  # price of the part
    foreign key (supplier) references Supplier_Nomenclature (id),
    foreign key (manufacturer) references Supplier_Nomenclature (id)  
);
# создаем таблицу СекцииСклада
create table Warehouse_Sections(
	id integer primary key,  # PK
    alias varchar(30),
    total_size integer,  # size of the warehouse section
    free_size integer  # free size of the warehouse section
);
# создаем таблицу ДеталиНаСкладе
create table Parts_In_Stock(
	id integer,  # FK to Parts_Catalog
    section integer,  # FK to Warehouse_Sections
    number integer,  # number of this parts in the stock
	foreign key (id) references Parts_Catalog (id),
    foreign key (section) references Warehouse_Sections (id)
);
# создаем таблицу БазаКлиентов
create table Clients_Base(
	id integer primary key,  # PK
    name varchar(30),  # first&second client's names
    phone varchar(15)  # client's phone number
);
# создаем таблицу ЗаказыСоСклада
create table Warehouse_Orders(
	id integer primary key,  # PK
    date Date,  # date of order 
    client integer,  # FK to Clients_Base
    part integer,  # FK to Parts_Catalog
    section integer,  # FK to Warehouse_Sections
    number integer,  # number of parts
    foreign key (client) references Clients_Base (id),  
    foreign key (part) references Parts_Catalog (id),
    foreign key (section) references Warehouse_Sections (id)
);
# создаем таблицу ЗаказыУПоставщика
create table Supplier_Orders(
	id integer primary key,  # PK
    date Date,  # date of order
	client integer,  # FK to Clients_Base
    part integer,  # FK to Parts_Catalog
    foreign key (client) references Clients_Base (id), 
    foreign key (part) references Parts_Catalog (id), 
    number integer  # number of parts
);    	
# создаем таблицу ЖурналБрака
create table Defects_Register(
	id integer primary key,  # PK
    part integer,   # FK to Parts_Catalog
    number integer,  # number of defect parts
    foreign key (part) references Parts_Catalog (id)
);