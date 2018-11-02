import math
from PyQt5 import QtWidgets
from ui_calculator import Ui_Calculator


class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):

    firstNumber = None
    userIsTyping = False

    def __init__(self):
        super(CalculatorWindow, self).__init__()
        self.setupUi(self)
        self.show()

        # Connect buttons
        self.pushButton_0.clicked.connect(self.digit_pressed)
        self.pushButton_1.clicked.connect(self.digit_pressed)
        self.pushButton_2.clicked.connect(self.digit_pressed)
        self.pushButton_3.clicked.connect(self.digit_pressed)
        self.pushButton_4.clicked.connect(self.digit_pressed)
        self.pushButton_5.clicked.connect(self.digit_pressed)
        self.pushButton_6.clicked.connect(self.digit_pressed)
        self.pushButton_7.clicked.connect(self.digit_pressed)
        self.pushButton_8.clicked.connect(self.digit_pressed)
        self.pushButton_9.clicked.connect(self.digit_pressed)
        self.pushButton_hexA.clicked.connect(self.hex_pressed)
        self.pushButton_hexB.clicked.connect(self.hex_pressed)
        self.pushButton_hexC.clicked.connect(self.hex_pressed)
        self.pushButton_hexD.clicked.connect(self.hex_pressed)
        self.pushButton_hexE.clicked.connect(self.hex_pressed)
        self.pushButton_hexF.clicked.connect(self.hex_pressed)

        # Special buttons
        self.pushButton_decimal.clicked.connect(self.dot_pressed)
        self.pushButton_plusMinus.clicked.connect(self.unary_operation_pressed)
        self.pushButton_percent.clicked.connect(self.unary_operation_pressed)
        self.pushButton_equals.clicked.connect(self.equals_pressed)
        self.pushButton_clear.clicked.connect(self.clear)

        # Binary operations
        self.pushButton_add.clicked.connect(self.binary_operation_pressed)
        self.pushButton_add.setCheckable(True)
        self.pushButton_substract.clicked.connect(self.binary_operation_pressed)
        self.pushButton_substract.setCheckable(True)
        self.pushButton_multiply.clicked.connect(self.binary_operation_pressed)
        self.pushButton_multiply.setCheckable(True)
        self.pushButton_divide.clicked.connect(self.binary_operation_pressed)
        self.pushButton_divide.setCheckable(True)

        # Trigonometric functions
        self.pushButton_sin.clicked.connect(self.trigonometric_pressed)
        self.pushButton_sin.setCheckable(True)
        self.pushButton_cos.clicked.connect(self.trigonometric_pressed)
        self.pushButton_cos.setCheckable(True)
        self.pushButton_tg.clicked.connect(self.trigonometric_pressed)
        self.pushButton_tg.setCheckable(True)
        self.pushButton_ctg.clicked.connect(self.trigonometric_pressed)
        self.pushButton_ctg.setCheckable(True)

        # Systems(DEC, BIN, HEX)
        self.radioButton_DEC.clicked.connect(self.check_system)
        self.radioButton_BIN.clicked.connect(self.check_system)
        self.radioButton_HEX.clicked.connect(self.check_system)
        self.pushButton_toDEC.clicked.connect(self.convert_to_system)
        self.pushButton_toDEC.setCheckable(True)
        self.pushButton_toDEC.setDisabled(True)
        self.pushButton_toBIN.clicked.connect(self.convert_to_system)
        self.pushButton_toBIN.setCheckable(True)
        self.pushButton_toHEX.clicked.connect(self.convert_to_system)
        self.pushButton_toHEX.setCheckable(True)

    def digit_pressed(self):
        button = self.sender()

        if ((self.pushButton_add.isChecked() or
             self.pushButton_substract.isChecked() or
             self.pushButton_multiply.isChecked() or
             self.pushButton_divide.isChecked()) and
                (not self.userIsTyping)):

            newLabel = format(float(button.text()), '.12g')
            self.userIsTyping = True
        else:
            if ('.' in self.label.text()) and (button.text() == '0'):
                newLabel = format(self.label.text() + button.text(), '.12')
            else:
                if any([x in self.label.text() for x in ["A", "B", "C", "D", "E", "F"]]):
                    newLabel = self.label.text() + button.text()
                else:
                    newLabel = format(float(self.label.text() + button.text()), '.12g')

        self.label.setText(str(newLabel))

    def hex_pressed(self):
        button = self.sender()

        self.userIsTyping = True

        if not self.userIsTyping or self.label.text() == '0':
            newLabel = button.text()
        else:
            if any([x in self.label.text() for x in ["A", "B", "C", "D", "E", "F"]]):
                newLabel = self.label.text() + button.text()
            else:
                newLabel = self.label.text() + button.text()

        self.userIsTyping = False
        self.label.setText(str(newLabel))

    def dot_pressed(self):
        if '.' in self.label.text():
            pass
        else:
            self.label.setText(self.label.text() + '.')

    def unary_operation_pressed(self):
        button = self.sender()

        labelNumber = float(self.label.text())

        if button.text() == '+/-':
            labelNumber = labelNumber * -1
        else:  # button == '%'
            labelNumber = labelNumber * 0.01

        newlabel = format(labelNumber, '.12g')
        self.label.setText(newlabel)

    def binary_operation_pressed(self):
        button = self.sender()
        self.firstNumber = float(self.label.text())
        button.setChecked(True)

    def equals_pressed(self):
        secondNumber = float(self.label.text())

        if self.pushButton_add.isChecked():
            labelNumber = self.firstNumber + secondNumber
            newlabel = format(labelNumber, '.12g')
            self.label.setText(newlabel)
            self.pushButton_add.setChecked(False)
        elif self.pushButton_substract.isChecked():
            labelNumber = self.firstNumber - secondNumber
            newlabel = format(labelNumber, '.12g')
            self.label.setText(newlabel)
            self.pushButton_substract.setChecked(False)
        elif self.pushButton_multiply.isChecked():
            labelNumber = self.firstNumber * secondNumber
            newlabel = format(labelNumber, '.12g')
            self.label.setText(newlabel)
            self.pushButton_multiply.setChecked(False)
        elif self.pushButton_divide.isChecked():
            if secondNumber == 0:
                self.label.setText('Error. Division 0!')
            else:
                labelNumber = self.firstNumber / secondNumber
                newlabel = format(labelNumber, '.12g')
                self.label.setText(newlabel)
                self.pushButton_divide.setChecked(False)

        self.userIsTyping = False

    def clear(self):
        self.pushButton_add.setChecked(False)
        self.pushButton_substract.setChecked(False)
        self.pushButton_multiply.setChecked(False)
        self.pushButton_divide.setChecked(False)
        self.userIsTyping = False
        self.label.setText('0')

    def check_system(self):
        radio_button = self.sender().text()

        if radio_button == 'DEC':
            self.disable_for_dec()

        elif radio_button == 'BIN':
            self.disable_for_bin()

        elif radio_button == 'HEX':
            self.disable_for_hex()

    def convert_to_system(self):
        to_convert = self.label.text()

        if self.radioButton_BIN.isChecked():

            if self.pushButton_toDEC.isChecked():  # BIN to DEC
                self.pushButton_toDEC.setChecked(False)
                converted_number = 0

                for char in to_convert:
                    converted_number *= 2
                    if char == '1':
                        converted_number += 1
                self.radioButton_DEC.click()
                self.label.setText(format(converted_number, '.12g'))

            elif self.pushButton_toHEX.isChecked():  # BIN to HEX

                converted_number = '%0*X' % ((len(to_convert) + 3) // 4, int(to_convert, 2))

                self.pushButton_toHEX.setChecked(False)
                self.radioButton_HEX.click()
                self.label.setText(str(converted_number))

        elif self.radioButton_HEX.isChecked():

            if self.pushButton_toDEC.isChecked():  # HEX to DEC

                converted_number = int(to_convert, 16)

                self.pushButton_toDEC.setChecked(False)
                self.radioButton_DEC.click()
                self.label.setText(str(converted_number))

            elif self.pushButton_toBIN.isChecked():  # HEX to BIN

                converted_number = "{0:8b}".format(int(to_convert, 16))

                self.pushButton_toBIN.setChecked(False)
                self.radioButton_BIN.click()
                self.label.setText(str(converted_number))

        elif self.radioButton_DEC.isChecked():

            if self.pushButton_toHEX.isChecked():  # DEC to HEX
                converted_number = ''

                h = [str(i) for i in range(10)] \
                    + ["A", "B", "C", "D", "E", "F"]

                while int(to_convert):
                    converted_number += h[int(to_convert) % 16]
                    to_convert = int(to_convert) // 16

                self.pushButton_toHEX.setChecked(False)
                self.radioButton_HEX.click()
                self.label.setText(str(converted_number[::-1]))

            elif self.pushButton_toBIN.isChecked():  # DEC to BIN
                converted_number = ''

                while to_convert:
                    if int(to_convert) % 2 == 0:
                        converted_number += '0'
                    else:
                        converted_number += '1'

                    to_convert = int(to_convert) // 2

                self.pushButton_toBIN.setChecked(False)
                self.radioButton_BIN.click()
                self.label.setText(str(''.join(reversed(converted_number))))

    def trigonometric_pressed(self):
        self.firstNumber = float(self.label.text())
        button = self.sender()
        button.setChecked(True)

        if self.pushButton_sin.isChecked():
            self.pushButton_sin.setChecked(False)
            self.label.setText(str(math.sin(self.firstNumber)))
        elif self.pushButton_cos.isChecked():
            self.pushButton_cos.setChecked(False)
            self.label.setText(str(math.cos(self.firstNumber)))
        elif self.pushButton_tg.isChecked():
            self.pushButton_tg.setChecked(False)
            self.label.setText(str(math.tan(self.firstNumber)))
        elif self.pushButton_ctg.isChecked():
            self.pushButton_ctg.setChecked(False)
            self.label.setText(str(math.atan(self.firstNumber)))

    def disable_for_bin(self):
        self.pushButton_toBIN.setDisabled(True)
        self.pushButton_toDEC.setDisabled(False)
        self.pushButton_toHEX.setDisabled(False)
        self.pushButton_2.setDisabled(True)
        self.pushButton_3.setDisabled(True)
        self.pushButton_4.setDisabled(True)
        self.pushButton_5.setDisabled(True)
        self.pushButton_6.setDisabled(True)
        self.pushButton_7.setDisabled(True)
        self.pushButton_8.setDisabled(True)
        self.pushButton_9.setDisabled(True)
        self.pushButton_decimal.setDisabled(True)
        self.pushButton_plusMinus.setDisabled(True)
        self.pushButton_percent.setDisabled(True)
        self.pushButton_equals.setDisabled(True)
        self.pushButton_add.setDisabled(True)
        self.pushButton_substract.setDisabled(True)
        self.pushButton_divide.setDisabled(True)
        self.pushButton_multiply.setDisabled(True)
        self.pushButton_divide.setDisabled(True)
        self.pushButton_sin.setDisabled(True)
        self.pushButton_cos.setDisabled(True)
        self.pushButton_tg.setDisabled(True)
        self.pushButton_ctg.setDisabled(True)
        self.pushButton_hexA.setDisabled(True)
        self.pushButton_hexB.setDisabled(True)
        self.pushButton_hexC.setDisabled(True)
        self.pushButton_hexD.setDisabled(True)
        self.pushButton_hexE.setDisabled(True)
        self.pushButton_hexF.setDisabled(True)

    def disable_for_dec(self):
        self.pushButton_toDEC.setDisabled(True)
        self.pushButton_toBIN.setDisabled(False)
        self.pushButton_toHEX.setDisabled(False)
        self.pushButton_2.setDisabled(False)
        self.pushButton_3.setDisabled(False)
        self.pushButton_4.setDisabled(False)
        self.pushButton_5.setDisabled(False)
        self.pushButton_6.setDisabled(False)
        self.pushButton_7.setDisabled(False)
        self.pushButton_8.setDisabled(False)
        self.pushButton_9.setDisabled(False)
        self.pushButton_decimal.setDisabled(False)
        self.pushButton_plusMinus.setDisabled(False)
        self.pushButton_percent.setDisabled(False)
        self.pushButton_equals.setDisabled(False)
        self.pushButton_add.setDisabled(False)
        self.pushButton_substract.setDisabled(False)
        self.pushButton_divide.setDisabled(False)
        self.pushButton_multiply.setDisabled(False)
        self.pushButton_divide.setDisabled(False)
        self.pushButton_sin.setDisabled(False)
        self.pushButton_cos.setDisabled(False)
        self.pushButton_tg.setDisabled(False)
        self.pushButton_ctg.setDisabled(False)
        self.pushButton_hexA.setDisabled(True)
        self.pushButton_hexB.setDisabled(True)
        self.pushButton_hexC.setDisabled(True)
        self.pushButton_hexD.setDisabled(True)
        self.pushButton_hexE.setDisabled(True)
        self.pushButton_hexF.setDisabled(True)

    def disable_for_hex(self):
        self.pushButton_toDEC.setDisabled(False)
        self.pushButton_toBIN.setDisabled(False)
        self.pushButton_toHEX.setDisabled(True)
        self.pushButton_2.setDisabled(False)
        self.pushButton_3.setDisabled(False)
        self.pushButton_4.setDisabled(False)
        self.pushButton_5.setDisabled(False)
        self.pushButton_6.setDisabled(False)
        self.pushButton_7.setDisabled(False)
        self.pushButton_8.setDisabled(False)
        self.pushButton_9.setDisabled(False)
        self.pushButton_decimal.setDisabled(True)
        self.pushButton_plusMinus.setDisabled(True)
        self.pushButton_percent.setDisabled(True)
        self.pushButton_equals.setDisabled(True)
        self.pushButton_add.setDisabled(True)
        self.pushButton_substract.setDisabled(True)
        self.pushButton_divide.setDisabled(True)
        self.pushButton_multiply.setDisabled(True)
        self.pushButton_divide.setDisabled(True)
        self.pushButton_sin.setDisabled(True)
        self.pushButton_cos.setDisabled(True)
        self.pushButton_tg.setDisabled(True)
        self.pushButton_ctg.setDisabled(True)
        self.pushButton_hexA.setDisabled(False)
        self.pushButton_hexB.setDisabled(False)
        self.pushButton_hexC.setDisabled(False)
        self.pushButton_hexD.setDisabled(False)
        self.pushButton_hexE.setDisabled(False)
        self.pushButton_hexF.setDisabled(False)
