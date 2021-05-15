"""Информационные запросы к базе данных согласно варианту курсовой работы."""


# Информационный запрос 1:


def request_1_1(engine, category, part_id):
    """Получить список поставщиков категории category, поставляющих деталь part_id."""
    result = engine.execute(f"""with sellers as(select distinct supplier from Supplier_Orders where part='{part_id}') 
                            select id from Supplier_Nomenclature, sellers 
                            where sellers.supplier=Supplier_Nomenclature.id and Supplier_Nomenclature.type='{category}'
                            """).fetchall()
    return result


def request_1_2(engine, category, part_id):
    """Получить количество поставщиков категории category, поставляющих деталь part_id."""
    result = len(request_1_1(engine, category, part_id))
    return result


def request_1_3(engine, category, part_id, date_1, date_2, threshold_number):
    """Получить список поставщиков категории category, поставивших не менее
    threshold_number деталей part_id  за время с date_1 по date_2"""
    result = engine.execute(f"""with suppliers as (with suppliers_and_numbers as (select supplier, sum(number) as 
                            total_number from Supplier_Orders where part='{part_id}' and date between '{date_1}' and 
                            '{date_2}' group by supplier) select supplier from suppliers_and_numbers where 
                            total_number>='{threshold_number}') select id from Supplier_Nomenclature, suppliers where
                            suppliers.supplier=Supplier_Nomenclature.id and Supplier_Nomenclature.type='{category}'
                            """).fetchall()

    return result


def request_1_4(engine, category, part_id, date_1, date_2, threshold_number):
    """Получить количество поставщиков категории category, поставивших не менее
        threshold_number деталей part_id  за время с date_1 по date_2."""
    result = len(request_1_3(engine, category, part_id, date_1, date_2, threshold_number))
    return result


# Информационный запрос 2:


def request_2(engine, part_id):
    """Получить данные о конкретном виде деталей part_id: какими поставщиками
       поставляется, какие у них расценки и время поставки."""
    result = engine.execute(f"""with supplier_id as (select distinct supplier from Supplier_Orders where 
                            part='{part_id}') select id, name, percentage_price*(select price from Parts_Catalog 
                            where id='{part_id}')/100 as price, time_of_delivery from Supplier_Nomenclature, supplier_id 
                            where supplier_id.supplier=Supplier_Nomenclature.id""").fetchall()
    return result


# Информационный запрос 3:


def request_3_1(engine, part_id, date_1, date_2):
    """Получить список покупателей, которые купили товар part_id за время с date_1 по date_2."""
    result = engine.execute(f"""select distinct client from warehouse_orders 
                            where date between '{date_1}' and '{date_2}' and part='{part_id}'""").fetchall()
    return result


def request_3_2(engine, part_id, date_1, date_2):
    """Получить количество покупателей, которые купили товар part_id за время с date_1 по date_2."""
    result = len(request_3_1(engine, part_id, date_1, date_2))
    return result


def request_3_3(engine, part_id, threshold_number):
    """Получить список покупателей, которые купили товар part_id в количестве не меньше threshold_number."""
    result = engine.execute(f"""with client_total_pay as (select client, sum(number)*(select price from parts_catalog 
                            where id='{part_id}') as total_pay from warehouse_orders where part='{part_id}' 
                            group by client) select client from client_total_pay 
                            where total_pay>='{threshold_number}'""").fetchall()
    return result


def request_3_4(engine, part_id, threshold_number):
    """Получить количество покупателей, которые купили товар part_id в количестве не меньше threshold_number."""
    result = len(request_3_3(engine, part_id, threshold_number))
    return result


# Информационный запрос 4:


def request_4(engine):
    """Получить перечень, объем и номер ячейки для всех деталей, хранящихся на складе."""
    result = engine.execute("""with sections as(select distinct section from Parts_In_Stock) select part_type, id as 
                            section_number, total_size from Warehouse_Sections, sections 
                            where Warehouse_Sections.id=sections.section order by part_type""").fetchall()
    return result


# Информационный запрос 5:


def request_5_1(engine):
    """Вывести в порядке возрастания десять самых продаваемых деталей."""
    result = engine.execute("""with sold_parts as (select part, sum(number) as total_number from Warehouse_Orders group 
                            by part order by total_number desc limit 10) select part from sold_parts order by 
                            total_number""").fetchall()
    return result


def request_5_2(engine):
    """Вывести в порядке возрастания десять самых «дешевых» поставщиков."""
    result = engine.execute("""select id from Supplier_Nomenclature order by percentage_price limit 10""").fetchall()
    return result


