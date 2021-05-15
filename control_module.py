from tabulate import tabulate
from create_tables import full_create, full_drop
from populating_tables import populate_tables


def controller(engine, request, client_id=None, access_level='user'):
    """Обрабатывает большинство запросов"""
    user_interface = {
        'Help': help_me,
        'SelectPartsInStock': SelectPartsInStock,
        'SelectPartsInStock special': SelectPartsInStock_special,
        'AddOrder': AddOrder,
        'GetMyOrders': GetMyOrders,
        'SelectPartsCatalog': SelectPartsCatalog,
        'LogIn': LogIn,
        'SignIn': SignIn,
        'End': End
    }
    manager_interface = {
        'Help': help_me,
        'SelectPartsInStock': SelectPartsInStock,
        'SelectPartsInStock special': SelectPartsInStock_special,
        'AddOrder': AddOrder,
        'GetMyOrders': GetMyOrders,
        'SelectPartsCatalog': SelectPartsCatalog,
        'LogIn': LogIn,
        'SignIn': SignIn,
        'End': End,
        'SelectSupplierNomenclature': SelectSupplierNomenclature,
        'SelectSupplierNomenclature special': SelectSupplierNomenclature_special,
        'SelectWarehouseSections': SelectWarehouseSections,
        'SelectWarehouseSections special': SelectWarehouseSections_special,
        'SelectClientsBase': SelectClientsBase,
        'SelectClientsBase special': SelectClientsBase_special,
        'SelectWarehouseOrders': SelectWarehouseOrders,
        'SelectWarehouseOrders special': SelectWarehouseOrders_special,
        'SelectSupplierOrders': SelectSupplierOrders,
        'SelectSupplierOrders special': SelectSupplierOrders_special,
        'SelectOverheads': SelectOverheads,
        'SelectOverheads special': SelectOverheads_special,
        'SelectDefectsRegister': SelectDefectsRegister,
        'SelectDefectsRegister special': SelectDefectsRegister_special,
        'ExecuteSupplierOrder': ExecuteSupplierOrder,
        'ChangeSupplierPrice': ChangeSupplierPrice,
        'InsertSupplierNomenclature': InsertSupplierNomenclature,
        'InsertWarehouseSections': InsertWarehouseSections,
        'GetFromWarehouse': GetFromWarehouse,
        'InsertOverheads': InsertOverheads,
        'InsertDefectsRegister': InsertDefectsRegister,
        'InsertPartsCatalog': InsertPartsCatalog,
        'GetSpecialSupplier': GetSpecialSupplier,
        'GetNumberOfSpecialSupplier': GetNumberOfSpecialSupplier,
        'GetSpecialSupplierByDateNumber': GetSpecialSupplierByDateNumber,
        'GetNumberOfSpecialSupplierByDateNumber': GetNumberOfSpecialSupplierByDateNumber,
        'GetInfoForSpecialPart': GetInfoForSpecialPart,
        'GetSpecialClientByDate': GetSpecialClientByDate,
        'GetNumberOfSpecialClientByDate': GetNumberOfSpecialClientByDate,
        'GetSpecialClientByNumber': GetSpecialClientByNumber,
        'GetNumberOfSpecialClientByNumber': GetNumberOfSpecialClientByNumber,
        'GetPartsInStockInfo': GetPartsInStockInfo,
        'GetTenPopularParts': GetTenPopularParts,
        'GetTenCheapestSuppliers': GetTenCheapestSuppliers,
        'GetAverageSalesPerMonth': GetAverageSalesPerMonth,
        'GetSpecialSupplierAmountOfIncome': GetSpecialSupplierAmountOfIncome,
        'GetSpecialSupplierAmountOfGain': GetSpecialSupplierAmountOfGain,
        'GetOverheadsAmountOfIncome': GetOverheadsAmountOfIncome,
        'GetUnsoldPartsByDate': GetUnsoldPartsByDate,
        'GetNumberOfUnsoldPartsByDate': GetNumberOfUnsoldPartsByDate,
        'GetUnsoldPartsAmountByDate': GetUnsoldPartsAmountByDate,
        'GetDefectPartsInfoByDate': GetDefectPartsInfoByDate,
        'GetNumberOfDefectPartsInfoByDate': GetNumberOfDefectPartsInfoByDate,
        'GetDefectSupplierInfoByDate': GetDefectSupplierInfoByDate,
        'GetSoldPartsByDay': GetSoldPartsByDay,
        'GetNumberOfSoldPartsByDay': GetNumberOfSoldPartsByDay,
        'GetIncomeByDay': GetIncomeByDay,
        'GetCashReport': GetCashReport,
        'GetInventoryStatement': GetInventoryStatement,
        'GetDailyTurnoverSpeed': GetDailyTurnoverSpeed,
        'GetEmptyCages': GetEmptyCages,
        'GetWarehouseCapacity': GetWarehouseCapacity,
        'GetFreeWarehouseCapacity': GetFreeWarehouseCapacity,
        'GetExpectedClientsOrders': GetExpectedClientsOrders,
        'GetNumberOfExpectedClientsOrders': GetNumberOfExpectedClientsOrders,
        'GetSumOfExpectedClientsOrders': GetSumOfExpectedClientsOrders,
        'GetOrders': GetOrders
    }
    admin_interface = {
        'Help': help_me,
        'SelectPartsInStock': SelectPartsInStock,
        'SelectPartsInStock special': SelectPartsInStock_special,
        'AddOrder': AddOrder,
        'GetMyOrders': GetMyOrders,
        'SelectPartsCatalog': SelectPartsCatalog,
        'LogIn': LogIn,
        'SignIn': SignIn,
        'End': End,
        'SelectSupplierNomenclature': SelectSupplierNomenclature,
        'SelectSupplierNomenclature special': SelectSupplierNomenclature_special,
        'SelectWarehouseSections': SelectWarehouseSections,
        'SelectWarehouseSections special': SelectWarehouseSections_special,
        'SelectClientsBase': SelectClientsBase,
        'SelectClientsBase special': SelectClientsBase_special,
        'SelectWarehouseOrders': SelectWarehouseOrders,
        'SelectWarehouseOrders special': SelectWarehouseOrders_special,
        'SelectSupplierOrders': SelectSupplierOrders,
        'SelectSupplierOrders special': SelectSupplierOrders_special,
        'SelectOverheads': SelectOverheads,
        'SelectOverheads special': SelectOverheads_special,
        'SelectDefectsRegister': SelectDefectsRegister,
        'SelectDefectsRegister special': SelectDefectsRegister_special,
        'ExecuteSupplierOrder': ExecuteSupplierOrder,
        'ChangeSupplierPrice': ChangeSupplierPrice,
        'InsertSupplierNomenclature': InsertSupplierNomenclature,
        'InsertWarehouseSections': InsertWarehouseSections,
        'GetFromWarehouse': GetFromWarehouse,
        'InsertOverheads': InsertOverheads,
        'InsertDefectsRegister': InsertDefectsRegister,
        'InsertPartsCatalog': InsertPartsCatalog,
        'GetSpecialSupplier': GetSpecialSupplier,
        'GetNumberOfSpecialSupplier': GetNumberOfSpecialSupplier,
        'GetSpecialSupplierByDateNumber': GetSpecialSupplierByDateNumber,
        'GetNumberOfSpecialSupplierByDateNumber': GetNumberOfSpecialSupplierByDateNumber,
        'GetInfoForSpecialPart': GetInfoForSpecialPart,
        'GetSpecialClientByDate': GetSpecialClientByDate,
        'GetNumberOfSpecialClientByDate': GetNumberOfSpecialClientByDate,
        'GetSpecialClientByNumber': GetSpecialClientByNumber,
        'GetNumberOfSpecialClientByNumber': GetNumberOfSpecialClientByNumber,
        'GetPartsInStockInfo': GetPartsInStockInfo,
        'GetTenPopularParts': GetTenPopularParts,
        'GetTenCheapestSuppliers': GetTenCheapestSuppliers,
        'GetAverageSalesPerMonth': GetAverageSalesPerMonth,
        'GetSpecialSupplierAmountOfIncome': GetSpecialSupplierAmountOfIncome,
        'GetSpecialSupplierAmountOfGain': GetSpecialSupplierAmountOfGain,
        'GetOverheadsAmountOfIncome': GetOverheadsAmountOfIncome,
        'GetUnsoldPartsByDate': GetUnsoldPartsByDate,
        'GetNumberOfUnsoldPartsByDate': GetNumberOfUnsoldPartsByDate,
        'GetUnsoldPartsAmountByDate': GetUnsoldPartsAmountByDate,
        'GetDefectPartsInfoByDate': GetDefectPartsInfoByDate,
        'GetNumberOfDefectPartsInfoByDate': GetNumberOfDefectPartsInfoByDate,
        'GetDefectSupplierInfoByDate': GetDefectSupplierInfoByDate,
        'GetSoldPartsByDay': GetSoldPartsByDay,
        'GetNumberOfSoldPartsByDay': GetNumberOfSoldPartsByDay,
        'GetIncomeByDay': GetIncomeByDay,
        'GetCashReport': GetCashReport,
        'GetInventoryStatement': GetInventoryStatement,
        'GetDailyTurnoverSpeed': GetDailyTurnoverSpeed,
        'GetEmptyCages': GetEmptyCages,
        'GetWarehouseCapacity': GetWarehouseCapacity,
        'GetFreeWarehouseCapacity': GetFreeWarehouseCapacity,
        'GetExpectedClientsOrders': GetExpectedClientsOrders,
        'GetNumberOfExpectedClientsOrders': GetNumberOfExpectedClientsOrders,
        'GetSumOfExpectedClientsOrders': GetSumOfExpectedClientsOrders,
        'GetOrders': GetOrders,
        'DeleteTables': full_drop,
        'CreateTables': full_create,
        'PopulateTables': populate_tables,
        'TestSample': TestSample
    }
    my_interface = {
        'user': user_interface,
        'manager': manager_interface,
        'admin': admin_interface
    }
    request_function = my_interface[access_level].get(request)
    if request_function is None:
        print("Неизвестная команда. Ничего не происходит.")
    else:
        if request_function is help_me:
            request_function(engine, access_level)
        else:
            return request_function(engine, client_id)


