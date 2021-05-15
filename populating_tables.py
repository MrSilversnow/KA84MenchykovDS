"""Функции для для заполнения таблиц в базе данных autoparts_store."""


def insert_supplier_nomenclature(engine, name, country='Ukraine', supplier_type='dealer',
                                 time_of_delivery=1, percentage_price=80):
    """Добавить новую строку в таблицу Supplier_Nomenclature."""
    engine.execute(f"""insert into Supplier_Nomenclature (name, country, type, time_of_delivery, percentage_price) 
                   values ('{name}', '{country}', '{supplier_type}', '{time_of_delivery}', '{percentage_price}')""")


def insert_parts_catalog(engine, name, price, part_size=1):
    """""Добавить новую строку в таблицу Parts_Catalog."""
    engine.execute(f"insert into Parts_Catalog (name, price, size) values ('{name}', '{price}', '{part_size}')")


def insert_warehouse_sections(engine, alias, part_type, total_size):
    """Добавить новую строку в таблицу Warehouse_Sections."""
    engine.execute(f"""insert into Warehouse_Sections (alias, part_type, total_size) 
                    values ('{alias}', '{part_type}', '{total_size}')""")


def insert_parts_in_stock(engine, section, number, supplier, manufacturer, date):
    """Добавить новую строку в таблицу Parts_In_Stock."""
    engine.execute(f"""insert into Parts_In_Stock (section, number, supplier, manufacturer, date)
                      values ('{section}', '{number}', '{supplier}', '{manufacturer}', '{date}')""")


def insert_clients_base(engine, name, password, phone):
    """Добавить новую строку в таблицу Clients_Base."""
    engine.execute(f"insert into Clients_Base (name, password, phone) values ('{name}', '{password}', '{phone}')")


def insert_warehouse_orders(engine, date, client, part, section, number, supplier, manufacturer):
    """Добавить новую строку в таблицу Warehouse_Orders."""
    engine.execute(f"""insert into Warehouse_Orders (date, client, part, section, number, supplier, manufacturer)
                   values ('{date}', '{client}', '{part}', '{section}', '{number}', '{supplier}', '{manufacturer}')""")


def insert_supplier_orders(engine, date, client, part, executed, number, supplier, manufacturer):
    """Добавить новую строку в таблицу Supplier_Orders."""
    engine.execute(f"""insert into Supplier_Orders (date, client, part, executed, number, supplier, manufacturer)
                   values ('{date}', '{client}', '{part}', '{executed}', '{number}', '{supplier}', '{manufacturer}')
    """)


def insert_overheads(engine, overhead_type, explanation, date, money):
    """Добавить новую строку в таблицу Overheads."""
    engine.execute(f"""insert into Overheads (type, explanation, date, money) 
                   values ('{overhead_type}', '{explanation}', '{date}', '{money}')""")


def insert_defects_register(engine, date, part, supplier, manufacturer, number):
    """Добавить новую строку в таблицу Defects_Register."""
    engine.execute(f"""insert into Defects_Register (date, part, supplier, manufacturer, number)
                   values ('{date}', '{part}', '{supplier}', '{manufacturer}', '{number}')""")


def insert_applications_pending(engine, part_name, number, client):
    """Добавить новую строку в таблицу Applications_Pending."""
    engine.execute(f"""insert into Applications_Pending (part_name, number, client)
                       values ('{part_name}', '{number}', '{client}')""")


def populate_supplier_nomenclature(engine):
    """Заполняет данными таблицу Supplier_Nomenclature."""
    insert_supplier_nomenclature(engine, 'AR company', 'Ukraine', 'dealer', 1, 80)
    insert_supplier_nomenclature(engine, 'Souse', 'Italy', 'large firm', 4, 50)
    insert_supplier_nomenclature(engine, 'Blank', 'Ukraine', 'small firm', 1, 85)
    insert_supplier_nomenclature(engine, 'Tree', 'Japan', 'small firm', 9, 40)
    insert_supplier_nomenclature(engine, 'VR company', 'Ukraine', 'dealer', 1, 80)
    insert_supplier_nomenclature(engine, 'Terra', 'Switzerland', 'large firm', 4, 90)
    insert_supplier_nomenclature(engine, 'Darth Sidious', 'USA', 'dealer', 13, 50)
    insert_supplier_nomenclature(engine, 'Palpatine', 'Russia', 'dealer', 2, 25)
    insert_supplier_nomenclature(engine, 'Mina Bonteri', 'Ukraine', 'large firm', 1, 45)
    insert_supplier_nomenclature(engine, 'Rush Clovis', 'Ukraine', 'dealer', 1, 95)
    insert_supplier_nomenclature(engine, 'Crix Madine', 'Ukraine', 'large firm', 1, 85)
    insert_supplier_nomenclature(engine, 'Arvel Crynyd', 'Ukraine', 'dealer', 1, 75)