# Информационный запрос 6:


def request_6(engine):
    """Получить среднее число продаж в месяц по каждому виду деталей."""
    result = engine.execute("""with months as (select TIMESTAMPDIFF(month, min(date), max(date)) as total_months 
                            from Warehouse_Orders), parts_sales as (select part, sum(number) as total_number 
                            from Warehouse_Orders group by part) select part, total_number/(select months.total_months 
                            from months) as sales_per_month from parts_sales""").fetchall()
    return result


# Информационный запрос 7:


def request_7_1(engine, s_s, d_1, d_2):
    """Получить долю товара конкретного поставщика s_s в единицах товара за время с d_1 по d_2."""
    result = engine.execute(f"""select sum(number) as total_number from Warehouse_Orders 
                            where supplier='{s_s}' and date between '{d_1}' and '{d_2}'""").fetchone()
    if len(result) == 0:
        result = 0
    else:
        result = result[0]
    return result


def request_7_2(engine, s_s, d_1, d_2):
    """Получить долю товара конкретного поставщика s_s в процентах от единиц товара за время с d_1 по d_2."""
    res_7_1 = request_7_1(engine, s_s, d_1, d_2)
    if len(res_7_1) == 0:
        result = 0
    else:
        res_7_1 = res_7_1[0][0]
        result = res_7_1 / engine.execute(f"""select sum(number) as total_number from Warehouse_Orders 
                                          where date between '{d_1}' and '{d_2}'""").fetchall()[0][0] * 100
    return result


def request_7_3(engine, s_s, d_1, d_2):
    """Получить долю товара конкретного поставщика special_supplier в деньгах за время с d_1 по d_2."""
    result = engine.execute(f"""with prices as (with part_number as (select part, sum(number) as total_number from 
                            Warehouse_Orders where supplier='{s_s}' and date between '{d_1}' and '{d_2}' group
                            by part) select sum(total_number*price) as total_price from Parts_Catalog, part_number where 
                            part_number.part=Parts_Catalog.id and date between '{d_1}' and '{d_2}')
                            select sum(total_price) as income_from_supplier from prices""").fetchone()
    if len(result) == 0:
        result = 0
    else:
        result = result[0]
    return result


def request_7_4(engine, s_s, d_1, d_2):
    """Получить долю товара конкретного поставщика s_s в процентах от оборота за время с d_1 по d_2."""
    res_7_3 = request_7_3(engine, s_s, d_1, d_2)
    if len(res_7_3) == 0:
        result = 0
    else:
        res_7_3 = res_7_3[0][0]
        result = res_7_3 / engine.execute(f"""with prices as (with part_number as (select part, sum(number) as 
                                          total_number from Warehouse_Orders where date between '{d_1}' and '{d_2}'
                                          group by part) select sum(total_number*price) as total_price from 
                                          Parts_Catalog, part_number where part_number.part=Parts_Catalog.id)
                                          select sum(total_price) as total_income from prices""").fetchall()[0][0] * 100
    return result


def request_7_5(engine, s_s, d_1, d_2):
    """Получить долю товара конкретного поставщика s_s в процентах от дохода за время с d_1 по d_2."""
    res_7_3 = request_7_3(engine, s_s, d_1, d_2)
    if len(res_7_3) == 0:
        result = 0
    else:
        res_7_3 = res_7_3[0][0]
        income = engine.execute(f"""with prices as (with part_number as (select part, sum(number) as 
                                total_number from Warehouse_Orders where date between '{d_1}' and '{d_2}'
                                group by part) select sum(total_number*price) as total_price from 
                                Parts_Catalog, part_number where part_number.part=Parts_Catalog.id)
                                select sum(total_price) as total_income from prices""").fetchall()
        if len(income) == 0:
            return None
        elif income[0][0] == 0:
            return None
        else:
            income = income[0][0]
        straight_outcome = engine.execute(f"""with temp_table as (select supplier, price from Supplier_Orders, 
                                         Parts_Catalog where Supplier_Orders.part=Parts_Catalog.id and date between
                                         '{d_1}' and '{d_2}') select sum(price*percentage_price/100) as 
                                         total_consumption from temp_table, Supplier_Nomenclature where 
                                         temp_table.supplier=Supplier_Nomenclature.id""").fetchall()
        if len(straight_outcome) == 0:
            straight_outcome = 0
        else:
            straight_outcome = straight_outcome[0][0]
        overhead_outcome = engine.execute(f"""select sum(money) from Overheads 
                                          where date between '{d_1}' and '{d_2}'""").fetchall()
        if len(overhead_outcome) == 0:
            overhead_outcome = 0
        else:
            overhead_outcome = overhead_outcome[0][0]
        outcome = straight_outcome + overhead_outcome
        gain = income - outcome
        if gain <= 0:
            result = None
        else:
            result = res_7_3 / gain * 100
        return result