def help_me(_, access_level):
    print(access_level)
    print("""Вас приветствует справка программы "База Данных Магазина Автозапчастей"
             Програма была разработана разработчиком под псевдонимом "Надо было делать раньше"
             Для использования базы данных вам доступны следующие команды:
             Help - вывод справки (вы здесь)
             SelectPartsInStock [special] - выводит информацию о товаре на складе | special позволяет делать запрос по id 
             AddOrder - сделать заказ на получение деталей
             GetMyOrders - выводит заказанные детали и их количество
             SelectPartsCatalog - выводит список деталей
             End - закрытие программы""")
    if access_level == 'manager' or access_level == 'admin':
        print("""
                 SelectSupplierNomenclature [special] - выводит список поставщиков | special позволяет делать запрос по id 
                 SelectWarehouseSections [special] - выводит список секций склада | special позволяет делать запрос по id 
                 SelectClientsBase [special] - выводит информацию о клиентах | special позволяет делать запрос по id 
                 SelectWarehouseOrders [special] - выводит информацию о продажах со склада | special позволяет делать запрос по id 
                 SelectSupplierOrders [special] - выводит информацию о заявках поставщику | special позволяет делать запрос по id 
                 SelectOverheads [special] - выводит информацию о накладных расходах | special позволяет делать запрос по id 
                 SelectDefectsRegister [special] - выводит информацию о браке | special позволяет делать запрос по id 
                 ExecuteSupplierOrder - переключает состояние заказа у поставщика на выполнено
                 ChangeSupplierPrice - изменяет процентную ценовую политику поставщика
                 InsertSupplierNomenclature  - добавляет нового поставщика
                 InsertWarehouseSections - добавляет новую секцию склада
                 GetFromWarehouse - осуществляет продажу деталей со склада
                 InsertOverheads - добавляет информацию о накладных расходах
                 InsertDefectsRegister - добавляет информацию о браке
                 InsertPartsCatalog - добавляет в каталог новую часть
                 GetSpecialSupplier - выводит список поставщиков определенного вида, поставивших определенный товар за определенный период
                 GetNumberOfSpecialSupplier - выводит количество поставщиков определенного вида, поставивших определенный товар за определенный период
                 GetSpecialSupplierByDateNumber - выводит список поставщиков определенного вида, поставивших определенный товар как минимум определенного количества в определенный период
                 GetNumberOfSpecialSupplierByDateNumber - выводит количество поставщиков определенного вида, поставивших определенный товар как минимум определенного количества в определенный период
                 GetInfoForSpecialPart - выводит данные про конкретный вид деталей: поставщиков, их расценки, время поставки
                 GetSpecialClientByDate - выводит список клиентов, купивших конкретный вид деталей за определенный период
                 GetNumberOfSpecialClientByDate - выводит количество клиентов, купивших конкретный вид деталей за определенный период
                 GetSpecialClientByNumber - выводит список клиентов, купивших конкретный в определенном количестве
                 GetNumberOfSpecialClientByNumber - выводит количество клиентов, купивших конкретный в определенном количестве
                 GetPartsInStockInfo - выводит список, размер и номер ячейки для всех деталей, хранящихся на складе
                 GetTenPopularParts - выводит список из 10-ти самых продаваемых товаров в порядке возрастания
                 GetTenCheapestSuppliers - выводит с список из 10-ти самых "дешевых" поставщиков в порядке возрастания
                 GetAverageSalesPerMonth - выводит список средних продаж в месяц для каждой детали
                 GetSpecialSupplierAmountOfIncome - выводит долю товара конкретного поставщика в процентах, деньгах, единицах от всего оборота магазина за указанный период
                 GetSpecialSupplierAmountOfGain - выводит долю товара конкретного поставщика в процентах, деньгах от прибыли магазина за указанный период
                 GetOverheadsAmountOfIncome - выводит накладные расходы в процентах от объема продаж
                 GetUnsoldPartsByDate - выводит список непроданного товара на складе за определенный период
                 GetNumberOfUnsoldPartsByDate - выводит список непроданного товара на складе за определенный период
                 GetUnsoldPartsAmountByDate - выводит долю в процентах непроданного товара от общего товара за определенный период
                 GetDefectPartsInfoByDate - выводит список бракованого товара за определенный период
                 GetNumberOfDefectPartsInfoByDate - выводит количество бракованого товара за определенный период
                 GetDefectSupplierInfoByDate -  список поставщиков бракованного товара, пришедшего за определенный период
                 GetSoldPartsByDay - выводит список проданого за день товара
                 GetNumberOfSoldPartsByDay - выводит общее количество проданого за день товара
                 GetIncomeByDay - выводит стоимость товара, проданого за день
                 GetCashReport - выводит касовый отчет за определенный период
                 GetInventoryStatement - выводит инвентаризационную ведомость
                 GetDailyTurnoverSpeed - выводит скорость оборота средств, вложенных в товар (как товар быстро продается)
                 GetEmptyCages - выводит количество пустых ячеек на складе
                 GetWarehouseCapacity - выводит общий объем склада
                 GetFreeWarehouseCapacity - выводит незанятый размер склада
                 GetExpectedClientsOrders - выводит список заявок от покупателей на ожидаемый товар
                 GetNumberOfExpectedClientsOrders - выводит количество заявок от покупателей на ожидаемый товар
                 GetSumOfExpectedClientsOrders - выводит общую сумму заявок от покупателей на ожидаемый товар
                 GetOrders - выводит неподтвержденные заказы клиентов
                 """)
        if access_level == 'admin':
            print("""DeleteTables - удаляет все таблицы в базе данных
                     CreateTables - создает все таблицы в базе данных
                     PopulateTables - заполняет таблицы некоторыми тестовыми данными
                     TestSample - последовательно выполняет команды DeleteTables, CreateTables, PopulateTables""")