def populate_parts_catalog(engine):
    """Заполняет данными таблицу Parts_Catalog."""
    insert_parts_catalog(engine, 'Bonnet', 42690, 4)
    insert_parts_catalog(engine, 'Wing mirror', 355, 1)
    insert_parts_catalog(engine, 'Windscreen', 4221, 2)
    insert_parts_catalog(engine, 'Rear-view mirror', 964, 1)
    insert_parts_catalog(engine, 'Windscreen wiper', 36426, 1)
    insert_parts_catalog(engine, 'Licence', 7537, 1)
    insert_parts_catalog(engine, 'Door', 2642, 3)
    insert_parts_catalog(engine, 'Indicator', 773, 1)
    insert_parts_catalog(engine, 'Boot', 3795, 2)
    insert_parts_catalog(engine, 'Tyre', 2657, 2)
    insert_parts_catalog(engine, 'Wheel', 57694, 2)
    insert_parts_catalog(engine, 'Headlight', 35786, 1)
    insert_parts_catalog(engine, 'Bumper', 58356, 5)


def populate_warehouse_sections(engine):
    """Заполняет данными таблицу Warehouse_Sections."""
    insert_warehouse_sections(engine, 'Green section', 1, 1370)
    insert_warehouse_sections(engine, 'White section', 1, 1250)
    insert_warehouse_sections(engine, 'Blue section', 1, 2380)
    insert_warehouse_sections(engine, 'Silver section', 2, 5100)
    insert_warehouse_sections(engine, 'Gold section', 3, 7510)
    insert_warehouse_sections(engine, 'Grey section', 4, 9250)
    insert_warehouse_sections(engine, 'Yellow section', 5, 1320)
    insert_warehouse_sections(engine, 'Grim section', 6, 3120)
    insert_warehouse_sections(engine, 'Teen section', 7, 9500)
    insert_warehouse_sections(engine, 'Voice section', 8, 5700)
    insert_warehouse_sections(engine, 'Nice section', 9, 4600)
    insert_warehouse_sections(engine, 'Sleep section', 10, 2210)
    insert_warehouse_sections(engine, 'Deep section', 11, 1450)
    insert_warehouse_sections(engine, 'Cut section', 12, 3600)
    insert_warehouse_sections(engine, 'Cat section', 13, 2200)


# insert_parts_in_stock(engine, section, number, supplier, manufacturer, date)
def populate_parts_in_stock(engine):
    """Заполняет данными таблицу Parts_In_Stock."""
    insert_parts_in_stock(engine, 1, 12, 4, 2, '2019-03-04')
    insert_parts_in_stock(engine, 1, 3, 1, 3, '2019-03-04')
    insert_parts_in_stock(engine, 2, 30, 1, 4, '2019-03-04')
    insert_parts_in_stock(engine, 3, 26, 3, 2, '2019-05-04')
    insert_parts_in_stock(engine, 3, 85, 4, 3, '2019-06-04')
    insert_parts_in_stock(engine, 5, 37, 2, 4, '2019-06-14')
    insert_parts_in_stock(engine, 6, 36, 7, 2, '2019-08-24')
    insert_parts_in_stock(engine, 4, 46, 5, 3, '2019-09-04')
    insert_parts_in_stock(engine, 7, 53, 5, 4, '2019-11-14')
    insert_parts_in_stock(engine, 8, 32, 5, 2, '2019-12-28')
    insert_parts_in_stock(engine, 9, 113, 5, 3, '2019-12-28')
    insert_parts_in_stock(engine, 10, 13, 7, 4, '2020-01-13')
    insert_parts_in_stock(engine, 11, 11, 2, 2, '2020-01-13')
    insert_parts_in_stock(engine, 12, 15, 2, 3, '2020-01-13')
    insert_parts_in_stock(engine, 13, 34, 5, 4, '2020-01-15')
    insert_parts_in_stock(engine, 14, 10, 2, 2, '2020-01-17')
    insert_parts_in_stock(engine, 15, 2, 5, 3, '2020-01-18')
    insert_parts_in_stock(engine, 14, 15, 6, 4, '2020-01-21')
    insert_parts_in_stock(engine, 10, 3, 7, 2, '2020-01-25')
    insert_parts_in_stock(engine, 10, 4, 2, 3, '2020-02-03')


