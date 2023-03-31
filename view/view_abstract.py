from abc import ABC, abstractmethod


class View(ABC):
    """
    Класс View является абстрактным базовым классом для всех классов представлений (Views)
    в приложении.
    Каждое представление должно реализовывать методы "set_presenter" и "start".
    """

    @abstractmethod
    def set_presenter(self, presenter):
        """
        Aбстрактный метод, который должен принимать экземпляр класса-презентера
        (Presenter) в качестве аргумента.
        """

    @abstractmethod
    def start(self):
        """
        Aбстрактный метод, который должен выполнять начальную настройку представления и
        запускать его отображение.
        """