# Информационный запрос 8:


def request_8(engine):
    income = engine.execute(f"""with prices as (with part_number as (select part, sum(number) as 
                            total_number from Warehouse_Orders
                            group by part) select sum(total_number*price) as total_price from 
                            Parts_Catalog, part_number where part_number.part=Parts_Catalog.id)
                            select sum(total_price) as total_income from prices""").fetchall()
    overheads = engine.execute(f"""select sum(money) from Overheads""").fetchall()
    if len(income) == 0:
        return None
    else:
        income = income[0][0]
        if income == 0:
            return None
    if len(overheads) == 0:
        return 0
    else:
        overheads = overheads[0][0]
    result = overheads / income * 100
    return result


# Информационный запрос 9:


def request_9_1(engine, d_1, d_2):
    """Получить перечень непроданного товара на складе за определенный период с d_1 по d_2."""
    result = engine.execute(f"""with sections_wn as (select section, sum(number) as warehouse_number from Parts_In_Stock
                            where date between '{d_1}' and '{d_2}' group by section) select part_type, 
                            sum(warehouse_number) as part_number from sections_wn, Warehouse_Sections 
                            where sections_wn.section=Warehouse_Sections.id group by part_type""").fetchall()
    return result


def request_9_2(engine, d_1, d_2):
    """Получить общее количество непроданного товара на складе за определенный период с d_1 по d_2."""
    result = len(request_9_1(engine, d_1, d_2))
    return result


def request_9_3(engine, d_1, d_2):
    """Получить объем непроданного товара на складе за определенный период с d_1 по d_2 от общего товара в процентах."""
    total = engine.execute(f"""with number_with_date as ( with temp_table as (select number, supplier, date 
                           from Supplier_Orders where executed=true) select number, 
                           date_add(date, interval time_of_delivery day) as date_of_arrival
                           from temp_table, Supplier_Nomenclature where temp_table.supplier=Supplier_Nomenclature.id)
                           select sum(number) as total_p from number_with_date where date_of_arrival 
                           between '{d_1}' and '{d_2}'""").fetchall()
    if len(total) == 0:
        return None
    else:
        total = total[0][0]
    unsold = engine.execute(f"""with sections_wn as (select section, sum(number) as warehouse_number from Parts_In_Stock
                                where date between '{d_1}' and '{d_2}' group by section) select part_type, 
                                sum(warehouse_number) as part_number from sections_wn, Warehouse_Sections 
                                where sections_wn.section=Warehouse_Sections.id group by part_type""").fetchall()
    if len(unsold) == 0:
        return 0
    else:
        unsold = unsold[0][0]
    result = unsold / total * 100
    if result < 0:
        return None
    else:
        return result


# Информационный запрос 10:


def request_10_1(engine, d_1, d_2):
    """Получить перечень бракованного товара, пришедшего за определенный период."""
    result = engine.execute(f"""select part, sum(number) as number_of_parts from Defects_Register 
                            where date between '{d_1}' and '{d_2}' group by part""").fetchall()
    return result


def request_10_2(engine, d_1, d_2):
    """Получить общее количество бракованного товара, пришедшего за определенный период."""
    result = engine.execute(f"""select sum(number) as number_of_parts from Defects_Register 
                                where date between '{d_1}' and '{d_2}'""").fetchall()
    return result


def request_10_3(engine, d_1, d_2):
    """Получить список поставщиков бракованного товара, пришедшего за определенный период."""
    result = engine.execute(f"""select distinct(supplier) as defects_supplier from Defects_Register 
                            where date between '{d_1}' and '{d_2}'""").fetchall()
    return result


# Информационный запрос 11:


def request_11_1(engine, day):
    """Получить перечень товара, реализованного за конкретный день day."""
    result = engine.execute(f"""select part, sum(number) as part_number from warehouse_orders where date='{day}' 
                            and number>0 group by part""").fetchall()
    return result


def request_11_2(engine, day):
    """Получить общее количество товара, реализованного за конкретный день day."""
    result = engine.execute(f"""select sum(number) as total_number from warehouse_orders where date='{day}' 
                            and number>0""").fetchall()
    return result