def populate_clients_base(engine):
    """Заполняет данными таблицу Clients_Base."""
    insert_clients_base(engine, 'YOURSELF', 'qwerty', '+000-000-000-00')
    insert_clients_base(engine, 'Anakin Skywalker', 'qwerty', '+259-150-242-24')
    insert_clients_base(engine, 'Luke Skywalker', 'qwerty', '+259-150-242-24')
    insert_clients_base(engine, 'Leia Organa', 'qwerty', '+259-150-242-24')
    insert_clients_base(engine, 'Han Solo', 'qwerty', '+259-150-242-24')
    insert_clients_base(engine, 'Ben Solo', 'qwerty', '+259-150-242-24')
    insert_clients_base(engine, 'Padme Amidala', 'qwerty', '+259-150-242-24')
    insert_clients_base(engine, 'Jobal Naberrie', 'qwerty', '+259-150-242-24')
    insert_clients_base(engine, 'Pooja Naberrie', 'qwerty', '+259-150-242-24')
    insert_clients_base(engine, 'Ruwee Naberrie', 'qwerty', '+259-150-242-24')
    insert_clients_base(engine, 'Ryoo Naberrie', 'qwerty', '+259-150-242-24')
    insert_clients_base(engine, 'Sola Naberrie', 'qwerty', '+259-150-242-20')
    insert_clients_base(engine, 'Beru Whitesun Lars', 'qwerty', '+259-150-242-21')
    insert_clients_base(engine, 'Cliegg Lars', 'qwerty', '+259-150-242-22')
    insert_clients_base(engine, 'Owen Lars', 'qwerty', '+259-150-242-23')
    insert_clients_base(engine, 'Aika Lars', 'qwerty', '+259-150-242-24')
    insert_clients_base(engine, 'Bail Organa', 'qwerty', '+259-150-242-25')
    insert_clients_base(engine, 'Breha Organa', 'qwerty', '+259-150-242-26')
    insert_clients_base(engine, 'Avar Kriss', 'qwerty', '+259-150-242-27')
    insert_clients_base(engine, 'Depa Billaba', 'qwerty', '+259-150-242-28')
    insert_clients_base(engine, 'Shmi Skywalker', 'qwerty', '+259-150-242-29')
    insert_clients_base(engine, 'Ezra Bridger', 'qwerty', '+259-150-242-36')
    insert_clients_base(engine, 'Eno Cordova', 'qwerty', '+259-150-242-14')
    insert_clients_base(engine, 'Cin Drallig', 'shine', '+259-150-242-12')
    insert_clients_base(engine, 'Sifo-Dyas', 'shine', '+259-150-242-04')
    insert_clients_base(engine, 'Caleb Dume', 'shine', '+259-150-242-44')
    insert_clients_base(engine, 'Qui-Gon Jinn', 'shine', '+259-150-242-54')
    insert_clients_base(engine, 'Cere Junda', 'shine', '+259-150-242-84')
    insert_clients_base(engine, 'Ben Kenobi', 'shine', '+259-150-242-94')
    insert_clients_base(engine, 'Cal Kestis', 'shine', '+259-150-242-53')
    insert_clients_base(engine, 'Jocasta Nu', 'shine', '+259-150-242-91')
    insert_clients_base(engine, 'Mace Windu', 'shine', '+259-150-240-24')
    insert_clients_base(engine, 'Darth Bane', 'shine', '+258-150-241-24')
    insert_clients_base(engine, 'Darth Tyranus', 'shine', '+259-150-242-24')
    insert_clients_base(engine, 'Taron Malicos', 'shine', '+259-150-243-24')
    insert_clients_base(engine, 'Trilla Suduri', 'shine', '+259-150-244-24')
    insert_clients_base(engine, 'Din Djarin', 'icecream', '+259-150-245-24')
    insert_clients_base(engine, 'Captain Hark', 'icecream','+259-150-246-24')
    insert_clients_base(engine, 'Rook Kast', 'icecream','+259-150-247-24')
    insert_clients_base(engine, 'Ketsu Onyo', 'icecream','+259-150-248-24')
    insert_clients_base(engine, 'Fenn Rau', 'icecream','+259-150-249-24')
    insert_clients_base(engine, 'Koska Reeves', 'icecream','+259-150-252-24')
    insert_clients_base(engine, 'Axe Woves', 'icecream','+259-150-262-24')
    insert_clients_base(engine, 'Boba Fett', 'icecream','+259-150-272-24')
    insert_clients_base(engine, 'Jango Fett', 'icecream', '+259-150-282-24')
    insert_clients_base(engine, 'Bo-Katan Kryze', 'icecream', '+259-150-292-24')
    insert_clients_base(engine, 'Satine Kryze', 'icecream', '+459-150-252-24')
    insert_clients_base(engine, 'Korkie Kryze', 'icecream', '+259-150-142-24')
    insert_clients_base(engine, 'Gar Saxon', 'icecream', '+259-150-342-24')
    insert_clients_base(engine, 'Tiber Saxon', 'icecream', '+259-150-442-24')
    insert_clients_base(engine, 'Paz Vizsla', 'icecream', '+259-150-542-24')
    insert_clients_base(engine, 'Pre Vizsla', 'icecream', '+259-150-642-24')
    insert_clients_base(engine, 'Alrich Wren', 'icecream', '+259-150-742-24')
    insert_clients_base(engine, 'Sabine Wren', 'icecream', '+259-150-842-24')
    insert_clients_base(engine, 'Tristan Wren', 'icecream', '+259-150-942-24')
    insert_clients_base(engine, 'Ursa Wren', 'icecream', '+259-150-242-24')
    insert_clients_base(engine, 'Faro Argyus', 'icecream', '+259-113-242-24')
    insert_clients_base(engine, 'Lux Bonteri', 'icecream', '+259-124-242-24')
    insert_clients_base(engine, 'Tan Divo', 'icecream', '+259-164-242-24')
    insert_clients_base(engine, 'Finis Valorum', 'icecream', '+259-179-242-24')


