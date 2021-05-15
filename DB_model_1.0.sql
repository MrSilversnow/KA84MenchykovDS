# Создать таблицу НоменклатураПоставщиков
create table Supplier_Nomenclature(
                       id integer primary key auto_increment,  # PK
                       name varchar(30),  # name of supplier
                       country varchar(30),  # name of suplier's country
                       type varchar(15),  # type of supplier
                       time_of_delivery integer,  # time of delivery in days
                       percentage_price integer  # какой процент от нашей цены на деталь мы платим им
);

# Создать таблицу КаталогДеталей
create table Parts_Catalog(
                        id integer primary key auto_increment,  # PK
                        name varchar(30),  # name of part
                        price integer,  # the price at which our store sells the product
                        size integer  # how many 'size' need this part in the Warehouse_Section
);

# Создать таблицу СекцииСклада 
create table Warehouse_Sections(
                        id integer primary key auto_increment,  # PK
                        alias varchar(30),  # псевдоним для складской ячейки, чтобы человеку было удобнее
                        part_type integer,  # FK to Parts_Catalog; показывает, какой товар в этой ячейке хранится
                        total_size integer,  # size of the warehouse section
                        foreign key (part_type) references Parts_Catalog (id)
);

# Создать таблицу ДеталиНаСкладе 
create table Parts_In_Stock(
                        id integer primary key auto_increment,  # PK 
                        section integer,  # FK to Warehouse_Sections
                        number integer,  # number of this parts in the stock
                        supplier integer,  # FK to Supplier_Nomenclature
                        manufacturer integer, # FK to Manufacturer_Nomenclature
                        date Date,  # дата поступления партии на склад 
                        foreign key (section) references Warehouse_Sections (id),
                        foreign key (supplier) references Supplier_Nomenclature (id),
                        foreign key (manufacturer) references Supplier_Nomenclature (id)
);

# Создать таблицу БазаКлиентов
create table Clients_Base(
                        id integer primary key auto_increment,  # PK
                        name varchar(30),  # first&second client's names
                        phone varchar(15)  # client's phone number
);

# Создать таблицу ЗаказыСоСклада (кассовые чеки)
 create table Warehouse_Orders(
                        id integer primary key auto_increment,  # PK
                        date Date,  # date of order 
                        client integer,  # FK to Clients_Base
                        part integer,  # FK to Parts_Catalog
                        section integer,  # FK to Warehouse_Sections
                        number integer,  # number of parts
                        supplier integer,  # FK to Supplier_Nomenclature
                        manufacturer integer, # FK to Supplier_Nomenclature
                        foreign key (client) references Clients_Base (id),  
                        foreign key (part) references Parts_Catalog (id),
                        foreign key (section) references Warehouse_Sections (id),
                        foreign key (supplier) references Supplier_Nomenclature (id),
                        foreign key (manufacturer) references Supplier_Nomenclature (id)
);

# Создать таблицу ЗаказыУПоставщика 
create table Supplier_Orders(
                        id integer primary key,  # PK
                        date Date,  # date of creating order
                        client integer default null,  # FK to Clients_Base
                        part integer,  # FK to Parts_Catalog
                        executed bool default false,  # True if order was executed, else False
                        number integer,  # number of parts
                        supplier integer,  # FK to Supplier_Nomenclature
                        manufacturer integer, # FK to Supplier_Nomenclature
                        foreign key (client) references Clients_Base (id), 
                        foreign key (part) references Parts_Catalog (id), 
                        foreign key (supplier) references Supplier_Nomenclature (id),
                        foreign key (manufacturer) references Supplier_Nomenclature (id)
);

# Создать таблицу НакладныеРасходы 
create table Overheads(
                        id integer primary key,  # PK
                        type varchar(20),  # тип накладного расхода
                        explanation varchar(40),  # дополнительные пояснения по поводу накладного расхода
                        date Date,  # date of spending money
                        money integer  # amount of money
);

# Создать таблицу ЖурналБрака 
create table Defects_Register(
                        id integer primary key auto_increment,  # PK
                        date Date,  # date the entry was created
                        part integer,   # FK to Parts_Catalog
                        supplier integer,  # FK to Supplier_Nomenclature
                        manufacturer integer, # FK to Supplier_Nomenclature
                        client integer,  # FK to Clients_Base
                        number integer,  # number of defect parts
                        foreign key (part) references Parts_Catalog (id),
                        foreign key (supplier) references Supplier_Nomenclature (id),
                        foreign key (manufacturer) references Supplier_Nomenclature (id),
                        foreign key (client) references Clients_Base (id)
);