def request_11_3(engine, day):
    """Получить стоимость товара, реализованного за конкретный день day."""
    result = engine.execute(f"""with temp_table as (select part, sum(number) as number_of_parts from warehouse_orders 
                            where date='{day}' group by part) select sum(number_of_parts*price) as total_price 
                            from temp_table, parts_catalog where parts_catalog.id=temp_table.part""").fetchall()
    return result


# Информационный запрос 12:


def request_12(engine, d_1, d_2):
    """Получить кассовый отчет за определенный период."""
    result = engine.execute(f"""with date_and_income as (with temp_table as (select date, part, number from 
                            warehouse_orders where date between '{d_1}' and '{d_2}') select date, 
                            (price*number) as order_price, number from temp_table, parts_catalog 
                            where temp_table.part=parts_catalog.id) select date, count(*) as day_orders, sum(number) as 
                            day_number, sum(order_price) as day_income from date_and_income group by date""").fetchall()
    return result


# Информационный запрос 13:


def request_13(engine):
    """Получить инвентаризационную ведомость."""
    result = engine.execute("""with half_table as (with temp_table as (select section, number from parts_in_stock)
                            select part_type, sum(number) as total_parts from  temp_table, warehouse_sections 
                            where temp_table.section=warehouse_sections.id group by part_type) select part_type as
                            part_id, name, total_parts, (total_parts*price) as total_price from half_table, 
                            parts_catalog where half_table.part_type=parts_catalog.id""").fetchall()
    return result

# Информационный запрос 14:


def request_14(engine):
    """Получить скорость оборота средств, вложенных в товар (как товар быстро продается)"""
    result = engine.execute("""with date_gain as (with date_and_gain as (with temp_table as (select date, part, number 
                            from warehouse_orders) select date, (price*number) as 
                            order_price from temp_table, parts_catalog where temp_table.part=parts_catalog.id)
                            select date, sum(order_price) as day_gain from date_and_gain group by date)
                            select sum(day_gain)/count(*) as daily_turnover_speed from date_gain""").fetchall()
    # print(result)
    return result


# Информационный запрос 15:


def request_15_1(engine):
    """Подсчитать сколько пустых ячеек на складе."""
    result = engine.execute("""with temp_table as (select section, sum(number) as section_number from parts_in_stock 
                            group by section) select count(*) as empty_sections from warehouse_sections where id not in 
                            (select section from temp_table where section_number > 0)""").fetchall()
    return result


def request_15_2(engine):
    """Подсчитать сколько склад сможет ещё вместить товара."""
    result = engine.execute("""with fulfill as (with temp_table as (with temp_table as (select section, sum(number) as 
                            section_number from parts_in_stock group by section) select part_type, sum(section_number) 
                            as part_number from warehouse_sections, temp_table where 
                            warehouse_sections.id=temp_table.section) select sum(part_number*size) as not_free_size from
                            temp_table, parts_catalog where temp_table.part_type=parts_catalog.id),
                            total_size as (select sum(total_size) as all_size from warehouse_sections)
                            select (all_size-not_free_size) as free_size from fulfill, total_size""").fetchall()
    return result


def request_15_3(engine):
    """Подсчитать сколько склад может всего вместить товара."""
    result = engine.execute("""select sum(total_size) as total_capacity from warehouse_sections""").fetchall()
    return result


# Информационный запрос 16:


def request_16_1(engine):
    """Получить перечень заявок от покупателей на ожидаемый товар."""
    result = engine.execute("""select id, part, number from supplier_orders where executed=false 
                            and client <> 1""").fetchall()
    return result


def request_16_2(engine):
    """Получить общее количество заявок от покупателей на ожидаемый товар."""
    result = len(request_16_1(engine))
    return result


def request_16_3(engine):
    """Подсчитать общую сумму заявок от покупателей на ожидаемый товар."""
    result = engine.execute("""with temp_table as (select part, sum(number) as part_number from supplier_orders where 
                            executed=false and client <> 1 group by part) select sum(part_number*price) as orders_sum 
                            from temp_table, parts_catalog where temp_table.part=parts_catalog.id""").fetchall()
    return result


if __name__ == '__main__':
    from sqlalchemy import create_engine
    # Подключаемся к серверу MySQL на localhost с помощью PyMySQL DB_API.
    my_engine = create_engine('mysql+pymysql://root:password@localhost:3306/autoparts_store')