# insert_warehouse_orders(engine, date, client, part, section, number, supplier, manufacturer)
def populate_warehouse_orders(engine):
    """Заполняет данными таблицу Warehouse_Orders."""
    insert_warehouse_orders(engine, '2019-03-07', 7, 8, 10, 13, 6, 11)
    insert_warehouse_orders(engine, '2020-01-25', 11, 3, 5, 24, 7, 2)
    insert_warehouse_orders(engine, '2019-12-29', 12, 1, 1, 35, 8, 3)
    insert_warehouse_orders(engine, '2020-01-18', 12, 5, 7, 14, 9, 11)
    insert_warehouse_orders(engine, '2019-06-04', 13, 8, 10, 3, 10, 10)
    insert_warehouse_orders(engine, '2019-11-14', 8, 6, 8, 21, 10, 10)
    insert_warehouse_orders(engine, '2020-01-13', 13, 8, 10, 23, 11, 11)
    insert_warehouse_orders(engine, '2020-01-13', 7, 3, 5, 19, 11, 11)


# insert_supplier_orders(engine, date, client, part, executed, number, supplier, manufacturer)
def populate_supplier_orders(engine):
    """Заполняет данными таблицу Warehouse_Orders."""
    insert_supplier_orders(engine, '2019-03-03', 1, 1, '1', 12, 4, 2)
    insert_supplier_orders(engine, '2019-03-03', 1, 1, '1', 3, 1, 3)
    insert_supplier_orders(engine, '2019-03-03', 1, 1, '1', 30, 1, 4)
    insert_supplier_orders(engine, '2019-05-03', 1, 1, '1', 26, 3, 2)
    insert_supplier_orders(engine, '2019-06-03', 1, 1, '1', 85, 4, 3)
    insert_supplier_orders(engine, '2019-09-03', 1, 2, '1', 46, 5, 3)
    insert_supplier_orders(engine, '2019-06-13', 1, 3, '1', 37, 2, 4)
    insert_supplier_orders(engine, '2019-08-23', 1, 4, '1', 36, 7, 2)
    insert_supplier_orders(engine, '2019-11-13', 1, 5, '1', 53, 5, 4)
    insert_supplier_orders(engine, '2019-12-27', 1, 6, '1', 32, 5, 2)
    insert_supplier_orders(engine, '2019-12-27', 1, 7, '1', 113, 5, 3)
    insert_supplier_orders(engine, '2020-01-12', 1, 8, '1', 13, 7, 4)
    insert_supplier_orders(engine, '2020-01-24', 1, 8, '1', 3, 7, 2)
    insert_supplier_orders(engine, '2020-02-02', 1, 8, '1', 4, 2, 3)
    insert_supplier_orders(engine, '2020-01-12', 1, 9, '1', 11, 2, 2)
    insert_supplier_orders(engine, '2020-01-12', 1, 10, '1', 15, 2, 3)
    insert_supplier_orders(engine, '2020-01-14', 1, 11, '1', 34, 5, 4)
    insert_supplier_orders(engine, '2020-01-16', 1, 12, '1', 10, 2, 2)
    insert_supplier_orders(engine, '2020-01-20', 1, 12, '1', 15, 6, 4)
    insert_supplier_orders(engine, '2020-01-17', 1, 13, '1', 2, 5, 3)
    insert_supplier_orders(engine, '2019-03-03', 7, 8, '1', 75, 6, 11)
    insert_supplier_orders(engine, '2020-01-12', 11, 3, '1', 64, 7, 2)
    insert_supplier_orders(engine, '2019-12-27', 12, 1, '1', 35, 8, 3)
    insert_supplier_orders(engine, '2020-01-17', 12, 5, '1', 64, 9, 11)
    insert_supplier_orders(engine, '2019-06-03', 13, 8, '1', 53, 10, 10)
    insert_supplier_orders(engine, '2019-11-13', 8, 6, '1', 32, 10, 10)
    insert_supplier_orders(engine, '2020-01-12', 13, 8, '1', 53, 11, 11)
    insert_supplier_orders(engine, '2020-01-12', 7, 3, '1', 35, 11, 11)
    insert_supplier_orders(engine, '2020-02-27', 18, 7, '0', 3, 11, 11)
    insert_supplier_orders(engine, '2020-02-28', 8, 9, '0', 42, 12, 11)
    insert_supplier_orders(engine, '2019-03-03', 1, 1, '1', -2, 4, 2)
    insert_supplier_orders(engine, '2020-01-17', 12, 5, '1', -4, 9, 11)


