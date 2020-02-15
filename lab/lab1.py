import re
from lab.lab1_ui import Ui_Semmetric_difference
from PyQt5 import QtWidgets, QtCore


class Lab1(Ui_Semmetric_difference):
    def __init__(self):
        self._union = set('Ø')
        self._set_difference_f_s = set('Ø')
        self._set_difference_s_f = set('Ø')
        self._intersection = set('Ø')
        self._symmetric_difference = set('Ø')
        self._translate = QtCore.QCoreApplication.translate

    def data(self):
        self.Union.clicked.connect(self._show_union)
        self.Set_difference_f_s.clicked.connect(self._show_set_difference_f_s)
        self.Set_difference_s_f.clicked.connect(self._show_set_difference_s_f)
        self.Intersection.clicked.connect(self._show_intersection)
        self.Symmetric_difference.clicked.connect(self._show_symmetric_difference)

    def _show_union(self):
        self._get_union()
        self.output.setText(str(self._union))

    def _show_set_difference_f_s(self):
        self._get_set_difference()
        self.output.setText(str(self._set_difference_f_s))

    def _show_set_difference_s_f(self):
        self._get_set_difference()
        self.output.setText(str(self._set_difference_s_f))

    def _show_intersection(self):
        self._get_intersection()
        self.output.setText(str(self._intersection))

    def _show_symmetric_difference(self):
        self._get_symmetric_difference()
        self.output.setText(str(self._symmetric_difference))

    def _get_union(self):
        first_array, second_array = self._get_arrays()
        self._union = set(first_array + second_array)

    def _get_set_difference(self):
        first_array, second_array = self._get_arrays()
        self._set_difference_f_s = set(first_array) - set(second_array) or set('Ø')
        self._set_difference_s_f = set(second_array) - set(first_array) or set('Ø')

    def _get_intersection(self):
        self._get_symmetric_difference()
        self._get_union()
        self._intersection = set(self._union) - set(self._symmetric_difference) or set('Ø')

    def _get_symmetric_difference(self):
        self._get_set_difference()
        self._symmetric_difference = set(list(self._set_difference_f_s) + list(self._set_difference_s_f))

    def _get_arrays(self):
        first_string = self.FArrayEdit.text()
        first_array = self.string_to_array(first_string)
        second_string = self.SArrayEdit.text()
        second_array = self.string_to_array(second_string)
        return first_array, second_array

    @staticmethod
    def string_to_array(string):
        pattern_int = r'(?<![-.])\b[0-9]+\b(?!\.[0-9])|[Ø]'
        pattern_float = r'[-+]?\d+[.]\d+'
        array_float = re.findall(pattern_float, string)
        array_int = re.findall(pattern_int, ' ' + string + ' ')
        array = []
        array += list(map(lambda x: int(x), array_int))
        array += list(map(lambda x: float(x), array_float))
        if not array:
            array.append('Ø')
        else:
            array.sort()
        return array


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Semmetric_difference = QtWidgets.QMainWindow()
    ui = Lab1()
    ui.setupUi(Semmetric_difference)
    ui.data()
    Semmetric_difference.show()
    sys.exit(app.exec_())
