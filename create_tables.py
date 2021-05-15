from sqlalchemy import create_engine


"""Функции для для добавления таблиц в базу данных autoparts_store."""


def create_supplier_nomenclature(engine):
    """Создать таблицу, содержащую список поставщиков и производителей."""
    engine.execute("""
                   create table Supplier_Nomenclature(
                       id integer primary key auto_increment,  # PK
                       name varchar(30),  # name of supplier
                       country varchar(30),  # name of suplier's country
                       type varchar(15),  # type of supplier
                       time_of_delivery integer,  # time of delivery in days
                       percentage_price integer  # какой процент от нашей цены на деталь мы платим им
                   )
    """)


def create_parts_catalog(engine):
    """Создать таблицу, содержащую номенклатуру автозапчастей."""
    engine.execute("""
                   create table Parts_Catalog(
                        id integer primary key auto_increment,  # PK
                        name varchar(30) unique,  # name of part
                        price integer,  # the price at which our store sells the product
                        size integer  # how many 'size' need this part in the Warehouse_Section
                   )
    """)


def create_warehouse_sections(engine):
    """Создать таблицу, содержащую секции склада."""
    engine.execute("""
                    create table Warehouse_Sections(
                        id integer primary key auto_increment,  # PK
                        alias varchar(30),  # псевдоним для складской ячейки, чтобы человеку было удобнее
                        part_type integer,  # FK to Parts_Catalog; показывает, какой товар в этой ячейке хранится
                        total_size integer,  # size of the warehouse section
                        foreign key (part_type) references Parts_Catalog (id)
                   )
    """)


def create_parts_in_stock(engine):
    """Создать таблицу, содержащую детали на складе."""
    engine.execute("""
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
                   )
    """)


def create_clients_base(engine):
    """Создать таблицу, содержащую информацию о клиентах."""
    engine.execute("""
                    create table Clients_Base(
                        id integer primary key auto_increment,  # PK
                        name varchar(30) unique,  # first&second client's names
                        password varchar(30),  # client's password
                        phone varchar(15)  # client's phone number
                   )
    """)


def create_warehouse_orders(engine):
    """Создать таблицу, содержащую информацию о заказах со склада."""
    engine.execute("""
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
                   )
    """)


def create_supplier_orders(engine):
    """Создать таблицу, содержащую информацию о заказах у поставщиков."""
    engine.execute("""
                    create table Supplier_Orders(
                        id integer primary key auto_increment,  # PK
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
                    ) 
    """)


def create_overheads(engine):
    """Создать таблицу, содержащую информацию о накладных расходах."""
    engine.execute("""
                    create table Overheads(
                        id integer primary key auto_increment,  # PK
                        type varchar(20),  # тип накладного расхода
                        explanation varchar(40),  # дополнительные пояснения по поводу накладного расхода
                        date Date,  # date of spending money
                        money integer  # amount of money
                    ) 
    """)


def create_defects_register(engine):
    """Создать таблицу, содержащую информацию о браке."""
    engine.execute("""
                    create table Defects_Register(
                        id integer primary key auto_increment,  # PK
                        date Date,  # date the entry was created
                        part integer,   # FK to Parts_Catalog
                        supplier integer,  # FK to Supplier_Nomenclature
                        manufacturer integer, # FK to Supplier_Nomenclature
                        number integer,  # number of defect parts
                        foreign key (part) references Parts_Catalog (id),
                        foreign key (supplier) references Supplier_Nomenclature (id),
                        foreign key (manufacturer) references Supplier_Nomenclature (id)
                    ) 
    """)


def create_applications_pending(engine):
    """Создать таблицу для неподтвержденных менеджером заказов клиентов."""
    engine.execute("""
                    create table Applications_Pending(
                        id integer primary key auto_increment,  # PK
                        part_name varchar(30),   # FK to Parts_Catalog
                        number integer,  # number of defect parts
                        client integer,  # FK to Clients_Base
                        foreign key (client) references Clients_Base (id)
                    ) 
    """)


def full_create(engine, *args):
    """Создать все требуемые для базы данных таблицы."""
    create_supplier_nomenclature(engine)
    create_parts_catalog(engine)
    create_warehouse_sections(engine)
    create_parts_in_stock(engine)
    create_clients_base(engine)
    create_warehouse_orders(engine)
    create_supplier_orders(engine)
    create_overheads(engine)
    create_defects_register(engine)
    create_applications_pending(engine)


def full_drop(engine, *args):
    """Удаляет все существующие таблицы в базе данных."""
    engine.execute("""drop table if exists Applications_Pending""")
    engine.execute("""drop table if exists Defects_Register""")
    engine.execute("""drop table if exists Overheads""")
    engine.execute("""drop table if exists Supplier_Orders""")
    engine.execute("""drop table if exists Warehouse_Orders""")
    engine.execute("""drop table if exists Clients_Base""")
    engine.execute("""drop table if exists Parts_In_Stock""")
    engine.execute("""drop table if exists Warehouse_Sections""")
    engine.execute("""drop table if exists Parts_Catalog""")
    engine.execute("""drop table if exists Supplier_Nomenclature""")


if __name__ == '__main__':
    # Подключаемся к серверу MySQL на localhost с помощью PyMySQL DB_API.
    my_engine = create_engine('mysql+pymysql://root:password@localhost:3306/autoparts_store')
    # Удаляем все имеющиеся таблицы в БД
    full_drop(my_engine)
    # Добавляем все необходимые таблицы в БД
    full_create(my_engine)
