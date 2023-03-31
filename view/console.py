from view.commands.menu import Menu
from view.validator import Validator
from view.view_abstract import View


class Console(View):

    __working = False
    __save = True
    __open = False

    def __init__(self):
        self.presenter = None

    def set_presenter(self, presenter):

        self.presenter = presenter

    def open_notebook(self):

        if not self.__open:
            self.presenter.open_file()
            self.__open = True
            if self.presenter.is_full():
                print("\nЗаписная книжка открыта")
            else:
                print("\nВ записной книжке нет записей")
        else:
            print("\nЗаписная книжка уже открыта!")

    def show_all(self):

        if self.presenter.is_full():
            print(self.presenter.get_notebook())
        else:
            print("\nЗаписная книжка не открыта или пуста!")

    def remove_note(self):

        if self.presenter.is_full():
            index = Validator.get_index(self.presenter.get_size_notebook(),
                                        "\nВведите номер заметки: ")
            self.presenter.remove_note(index)
            self.__save = False
            print("\nЗаметка удалена!\n")
        else:
            print("\nЗаписная книжка не открыта или пуста!")

    def change_note(self):

        if self.presenter.is_full():
            index = Validator.get_index(self.presenter.get_size_notebook(),
                                        "\nВведите номер заметки: ")
            update_note = input("\nОбновите заметку: ")
            self.presenter.change_note(index, update_note)
            self.__save = False
            print("\nЗаметка изменена!\n")
        else:
            print("\nЗаписная книжка не открыта или пуста!")

    def add_note(self):

        new_note = input("\nВведите заметку: ")
        self.presenter.add_note(new_note)
        print("\nЗаметка добавлена!\n")
        self.__save = False

    def finish(self):

        if self.__save:
            self.__working = False
        else:
            answer = input("\nСохранить изменения (да/нет)? ")
            if answer.lower() == 'да':
                self.presenter.save()
            self.__working = False
        print("\nЗавершение работы...")

    def save_changes(self):
        """Сохранение изменений"""
        self.presenter.save()
        self.__save = True
        print("\nИзменения сохранены")

    def start(self):
        """
        Начинает работу консоли, показывая меню и выполняя выбранные пользователем действия.
        Запрашивает у пользователя ввод, пока работа консоли не завершится.
        """
        self.__working = True
        menu = Menu(self)
        while self.__working:
            print(menu)
            index = Validator.get_index(menu.get_size_menu(), "\nВыберите пункт меню: ")
            menu.execute(index)
