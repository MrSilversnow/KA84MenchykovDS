"""Запросы для обновления некоторых таблиц."""


def execute_supplier_order(engine, _id):
    """Изменяет статус заказа _id у поставщика на исполненный."""
    engine.execute(f"update supplier_orders set executed='1' where id='{_id}'")
    print(f"Статус заказа {_id} успешно изменен на выполнено.")


def change_supplier_price(engine, supplier_id, new_price):
    """Изменяет ценовую политику поставщика supplier_id на долю в new_price%."""
    engine.execute(f"""update supplier_nomenclature set percentage_price='{new_price}' where id='{supplier_id}'""")


def add_to_warehouse(engine, part_id, number, supplier, manufacturer, date):
    """Добавляет товар на склад."""
    from populating_tables import insert_parts_in_stock
    r_space = engine.execute(f"""with t_t as (with temp_table as (select section, sum(number) as section_number 
                                     from parts_in_stock group by section) select section, section_number, total_size 
                                     from temp_table, warehouse_sections where temp_table.section=warehouse_sections.id 
                                     and part_type='{part_id}') select section, floor(total_size / (select size from 
                                     parts_catalog where id='{part_id}')-section_number) as remaining_space 
                                     from t_t""").fetchall()
    for _ in range(len(r_space)):
        number -= r_space[_][1]
        if number <= 0:
            insert_parts_in_stock(engine, r_space[_][0], number+r_space[_][1], supplier, manufacturer, date)
            break
        else:
            insert_parts_in_stock(engine, r_space[_][0], r_space[_][1], supplier, manufacturer, date)
    if number > 0:
        print(f"Склад переполнен. Вынуждено утилизировано {number} единиц товара.")
    else:
        print("Детали успешно помещены на склад")


def get_from_warehouse(engine, part_id, number, date, client):
    """Изымает товары со склада, генерируя касовые чеки."""
    from populating_tables import insert_warehouse_orders
    total_in_warehouse = engine.execute(f"""select sum(number) as tpn from parts_in_stock where section in (select id 
                                        from warehouse_sections where part_type='{part_id}')""").fetchone()
    if len(total_in_warehouse) == 0:
        total_in_warehouse = 0
    else:
        total_in_warehouse = total_in_warehouse[0]
    if total_in_warehouse is None:
        total_in_warehouse = 0
    if total_in_warehouse < number:
        print("К сожелению, на складе нет достаточного количества нужных деталей.")
    else:
        w_parts = engine.execute(f"""select section, number, supplier, manufacturer, id from parts_in_stock where 
                                 section in (select id from warehouse_sections where part_type='{part_id}') 
                                 order by section""").fetchall()
        for _ in range(len(w_parts)):
            number -= w_parts[_][1]
            if number <= 0:
                insert_warehouse_orders(engine, date, client, part_id, w_parts[_][0], number+w_parts[_][1],
                                        w_parts[_][2], w_parts[_][3])
                if number == 0:
                    engine.execute(f"delete from parts_in_stock where id='{w_parts[_][4]}'")
                break
            else:
                insert_warehouse_orders(engine, date, client, part_id, w_parts[_][0], w_parts[_][1],
                                        w_parts[_][2], w_parts[_][3])
                engine.execute(f"delete from parts_in_stock where id='{w_parts[_][4]}'")
        print("Детали успешно изъяты из склада")

