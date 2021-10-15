from abstarct.app.title import ABCAppTitle, AbcTitle

from config import NAME


class Title(AbcTitle):
    _HINT_IN_TITLE = "Press ESC to quit"
    __show_hint = True
    __text = ""

    @property
    def text(self):
        if self.__show_hint:
            return f"{NAME} [{self._HINT_IN_TITLE}] {self.__text}"
        else:
            return f"{NAME} {self.__text}"

    @text.setter
    def text(self, value):
        self.__text = value

    def enable_hint(self):
        self.__show_hint = True

    def disable_hint(self):
        self.__show_hint = False


class AppTitle(ABCAppTitle):
    def __get__(self, instance, owner=None):
        try:
            return instance.__title.text
        except AttributeError:
            instance.__title = Title()

        return instance.__title.text

    def __set__(self, instance, value):
        try:
            instance.__title.text = value
        except AttributeError:
            instance.__title = Title()
