from sqlalchemy import create_engine
from control_module import controller


def Authorize(engine):
    authorize = input("Если вы пользуетесь этой программой впервые, пожалуйста, зарегистрируйтесь.\n"
                      "Для того, чтобы начать регистрацию введите команду SignIn.\n"
                      "Если вы уже зарегистрированы, введите команду LogIn.\n"
                      "Если вы желаете покинуть программу, введите команду End\n"
                      "Для вызова справки введите команду Help\n")
    while authorize not in ('SignIn', 'LogIn', 'End'):
        authorize = input("Команда нераспознана. Попробуйте ещё раз, тщательно всё проверив: ")
    your_status = controller(engine, authorize)
    while your_status is None:
        print("Попытайтесь ещё раз.")
        your_status = controller(engine, authorize)
    print(f"Поздравляєм, вы успешно авторизировались.\nВаш уровень доступа {your_status[0]}.\nВаш id {your_status[1]}")
    return your_status







if __name__ == '__main__':
        # Подключаемся к серверу MySQL на localhost с помощью PyMySQL DB_API.
        my_engine = create_engine('mysql+pymysql://root:password@localhost:3306/autoparts_store')
        # Запускаем работу программы
        role, my_id = Authorize(my_engine)
        # role, my_id = ('admin', 1)
        while True:
            request = input("Введите команду: ")
            controller(my_engine, request, my_id, role)
