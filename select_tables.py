"""Запросы для получения всех данных в таблице."""


def select_supplier_nomenclature(engine, _id=None):
    if _id is None:
        return engine.execute("select * from supplier_nomenclature").fetchall()
    else:
        return engine.execute(f"select * from supplier_nomenclature where id='{_id}'").fetchall()


def select_parts_catalog(engine, _id=None):
    if _id is None:
        return engine.execute("select * from parts_catalog").fetchall()
    else:
        return engine.execute(f"select * from parts_catalog where id='{_id}'").fetchall()


def select_warehouse_sections(engine, _id=None):
    if _id is None:
        return engine.execute("select * from warehouse_sections").fetchall()
    else:
        return engine.execute(f"select * from warehouse_sections where id='{_id}'").fetchall()


def select_parts_in_stock(engine, _id=None):
    if _id is None:
        return engine.execute("select parts_in_stock.id,  section, part_type,  number,  supplier,  manufacturer,  date "
                              "from parts_in_stock, warehouse_sections where parts_in_stock.id=warehouse_sections.id "
                              "order by part_type").fetchall()
    else:
        return engine.execute(f"with t_t as (select parts_in_stock.id,  section, part_type,  number,  supplier,  "
                              f"manufacturer,  date from parts_in_stock, warehouse_sections where "
                              f"parts_in_stock.id=warehouse_sections.id) select * from t_t where "
                              f"part_type='{_id}'").fetchall()


def select_clients_base(engine, _id=None):
    if _id is None:
        return engine.execute("select * from clients_base").fetchall()
    else:
        return engine.execute(f"select * from clients_base where id='{_id}'").fetchall()


def select_warehouse_orders(engine, _id=None):
    if _id is None:
        return engine.execute("select * from warehouse_orders").fetchall()
    else:
        return engine.execute(f"select * from warehouse_orders where id='{_id}'").fetchall()


def select_supplier_orders(engine, _id=None):
    if _id is None:
        return engine.execute("select * from supplier_orders").fetchall()
    else:
        return engine.execute(f"select * from supplier_orders where id='{_id}'").fetchall()


def select_overheads(engine, _id=None):
    if _id is None:
        return engine.execute("select * from overheads").fetchall()
    else:
        return engine.execute(f"select * from overheads where id='{_id}'").fetchall()


def select_defects_register(engine, _id=None):
    if _id is None:
        return engine.execute("select * from defects_register").fetchall()
    else:
        return engine.execute(f"select * from defects_register where id='{_id}'").fetchall()


def select_applications_pending(engine, client_id=None):
    if client_id is None:
        return engine.execute("select * from applications_pending").fetchall()
    else:
        return engine.execute(f"select * from applications_pending where client='{client_id}'").fetchall()