# insert_overheads(engine, overhead_type, explanation, date, money)
def populate_overheads(engine):
    """Заполняет данными таблицу Overheads."""
    insert_overheads(engine, 'Salary', '', '2019-03-03', 25000)
    insert_overheads(engine, 'Salary', '', '2019-04-03', 25000)
    insert_overheads(engine, 'Salary', '', '2019-05-03', 25000)
    insert_overheads(engine, 'Salary', '', '2019-06-03', 25000)
    insert_overheads(engine, 'Salary', '', '2019-07-03', 25000)
    insert_overheads(engine, 'Salary', '', '2019-08-03', 25000)
    insert_overheads(engine, 'Salary', '', '2019-09-03', 25000)
    insert_overheads(engine, 'Salary', '', '2019-10-03', 25000)
    insert_overheads(engine, 'Salary', '', '2019-11-03', 25000)
    insert_overheads(engine, 'Salary', '', '2019-12-03', 25000)
    insert_overheads(engine, 'Salary', '', '2020-01-03', 25000)


# insert_defects_register(engine, date, part, supplier, manufacturer, number)
def populate_defects_register(engine):
    """Заполняет данными таблицу Defects_Register."""
    insert_defects_register(engine, '2019-03-03', 1, 4, 2, 2)
    insert_defects_register(engine, '2020-01-17',  5,  9, 11, 4)


def populate_tables(engine, *args):
    """Заполняет данными все таблицы."""
    populate_supplier_nomenclature(engine)  # total 12
    populate_parts_catalog(engine)  # total 13
    populate_warehouse_sections(engine)  # total 15
    populate_parts_in_stock(engine)  # total 20
    populate_clients_base(engine)  # total 40
    populate_warehouse_orders(engine)  # total 12
    populate_supplier_orders(engine)  # total 33
    populate_overheads(engine)  # total 10
    populate_defects_register(engine)  # total 2


if __name__ == '__main__':
    from sqlalchemy import create_engine
    # Подключаемся к серверу MySQL на localhost с помощью PyMySQL DB_API.
    my_engine = create_engine('mysql+pymysql://root:password@localhost:3306/autoparts_store')
    populate_tables(my_engine)
