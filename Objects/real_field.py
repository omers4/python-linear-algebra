from Objects.field import Field
from Objects.Errors import matrix_operation_illegal_exception as errors

__author__ = 'Omer'


class RealField(Field):
    def __init__(self, modulo=1):
        super(RealField, self).__init__(modulo)

    def sum(self, *elements):
        elements_sum = 0
        for element in elements:
            elements_sum = (elements_sum + element) % self._modulo
        return elements_sum

    def mul(self, first_element, *elements):
        elements_mul = first_element
        for element in elements:
            elements_mul = (elements_mul * element) % self._modulo
        return elements_mul

    def get_negative(self, element):
        return self._modulo - element

    def get_inverse(self, element):
        if element == 0:
            raise errors.MatrixOperationIllegal('0 Has no inverse number')
        for modulo_element in range(1, self._modulo):
            if self.mul(modulo_element, element) == 1:
                return modulo_element
        raise errors.MatrixOperationIllegal('Could not find inverse for ' + element)

    def sub(self, first_element, *elements):
        sub_value = first_element
        for element in elements:
            sub_value = self.sum(sub_value, self.get_negative(element))
        return sub_value

    def pow(self, base, *powers):
        pow_value = base
        for power in powers:
            pow_value = pow(pow_value, power, self._modulo)
        return pow_value