def check_date(string):
    """Проверяет, является ли строка датой в формате ГГГГ-ММ-ДД."""
    string = string.split('-')
    if len(string) == 3:
        if len(string[0]) == 4 and string[0].isdigit():
            if len(string[1]) == 2 and string[1].isdigit():
                if len(string[2]) == 2 and string[2].isdigit():
                    return True
    return False


def TestSample(engine, client_id):
    full_drop(engine)
    full_create(engine)
    populate_tables(engine)


def SignIn(engine, client_id):
    from populating_tables import insert_clients_base
    import re
    name = input("Введите ваше имя: ")
    if len(name) > 30:
        print("Ошибка: имя должно содержать не больше 30 символов")
        return None
    password = input("Введите ваш пароль: ")
    if len(password) > 30:
        print("Ошибка: пароль должен содержать не больше 30 символов")
        return None
    phone = input("Введите ваш телефон: ")
    if len(phone) > 15:
        print("Ошибка: номер телефона не должен превышать 15 знаков")
        return None
    insert_clients_base(engine, name, password, phone)
    print("Регистрация прошла успешно")
    my_id = engine.execute("select count(*) from clients_base").fetchone()[0]
    return tuple(('user', my_id))


def LogIn(engine, client_id):
    name = input("Введите ваше имя: ")
    if len(name) > 30:
        print("Ошибка: имя должно содержать не больше 30 символов")
        return None
    password = input("Введите ваш пароль: ")
    if len(password) > 30:
        print("Ошибка: пароль должен содержать не больше 30 символов")
        return None
    if name == 'sleep_admin' and password == 'qwerty':
        return tuple(('admin', 1))
    if name == 'alone_manager' and password == '123456':
        return tuple(('manager', 1))
    if "'" in (name+password):
        print("Использование ' недопустимо")
    my_id = engine.execute(f"select id from clients_base where name='{name}' and password='{password}'").fetchall()
    if len(my_id) == 0:
        print("Неправильный логин или пароль")
        return None
    my_id = my_id[0][0]
    print("Авторизация прошла успешно!")
    if my_id == 1:
        return tuple(('manager', 1))
    return tuple(('user', my_id))


def End(engine, client_id):
    from sys import exit
    print("Программа завершила свою роботу.")
    exit()


def SelectPartsInStock(engine, client_id):
    """Выводит информацию о товаре на складе."""
    from select_tables import select_parts_in_stock
    table = [('id', 'section', 'part_type', 'number', 'supplier', 'manufacturer', 'date'),]
    table = table + select_parts_in_stock(engine)
    print(tabulate(table, headers='firstrow'))


def SelectPartsInStock_special(engine, client_id):
    """Выводит информацию о товаре на складе по id товара."""
    from select_tables import select_parts_in_stock
    part_id = input("Введите id товара: ")
    if part_id.isdigit():
        table = [('id', 'section', 'part_type', 'number', 'supplier', 'manufacturer', 'date'),]
        table = table + select_parts_in_stock(engine, part_id)
        print(tabulate(table, headers='firstrow'))
    else:
        print("Ошибка: id может быть только целым числом")


def AddOrder(engine, client_id):
    """Добавляет заказ покупателя в очередь на подтверждение"""
    from populating_tables import insert_applications_pending
    part_name = input("Введите название товара: ")
    if len(part_name) > 30:
        print("Ошибка: название товара не может превышать 30 символов")
    else:
        number = input("Введите количество товара: ")
        if not number.isdigit() or int(number) <= 0:
            print(f"Ошибка: количество товара должно быть натуральным числом {number}")
        else:
            insert_applications_pending(engine, part_name, number, client_id)
            print("Заказ создан успешно")


