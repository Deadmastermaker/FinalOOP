from model.file_reader import FileReader


class Presenter:

    def __init__(self, view, notebook, path):
        self.__view = view
        self.__notebook = notebook
        self.__view.set_presenter(self)
        self.file = FileReader(path)

    def open_file(self):

        self.__notebook = self.file.file_read(self.__notebook)

    def save(self):

        self.file.save_changes(self.__notebook)

    def is_full(self):

        return self.__notebook.is_full()

    def add_note(self, text_note):

        self.__notebook.add_note(text_note)

    def remove_note(self, index):

        self.__notebook.remove(index)

    def change_note(self, index, update_text):

        self.__notebook.change_note(index, update_text)

    def get_size_notebook(self):

        return self.__notebook.size()

    def get_notebook(self):

        return self.__notebook