__author__ = 'Omer'


class Field(object):
    def __init__(self, modulo=1):
        self._modulo = modulo

    def sum(self, *elements):
        raise NotImplementedError

    def mul(self, first_element, *elements):
        raise NotImplementedError

    def get_negative(self, element):
        raise NotImplementedError

    def get_inverse(self, element):
        raise NotImplementedError

    def sub(self, first_element, *elements):
        raise NotImplementedError

    def pow(self, base, *powers):
        raise NotImplementedError