def GetMyOrders(engine, client_id):
    """Выводит информацию о неподтвержденных заказах клиента."""
    from select_tables import select_applications_pending
    table = [('id', 'part_name', 'number', 'client')]
    table = table + select_applications_pending(engine, client_id)
    print(tabulate(table, headers='firstrow'))


def GetOrders(engine, client_id):
    """Выводит информацию о неподтвержденных заказах."""
    from select_tables import select_applications_pending
    table = [('part_name', 'number', 'client')]
    table = table + select_applications_pending(engine)
    print(tabulate(table, headers='firstrow'))


def SelectPartsCatalog(engine, client_id):
    """Выводит полный каталог деталей"""
    from select_tables import select_parts_catalog
    table = [('id', 'name', 'price', 'size'), ]
    table = table + select_parts_catalog(engine)
    print(tabulate(table, headers='firstrow'))


def SelectPartsCatalog_special(engine, client_id):
    """Выводит деталь по ай-ди."""
    from select_tables import select_parts_catalog
    part_id = input("Введите id товара: ")
    if part_id.isdigit():
        table = [('id', 'name', 'price', 'size'), ]
        table = table + select_parts_catalog(engine, part_id)
        print(tabulate(table, headers='firstrow'))
    else:
        print("Ошибка: id может быть только целым числом")


def SelectSupplierNomenclature(engine, client_id):
    """Выводит список поставщиков."""
    from select_tables import select_supplier_nomenclature
    table = [('id', 'name', 'country', 'type', 'time of delivery', 'percentage_price'), ]
    table = table + select_supplier_nomenclature(engine)
    print(tabulate(table, headers='firstrow'))


def SelectSupplierNomenclature_special(engine, client_id):
    """Выводит поставщика по ай-ди."""
    from select_tables import select_supplier_nomenclature
    supplier_id = input("Введите id поставщика: ")
    if supplier_id.isdigit():
        table = [('id', 'name', 'country', 'type', 'time of delivery', 'percentage_price'), ]
        table = table + select_supplier_nomenclature(engine, supplier_id)
        print(tabulate(table, headers='firstrow'))
    else:
        print("Ошибка: id может быть только целым числом")


def SelectWarehouseSections(engine, client_id):
    """Выводит список секций склада."""
    from select_tables import select_warehouse_sections
    table = [('id', 'alias', 'part_type', 'total_size'), ]
    table = table + select_warehouse_sections(engine)
    print(tabulate(table, headers='firstrow'))


def SelectWarehouseSections_special(engine, client_id):
    """Выводит секцию склада по её номеру."""
    from select_tables import select_warehouse_sections
    section_id = input("Введите id секции: ")
    if section_id.isdigit():
        table = [('id', 'alias', 'part_type', 'total_size'), ]
        table = table + select_warehouse_sections(engine, section_id)
        print(tabulate(table, headers='firstrow'))
    else:
        print("Ошибка: id может быть только целым числом")


def SelectClientsBase(engine, client_id):
    """Выводит список клиентов."""
    from select_tables import select_clients_base
    table = [('id', 'name', 'password', 'phone'), ]
    table = table + select_clients_base(engine)
    print(tabulate(table, headers='firstrow'))


def SelectClientsBase_special(engine, client_id):
    """Выводит клиента по его ай-ди."""
    from select_tables import select_clients_base
    client_id = input("Введите id клиента: ")
    if client_id.isdigit():
        table = [('id', 'alias', 'part_type', 'total_size'), ]
        table = table + select_clients_base(engine, client_id)
        print(tabulate(table, headers='firstrow'))
    else:
        print("Ошибка: id может быть только целым числом")


def SelectWarehouseOrders(engine, client_id):
    """Выводит список касовых чеков."""
    from select_tables import select_warehouse_orders
    table = [('id', 'date', 'client', 'part', 'section', 'number', 'supplier', 'manufacturer'), ]
    table = table + select_warehouse_orders(engine)
    print(tabulate(table, headers='firstrow'))


def SelectWarehouseOrders_special(engine, client_id):
    """Выводит заказ по его ай-ди."""
    from select_tables import select_warehouse_orders
    order_id = input("Введите id заказа: ")
    if order_id.isdigit():
        table = [('id', 'date', 'client', 'part', 'section', 'number', 'supplier', 'manufacturer'), ]
        table = table + select_warehouse_orders(engine, order_id)
        print(tabulate(table, headers='firstrow'))
    else:
        print("Ошибка: id может быть только целым числом")


def SelectSupplierOrders(engine, client_id):
    """Выводит информацию о заявках поставщику"""
    from select_tables import select_supplier_orders
    table = [('id', 'date', 'client', 'part', 'executed', 'number', 'supplier', 'manufacturer'), ]
    table = table + select_supplier_orders(engine)
    print(tabulate(table, headers='firstrow'))


def SelectSupplierOrders_special(engine, client_id):
    """Выводит заказ по его ай-ди."""
    from select_tables import select_supplier_orders
    order_id = input("Введите id заказа: ")
    if order_id.isdigit():
        table = [('id', 'date', 'client', 'part', 'executed', 'number', 'supplier', 'manufacturer'), ]
        table = table + select_supplier_orders(engine, order_id)
        print(tabulate(table, headers='firstrow'))
    else:
        print("Ошибка: id может быть только целым числом")


def SelectOverheads(engine, client_id):
    """Выводит накладные расходы."""
    from select_tables import select_overheads
    table = [('id', 'type', 'explanation', 'date', 'money'), ]
    table = table + select_overheads(engine)
    print(tabulate(table, headers='firstrow'))


def SelectOverheads_special(engine, client_id):
    """Выводит накладные расходы по ай-ди."""
    from select_tables import select_overheads
    overheads_id = input("Введите id накладного расхода: ")
    if overheads_id.isdigit():
        table = [('id', 'type', 'explanation', 'date', 'money'), ]
        table = table + select_overheads(engine, overheads_id)
        print(tabulate(table, headers='firstrow'))
    else:
        print("Ошибка: id может быть только целым числом")


def SelectDefectsRegister(engine, client_id):
    """Выводит содержимое журнала брака."""
    from select_tables import select_defects_register
    table = [('id', 'date', 'part', 'supplier', 'manufactor', 'number'), ]
    table = table + select_defects_register(engine)
    print(tabulate(table, headers='firstrow'))


