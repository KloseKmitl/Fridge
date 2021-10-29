import PyQt5.QtWidgets as qtw
from PyQt5 import QtCore

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Simple Calculator')
        self.setLayout(qtw.QVBoxLayout())
        self.keypad()
        self.temp_nums = []
        self.fin_nums = []
        self.show()
        
    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        #Buttons
        self.outputLabel_1 = qtw.QLabel()
        self.outputLabel_1.setAlignment(QtCore.Qt.AlignRight)
        self.outputLabel_1.setStyleSheet("color: black;")
        self.outputLabel_1.setText('0')
        self.outputLabel_2 = qtw.QLabel()
        self.outputLabel_2.setAlignment(QtCore.Qt.AlignRight)
        self.outputLabel_2.setStyleSheet("color: grey;")
        btn_9 = qtw.QPushButton('9', clicked = lambda:self.num_press('9'))
        btn_8 = qtw.QPushButton('8', clicked = lambda:self.num_press('8'))
        btn_7 = qtw.QPushButton('7', clicked = lambda:self.num_press('7'))
        btn_6 = qtw.QPushButton('6', clicked = lambda:self.num_press('6'))
        btn_5 = qtw.QPushButton('5', clicked = lambda:self.num_press('5'))
        btn_4 = qtw.QPushButton('4', clicked = lambda:self.num_press('4'))
        btn_3 = qtw.QPushButton('3', clicked = lambda:self.num_press('3'))
        btn_2 = qtw.QPushButton('2', clicked = lambda:self.num_press('2'))
        btn_1 = qtw.QPushButton('1', clicked = lambda:self.num_press('1'))
        btn_0 = qtw.QPushButton('0', clicked = lambda:self.num_press('0'))
        btn_plus = qtw.QPushButton('+', clicked = lambda:self.func_press('+'))
        btn_mins = qtw.QPushButton('-', clicked = lambda:self.func_press('-'))
        btn_mult = qtw.QPushButton('*', clicked = lambda:self.func_press('*'))
        btn_divd = qtw.QPushButton('/', clicked = lambda:self.func_press('/'))
        btn_result = qtw.QPushButton('=', clicked = self.func_result)
        btn_clearall = qtw.QPushButton('C', clicked = self.clear_calc)
        btn_float = qtw.QPushButton('.', clicked = lambda:self.num_press('.'))
        btn_del = qtw.QPushButton('DEL', clicked = self.delete)
        btn_9.setStyleSheet("background-color: #007060;")
        btn_8.setStyleSheet("background-color: #007060;")
        btn_7.setStyleSheet("background-color: #007060;")
        btn_6.setStyleSheet("background-color: #007060;")
        btn_5.setStyleSheet("background-color: #007060;")
        btn_4.setStyleSheet("background-color: #007060;")
        btn_3.setStyleSheet("background-color: #007060;")
        btn_2.setStyleSheet("background-color: #007060;")
        btn_1.setStyleSheet("background-color: #007060;")
        btn_0.setStyleSheet("background-color: #007060;")
        btn_result.setStyleSheet("background-color: #50C878;")
        btn_float.setStyleSheet("background-color: #50C878;")
        btn_clearall.setStyleSheet("background-color: #F50407;")
        btn_plus.setStyleSheet("background-color: #50C878;")
        btn_mins.setStyleSheet("background-color: #50C878;")
        btn_mult.setStyleSheet("background-color: #50C878;")
        btn_divd.setStyleSheet("background-color: #50C878;")
        btn_del.setStyleSheet("background-color: #F50407;")

        #Adding buttons to layout
        container.layout().addWidget(self.outputLabel_2,0,0,1,4)
        container.layout().addWidget(self.outputLabel_1,1,0,1,4)
        container.layout().addWidget(btn_7,2,0,1,1)
        container.layout().addWidget(btn_8,2,1,1,1)
        container.layout().addWidget(btn_9,2,2,1,1)
        container.layout().addWidget(btn_divd,2,3,1,1)
        container.layout().addWidget(btn_4,3,0,1,1)
        container.layout().addWidget(btn_5,3,1,1,1)
        container.layout().addWidget(btn_6,3,2,1,1)
        container.layout().addWidget(btn_mult,3,3,1,1)
        container.layout().addWidget(btn_1,4,0,1,1)
        container.layout().addWidget(btn_2,4,1,1,1)
        container.layout().addWidget(btn_3,4,2,1,1)
        container.layout().addWidget(btn_mins,4,3,1,1)
        container.layout().addWidget(btn_result,5,0,1,1)
        container.layout().addWidget(btn_0,5,1,1,1)
        container.layout().addWidget(btn_float,5,2,1,1)
        container.layout().addWidget(btn_plus,5,3,1,1)
        container.layout().addWidget(btn_clearall,6,0,1,2)
        container.layout().addWidget(btn_del,6,2,1,2)
        self.layout().addWidget(container)

    def num_press(self, key_number):
        self.temp_nums.append(key_number)
        temp_string = ''.join(self.temp_nums)
        self.outputLabel_1.setText(temp_string)

    def func_press(self, operator):
        temp_string = ''.join(self.temp_nums)
        self.fin_nums.append(temp_string)
        self.fin_nums.append(operator)
        self.outputLabel_2.setText(''.join(self.fin_nums))
        self.temp_nums = []
        self.outputLabel_1.clear()

    def func_result(self):
        fin_string = ''.join(self.fin_nums) + ''.join(self.temp_nums)
        self.outputLabel_2.setText(fin_string)
        result_string = eval(fin_string)
        self.outputLabel_1.setText(str(result_string))
        self.fin_nums = [str(result_string)]
        self.temp_nums = []

    def clear_calc(self):
        self.outputLabel_1.setText('0')
        self.outputLabel_2.clear()
        self.temp_nums = []
        self.fin_nums = []

    def delete(self):
        if self.temp_nums == []:
            pass
        else:
            self.temp_nums.pop()
            self.outputLabel_1.setText(''.join(self.temp_nums))
            if self.temp_nums == []:
                self.outputLabel_1.setText('0')
        
app = qtw.QApplication([])
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create('Fusion'))
app.exec_()