from datetime import datetime

from model.note import Note


class Notebook:


    def __init__(self):
        self.__notes = []

    def size(self):

        return len(self.__notes)

    def add_note(self, text_note):

        note = Note(datetime.today().strftime('%d.%m.%Y'), text_note)
        self.__notes.append(note)

    def remove(self, index):

        del self.__notes[index]

    def change_note(self, index, update_text):

        self.__notes[index].change_text(update_text)

    def __str__(self):

        notes_string = "\nСписок заметок:\n"
        for i, note in enumerate(self.__notes, start=1):
            notes_string += f"\t{i}. {note}\n"
        return notes_string

    def is_full(self):

        return bool(self.__notes)

    def get_notes(self):

        return self.__notes