def SelectDefectsRegister_special(engine, client_id):
    """Выводит содержимое журнала брака по ай-ди."""
    from select_tables import select_defects_register
    overheads_id = input("Введите id записи: ")
    if overheads_id.isdigit():
        table = [('id', 'date', 'part', 'supplier', 'manufactor', 'number'), ]
        table = table + select_defects_register(engine, overheads_id)
        print(tabulate(table, headers='firstrow'))
    else:
        print("Ошибка: id может быть только целым числом")


def ExecuteSupplierOrder(engine, client_id):
    """Переключает состояние заказа у поставщика на выполнено"""
    from update_tables import execute_supplier_order, add_to_warehouse, get_from_warehouse
    order_id = input("Введите id заказа: ")
    if order_id.isdigit():
        s_order = engine.execute(f"select * from supplier_orders where id='{order_id}'").fetchall()
        if len(s_order) != 0:
            s_order = s_order[0]
            execute_supplier_order(engine, order_id)
            date = s_order[1]
            ttd = engine.execute(f"""select time_of_delivery from supplier_nomenclature where 
                                 id='{s_order[6]}'""").fetchall()[0][0]
            date = engine.execute(f"select date_add('{date}', interval '{ttd}' day)").fetchone()[0]
            add_to_warehouse(engine, s_order[3], s_order[5], s_order[6], s_order[7], date)
            if str(s_order[2]) != '1':
                get_from_warehouse(engine, s_order[3], s_order[5], date, s_order[2])
        else:
            print("Ошибка: заказа с таким id не существует")
    else:
        print("Ошибка: id может быть только целым числом")


def ChangeSupplierPrice(engine, client_id):
    """Изменяет ценовую политику поставщика."""
    from update_tables import change_supplier_price
    supplier_id = input("Введите id поставщика: ")
    if supplier_id.isdigit():
        new_price = input("Введите новый процент поставщика: ")
        if new_price.isdigit() and int(new_price) > 0:
            change_supplier_price(engine, supplier_id, new_price)
        else:
            print("Ошибка: процент должен быть натуральным числом.")
    else:
        print("Ошибка: id может быть только целым числом")


def InsertSupplierNomenclature(engine, client_id):
    """Добавляет нового поставщика"""
    from populating_tables import insert_supplier_nomenclature
    name = input("Введите название поставщика: ")
    if len(name) > 30:
        print("Ошибка: название поставщика не должно превышать 30 символов")
    else:
        country = input("Введите страну поставщика: ")
        if len(country) > 30:
            print("Ошибка: название страны не должно превышать 30 символов")
        else:
            supplier_type = input("Введите тип поставщика: ")
            if supplier_type not in ('dealer', 'small store', 'large firm', 'small firm'):
                print("Ошибка: допустимы только типы 'dealer', 'small store', 'large firm', 'small firm'")
            else:
                time_of_delivery = input("Введите время доставки: ")
                if time_of_delivery.isdigit() and int(time_of_delivery) > 0:
                    percentage_price = input("Введите процентную долю поставщика: ")
                    if percentage_price.isdigit() and int(percentage_price) > 0:
                        insert_supplier_nomenclature(name, country, supplier_type, time_of_delivery, percentage_price)
                        print("Добавление нового поставщика прошло успешно")
                    else:
                        print("Ошибка: процентная доля поставщика должна быть натуральным числом")
                else:
                    print("Ошибка: время доставки должно быть натуральным числом")


def InsertWarehouseSections(engine, client_id):
    """Добавляет новую секцию склада."""
    from populating_tables import insert_warehouse_sections
    alias = input("Введите обозначение для секции: ")
    if len(alias) > 30:
        print("Ошибка: обозначение не должно превышать 30 символов")
    else:
        part_type = input("Введите id запчастей, которые должны хранится в этой секции: ")
        if not part_type.isdigit():
            print("Ошибка: id запчастей должно быть целым числом")
        else:
            total_size = ("Введите размер секции (в у.е.): ")
            if total_size.isdigit() and int(total_size) >= 100:
                insert_warehouse_sections(engine, alias, part_type, total_size)
                print("Секция успешно добавлена")
            else:
                print("Ошибка: размер секции должен быть целым числом не меньше 100")


def GetFromWarehouse(engine, client_id):
    """Осуществляет продажу деталей со склада"""
    from update_tables import get_from_warehouse
    from datetime import date
    part_id = input("Введите id детали: ")
    if part_id.isdigit():
        number = input("Введите количество деталей: ")
        if number.isdigit() and int(number) > 0:
            client = input("Введите id клиента: ")
            if client.isdigit():
                _date = str(date.today())
                get_from_warehouse(engine, part_id, number, _date, client)
            else:
                print("Ошибка: id должно быть целым числом.")
        else:
            print("Ошибка: количество деталей должно быть натуральным числом.")
    else:
        print("Ошибка: id должно быть целым числом.")


def InsertOverheads(engine, client_id):
    """Добавляет информацию о накладных расходах"""
    from populating_tables import insert_overheads
    from datetime import date
    overhead_type = input("Введите тип накладных расходов: ")
    if len(overhead_type) > 20:
        print("Ошибка: тип накладных расходов не должен превышать 20 символов")
    else:
        explanation = input("Введите дополнительную информацию про накладные расходы: ")
        if len(explanation) > 40:
            print("Ошибка: дополнительная информация про накладные расходы не должна превышать 40 символов")
        else:
            money = input("Введите сумму накладных расходов: ")
            if money.isdigit() and int(money) > 0:
                _date = str(date.today())
                insert_overheads(engine, overhead_type, explanation, _date, money)
                print("Накладные расходы успешно добавлены")
            else:
                print("Ошибка: сумма накладных расходов должна быть натуральным числом")


def InsertDefectsRegister(engine, client_id):
    """Добавляет информацию о браке"""
    from populating_tables import insert_defects_register, insert_supplier_orders
    from datetime import date
    part_id = input("Введите id товара: ")
    if part_id.isdigit():
        supplier_id = input("Введите id поставщика: ")
        if supplier_id.isdigit():
            manufacturer_id = input("Введите id изготовителя: ")
            if manufacturer_id.isdigit():
                number = input("Введите количество: ")
                if number.isdigit() and int(number) > 0:
                    _date = str(date.today())
                    insert_defects_register(engine, _date, part_id, supplier_id, manufacturer_id, number)
                    print("Запись о браке успешно добавлена")
                    s_type = engine.execute(f"""select type from supplier_nomenclature 
                                            where id='{supplier_id}'""").fetchone()[0]
                    if s_type in ('dealer', 'large firm'):
                        insert_supplier_orders(engine, _date, client_id, part_id, '0', number,
                                               supplier_id, manufacturer_id)
                        print("Брак отправлен обратно поставщику по гарантии")
            else:
                print("Ошибка: id может быть только целым числом")
        else:
            print("Ошибка: id может быть только целым числом")
    else:
        print("Ошибка: id может быть только целым числом")


def InsertPartsCatalog(engine, client_id):
    """Добавляет в каталог новую деталь."""
    from populating_tables import insert_parts_catalog
    name = input("Введите название запчасти: ")
    if len(name) > 30:
        print("Ошибка: название детали должно не превышать 30 символов")
    else:
        price = input("Введите цену продажи запчасти: ")
        if price.isdigit() and int(price) > 0:
            size = input("Введите размер запчасти (в у.е.): ")
            if size.isdigit() and int(size) > 0:
                insert_parts_catalog(engine, name, price, size)
                print("Добавление новой детали в каталог прошло успешно")
            else:
                print("Ошибка: размер запчасти должна быть целым положительным числом")
        else:
            print("Ошибка: цена запчасти должна быть целым положительным числом")


def GetSpecialSupplier(engine, client_id):
    """Выводит список поставщиков определенного вида, поставивших определенный товар."""
    from requests import request_1_1
    supplier_type = input("Введите тип поставщика: ")
    if supplier_type not in ('dealer', 'small store', 'large firm', 'small firm'):
        print("Ошибка: допустимы только типы 'dealer', 'small store', 'large firm', 'small firm'")
    else:
        part_id = input("Введите id товара")
        if part_id.isdigit():
            table = [('supplier_id',), ]
            table = table + request_1_1(engine, supplier_type, part_id)
            print(tabulate(table, headers='firstrow'))
        else:
            print("Ошибка: id может быть только целым числом")


def GetNumberOfSpecialSupplier(engine, client_id):
    """Выводит количество поставщиков определенного вида, поставивших определенный товар."""
    from requests import request_1_2
    supplier_type = input("Введите тип поставщика: ")
    if supplier_type not in ('dealer', 'small store', 'large firm', 'small firm'):
        print("Ошибка: допустимы только типы 'dealer', 'small store', 'large firm', 'small firm'")
    else:
        part_id = input("Введите id товара")
        if part_id.isdigit():
            table = [('supplier_count',), ]
            table = table + request_1_2(engine, supplier_type, part_id)
            print(tabulate(table, headers='firstrow'))
        else:
            print("Ошибка: id может быть только целым числом")


def GetSpecialSupplierByDateNumber(engine, client_id):
    """Выводит список поставщиков определенного вида, поставивших определенный товар как минимум определенного
       количества в определенный период"""
    from requests import request_1_3
    supplier_type = input("Введите тип поставщика: ")
    if supplier_type not in ('dealer', 'small store', 'large firm', 'small firm'):
        print("Ошибка: допустимы только типы 'dealer', 'small store', 'large firm', 'small firm'")
    else:
        part_id = input("Введите id товара")
        if part_id.isdigit():
            date_1 = input("Введите начальную дату в формате ГГГГ-ММ-ДД: ")
            if check_date(date_1):
                date_2 = input("Введите конечную дату в формате ГГГГ-ММ-ДД: ")
                if check_date(date_2):
                    threshold = input("Введите минимальное необходимое количество: ")
                    if threshold.isdigit():
                        table = [('supplier_id',), ]
                        table = table + request_1_3(engine, supplier_type, part_id)
                        print(tabulate(table, headers='firstrow'))
                    else:
                        print("Ошибка: минимально необходимое количество должно быть целым")
                else:
                    print("Ошибка: дата введена некорректно")
            else:
                print("Ошибка: дата введена некорректно")
        else:
            print("Ошибка: id может быть только целым числом")


def GetNumberOfSpecialSupplierByDateNumber(engine, client_id):
    """Выводит количество поставщиков определенного вида, поставивших определенный товар как минимум определенного
       количества в определенный период"""
    from requests import request_1_4
    supplier_type = input("Введите тип поставщика: ")
    if supplier_type not in ('dealer', 'small store', 'large firm', 'small firm'):
        print("Ошибка: допустимы только типы 'dealer', 'small store', 'large firm', 'small firm'")
    else:
        part_id = input("Введите id товара")
        if part_id.isdigit():
            date_1 = input("Введите начальную дату в формате ГГГГ-ММ-ДД: ")
            if check_date(date_1):
                date_2 = input("Введите конечную дату в формате ГГГГ-ММ-ДД: ")
                if check_date(date_2):
                    threshold = input("Введите минимальное необходимое количество: ")
                    if threshold.isdigit():
                        table = [('supplier_count',), ]
                        table = table + request_1_4(engine, supplier_type, part_id)
                        print(tabulate(table, headers='firstrow'))
                    else:
                        print("Ошибка: минимально необходимое количество должно быть целым")
                else:
                    print("Ошибка: дата введена некорректно")
            else:
                print("Ошибка: дата введена некорректно")
        else:
            print("Ошибка: id может быть только целым числом")


def GetInfoForSpecialPart(engine, client_id):
    """Выводит данные про конкретный вид деталей: поставщиков, их расценки, время поставки"""
    from requests import request_2
    part_id = input("Введите id товара")
    if part_id.isdigit():
        table = [('part_id',), ]
        table = table + request_2(engine, part_id)
        print(tabulate(table, headers='firstrow'))
    else:
        print("Ошибка: id может быть только целым числом")


def GetSpecialClientByDate(engine, client_id):
    """Выводит список клиентов, купивших конкретный вид деталей за определенный период"""
    from requests import request_3_1
    part_id = input("Введите id товара")
    if part_id.isdigit():
        date_1 = input("Введите начальную дату в формате ГГГГ-ММ-ДД: ")
        if check_date(date_1):
            date_2 = input("Введите конечную дату в формате ГГГГ-ММ-ДД: ")
            if check_date(date_2):
                table = [('client_id',), ]
                table = table + request_3_1(engine, part_id, date_1, date_2)
                print(tabulate(table, headers='firstrow'))
            else:
                print("Ошибка: дата введена некорректно")
        else:
            print("Ошибка: дата введена некорректно")
    else:
        print("Ошибка: id может быть только целым числом")


def GetNumberOfSpecialClientByDate(engine, client_id):
    """Выводит количество клиентов, купивших конкретный вид деталей за определенный период"""
    from requests import request_3_2
    part_id = input("Введите id товара")
    if part_id.isdigit():
        date_1 = input("Введите начальную дату в формате ГГГГ-ММ-ДД: ")
        if check_date(date_1):
            date_2 = input("Введите конечную дату в формате ГГГГ-ММ-ДД: ")
            if check_date(date_2):
                table = [('client_count',), ]
                table = table + request_3_2(engine, part_id, date_1, date_2)
                print(tabulate(table, headers='firstrow'))
            else:
                print("Ошибка: дата введена некорректно")
        else:
            print("Ошибка: дата введена некорректно")
    else:
        print("Ошибка: id может быть только целым числом")


def GetSpecialClientByNumber(engine, client_id):
    """Выводит список клиентов, купивших конкретный товар в определенном количестве"""
    from requests import request_3_3
    part_id = input("Введите id товара")
    if part_id.isdigit():
        threshold = input("Введите минимальное необходимое количество: ")
        if threshold.isdigit():
            table = [('client_id',), ]
            table = table + request_3_3(engine, part_id, threshold)
            print(tabulate(table, headers='firstrow'))
        else:
            print("Ошибка: минимально необходимое количество должно быть целым")
    else:
        print("Ошибка: id может быть только целым числом")


def GetNumberOfSpecialClientByNumber(engine, client_id):
    """Выводит количество клиентов, купивших конкретный товар в определенном количестве"""
    from requests import request_3_4
    part_id = input("Введите id товара")
    if part_id.isdigit():
        threshold = input("Введите минимальное необходимое количество: ")
        if threshold.isdigit():
            table = [('client_count',), ]
            table = table + request_3_4(engine, part_id, threshold)
            print(tabulate(table, headers='firstrow'))
        else:
            print("Ошибка: минимально необходимое количество должно быть целым")
    else:
        print("Ошибка: id может быть только целым числом")


def GetPartsInStockInfo(engine, client_id):
    """Выводит список, размер и номер ячейки для всех деталей, хранящихся на складе"""
    from requests import request_4
    table = [('part_type', 'section_number', 'total_size'), ]
    table = table + request_4(engine)
    print(tabulate(table, headers='firstrow'))


def GetTenPopularParts(engine, client_id):
    """Выводит список, размер и номер ячейки для всех деталей, хранящихся на складе"""
    from requests import request_5_1
    table = [('part_id',), ]
    table = table + request_5_1(engine)
    print(tabulate(table, headers='firstrow'))


def GetTenCheapestSuppliers(engine, client_id):
    """Выводит список из 10-ти самых "дешевых" поставщиков в порядке возрастания"""
    from requests import request_5_2
    table = [('supplier_id',), ]
    table = table + request_5_2(engine)
    print(tabulate(table, headers='firstrow'))


def GetAverageSalesPerMonth(engine, client_id):
    """Выводит список средних продаж в месяц для каждой детали"""
    from requests import request_6
    table = [('part_id', 'sales_per_month'), ]
    table = table + request_6(engine)
    print(tabulate(table, headers='firstrow'))


def GetSpecialSupplierAmountOfIncome(engine, client_id):
    """Выводит долю товара конкретного поставщика в процентах, деньгах, единицах от всего оборота магазина
       за указанный период"""
    from requests import request_7_1, request_7_2, request_7_3, request_7_4
    s_id = input("Введите id поставщика")
    if s_id.isdigit():
        date_1 = input("Введите начальную дату в формате ГГГГ-ММ-ДД: ")
        if check_date(date_1):
            date_2 = input("Введите конечную дату в формате ГГГГ-ММ-ДД: ")
            if check_date(date_2):
                table = [('parts_number', 'parts_amount_number', 'money_number', 'turnover_amount_number'), ]
                table = table + [(request_7_1(engine, s_id, date_1, date_2), request_7_2(engine, s_id, date_1, date_2),
                                  request_7_3(engine, s_id, date_1, date_2), request_7_4(engine, s_id, date_1, date_2)
                                  ), ]
                print(tabulate(table, headers='firstrow'))
            else:
                print("Ошибка: дата введена некорректно")
        else:
            print("Ошибка: дата введена некорректно")
    else:
        print("Ошибка: id может быть только целым числом")


def GetSpecialSupplierAmountOfGain(engine, client_id):
    """Выводит долю товара конкретного поставщика в процентах, деньгах от всего дохода магазина
       за указанный период"""
    from requests import request_7_3, request_7_5
    s_id = input("Введите id поставщика: ")
    if s_id.isdigit():
        date_1 = input("Введите начальную дату в формате ГГГГ-ММ-ДД: ")
        if check_date(date_1):
            date_2 = input("Введите конечную дату в формате ГГГГ-ММ-ДД: ")
            if check_date(date_2):
                table = [('money_number', 'gain_amount_number'), ]
                table = table + [(request_7_3(engine, s_id, date_1, date_2), request_7_5(engine, s_id, date_1, date_2)
                                  ), ]
                print(tabulate(table, headers='firstrow'))
            else:
                print("Ошибка: дата введена некорректно")
        else:
            print("Ошибка: дата введена некорректно")
    else:
        print("Ошибка: id может быть только целым числом")


def GetOverheadsAmountOfIncome(engine, client_id):
    """Выводит накладные расходы в процентах от объема продаж"""
    from requests import request_8
    table = [('overheads_amount',), ]
    table = table + [(request_8(engine),), ]
    print(tabulate(table, headers='firstrow'))


def GetUnsoldPartsByDate(engine, client_id):
    """Выводит список непроданного товара на складе за определенный период"""
    from requests import request_9_1
    date_1 = input("Введите начальную дату в формате ГГГГ-ММ-ДД: ")
    if check_date(date_1):
        date_2 = input("Введите конечную дату в формате ГГГГ-ММ-ДД: ")
        if check_date(date_2):
            table = [('part_type', 'part_number'), ]
            table = table + request_9_1(engine, date_1, date_2)
            print(tabulate(table, headers='firstrow'))
        else:
            print("Ошибка: дата введена некорректно")
    else:
        print("Ошибка: дата введена некорректно")


def GetNumberOfUnsoldPartsByDate(engine, client_id):
    """Выводит количество непроданного товара на складе за определенный период"""
    from requests import request_9_2
    date_1 = input("Введите начальную дату в формате ГГГГ-ММ-ДД: ")
    if check_date(date_1):
        date_2 = input("Введите конечную дату в формате ГГГГ-ММ-ДД: ")
        if check_date(date_2):
            table = [('total_part_number',), ]
            table = table + [(request_9_2(engine, date_1, date_2),), ]
            print(tabulate(table, headers='firstrow'))
        else:
            print("Ошибка: дата введена некорректно")
    else:
        print("Ошибка: дата введена некорректно")


def GetUnsoldPartsAmountByDate(engine, client_id):
    """Выводит долю в процентах непроданного товара от общего товара за определенный период"""
    from requests import request_9_3
    date_1 = input("Введите начальную дату в формате ГГГГ-ММ-ДД: ")
    if check_date(date_1):
        date_2 = input("Введите конечную дату в формате ГГГГ-ММ-ДД: ")
        if check_date(date_2):
            table = [('unsold_part_amount',), ]
            table = table + [(request_9_3(engine, date_1, date_2),), ]
            print(tabulate(table, headers='firstrow'))
        else:
            print("Ошибка: дата введена некорректно")
    else:
        print("Ошибка: дата введена некорректно")


def GetDefectPartsInfoByDate(engine, client_id):
    """Выводит список бракованого товара за определенный период"""
    from requests import request_10_1
    date_1 = input("Введите начальную дату в формате ГГГГ-ММ-ДД: ")
    if check_date(date_1):
        date_2 = input("Введите конечную дату в формате ГГГГ-ММ-ДД: ")
        if check_date(date_2):
            table = [('part' 'number_of_parts',), ]
            table = table + request_10_1(engine, date_1, date_2)
            print(tabulate(table, headers='firstrow'))
        else:
            print("Ошибка: дата введена некорректно")
    else:
        print("Ошибка: дата введена некорректно")


def GetNumberOfDefectPartsInfoByDate(engine, client_id):
    """Выводит количество бракованого товара за определенный период"""
    from requests import request_10_2
    date_1 = input("Введите начальную дату в формате ГГГГ-ММ-ДД: ")
    if check_date(date_1):
        date_2 = input("Введите конечную дату в формате ГГГГ-ММ-ДД: ")
        if check_date(date_2):
            table = [('number_of_defect_parts',), ]
            table = table + request_10_2(engine, date_1, date_2)
            print(tabulate(table, headers='firstrow'))
        else:
            print("Ошибка: дата введена некорректно")
    else:
        print("Ошибка: дата введена некорректно")


def GetDefectSupplierInfoByDate(engine, client_id):
    """Выводит поставщиков, поставивших брак за определенный период"""
    from requests import request_10_3
    date_1 = input("Введите начальную дату в формате ГГГГ-ММ-ДД: ")
    if check_date(date_1):
        date_2 = input("Введите конечную дату в формате ГГГГ-ММ-ДД: ")
        if check_date(date_2):
            table = [('defects_supplier',), ]
            table = table + request_10_3(engine, date_1, date_2)
            print(tabulate(table, headers='firstrow'))
        else:
            print("Ошибка: дата введена некорректно")
    else:
        print("Ошибка: дата введена некорректно")


def GetSoldPartsByDay(engine, client_id):
    """Выводит список проданого за день товара"""
    from requests import request_11_1
    _date = input("Введите дату в формате ГГГГ-ММ-ДД: ")
    if check_date(_date):
        table = [('part_id', 'part_number'), ]
        table = table + request_11_1(engine, _date)
        print(tabulate(table, headers='firstrow'))
    else:
        print("Ошибка: дата введена некорректно")


def GetNumberOfSoldPartsByDay(engine, client_id):
    """Выводит общее количество проданого за день товара"""
    from requests import request_11_2
    _date = input("Введите дату в формате ГГГГ-ММ-ДД: ")
    if check_date(_date):
        table = [('daily_part_number',), ]
        table = table + request_11_2(engine, _date)
        print(tabulate(table, headers='firstrow'))
    else:
        print("Ошибка: дата введена некорректно")


def GetIncomeByDay(engine, client_id):
    """Выводит стоимость проданого за день товара"""
    from requests import request_11_3
    _date = input("Введите дату в формате ГГГГ-ММ-ДД: ")
    if check_date(_date):
        table = [('daily_income',), ]
        table = table + request_11_3(engine, _date)
        print(tabulate(table, headers='firstrow'))
    else:
        print("Ошибка: дата введена некорректно")


def GetCashReport(engine, client_id):
    """Выводит касовый отчет за определенный период"""
    from requests import request_12
    date_1 = input("Введите начальную дату в формате ГГГГ-ММ-ДД: ")
    if check_date(date_1):
        date_2 = input("Введите конечную дату в формате ГГГГ-ММ-ДД: ")
        if check_date(date_2):
            table = [('date', 'day_orders', 'day_number', 'day_income'), ]
            table = table + request_12(engine, date_1, date_2)
            print(tabulate(table, headers='firstrow'))
        else:
            print("Ошибка: дата введена некорректно")
    else:
        print("Ошибка: дата введена некорректно")


def GetInventoryStatement(engine, client_id):
    """Выводит инвентаризационную ведомость"""
    from requests import request_13
    table = [('part_id', 'name', 'total_parts', 'total_price'), ]
    table = table + request_13(engine)
    print(tabulate(table, headers='firstrow'))


def GetDailyTurnoverSpeed(engine, client_id):
    """Выводит инвентаризационную ведомость"""
    from requests import request_14
    table = [('daily_turnover_speed',), ]
    table = table + request_14(engine)
    print(tabulate(table, headers='firstrow'))


def GetEmptyCages(engine, client_id):
    """Выводит количество пустых ячеек на складе"""
    from requests import request_15_1
    table = [('empty_sections',), ]
    table = table + request_15_1(engine)
    print(tabulate(table, headers='firstrow'))


def GetWarehouseCapacity(engine, client_id):
    """Выводит общий объем склада"""
    from requests import request_15_3
    table = [('total_warehouse_capacity',), ]
    table = table + request_15_3(engine)
    print(tabulate(table, headers='firstrow'))


def GetFreeWarehouseCapacity(engine, client_id):
    """Выводит незанятый объем склада"""
    from requests import request_15_2
    table = [('empty_warehouse_capacity',), ]
    table = table + request_15_2(engine)
    print(tabulate(table, headers='firstrow'))


def GetExpectedClientsOrders(engine, client_id):
    """Выводит список заявок от покупателей на ожидаемый товар"""
    from requests import request_16_1
    table = [('id', 'part', 'number',), ]
    table = table + request_16_1(engine)
    print(tabulate(table, headers='firstrow'))


def GetNumberOfExpectedClientsOrders(engine, client_id):
    """Выводит количество заявок от покупателей на ожидаемый товар"""
    from requests import request_16_2
    table = [('number_of_expected_orders',), ]
    table = table + request_16_2(engine)
    print(tabulate(table, headers='firstrow'))


def GetSumOfExpectedClientsOrders(engine, client_id):
    """Выводит общую сумму заявок от покупателей на ожидаемый товар"""
    from requests import request_16_3
    table = [('sum_of_expected_orders',), ]
    table = table + request_16_3(engine)
    print(tabulate(table, headers='firstrow'))