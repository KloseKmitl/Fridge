import PyQt5.QtWidgets as qtw

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
        self.result_field = qtw.QLineEdit()
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
        btn_clear = qtw.QPushButton('CE', clicked = self.clear_result)
        btn_float = qtw.QPushButton('.', clicked = lambda:self.num_press('.'))

        #Adding buttons to layout
        container.layout().addWidget(self.result_field,0,0,1,4)
        container.layout().addWidget(btn_7,1,0,1,1)
        container.layout().addWidget(btn_8,1,1,1,1)
        container.layout().addWidget(btn_9,1,2,1,1)
        container.layout().addWidget(btn_divd,1,3,1,1)
        container.layout().addWidget(btn_4,2,0,1,1)
        container.layout().addWidget(btn_5,2,1,1,1)
        container.layout().addWidget(btn_6,2,2,1,1)
        container.layout().addWidget(btn_mult,2,3,1,1)
        container.layout().addWidget(btn_1,3,0,1,1)
        container.layout().addWidget(btn_2,3,1,1,1)
        container.layout().addWidget(btn_3,3,2,1,1)
        container.layout().addWidget(btn_mins,3,3,1,1)
        container.layout().addWidget(btn_result,4,0,1,1)
        container.layout().addWidget(btn_0,4,1,1,1)
        container.layout().addWidget(btn_float,4,2,1,1)
        container.layout().addWidget(btn_plus,4,3,1,1)
        container.layout().addWidget(btn_clear,5,0,1,2)
        container.layout().addWidget(btn_clearall,5,2,1,2)
        self.layout().addWidget(container)

    def num_press(self, key_number):
        self.temp_nums.append(key_number)
        temp_string = ''.join(self.temp_nums)
        if self.fin_nums:
            self.result_field.setText(''.join(self.fin_nums) + temp_string)
        else:
            self.result_field.setText(temp_string)

    def func_press(self, operator):
        temp_string = ''.join(self.temp_nums)
        self.fin_nums.append(temp_string)
        self.fin_nums.append(operator)
        self.temp_nums = []
        self.result_field.setText(''.join(self.fin_nums))

    def func_result(self):
        fin_string = ''.join(self.fin_nums) + ''.join(self.temp_nums)
        result_string = eval(fin_string)
        fin_string += '='
        fin_string += str(result_string)
        self.result_field.setText(fin_string)

    def clear_calc(self):
        self.result_field.clear()
        self.temp_nums = []
        self.fin_nums = []

    def clear_result(self):
        fin_string = ''.join(self.fin_nums) + ''.join(self.temp_nums)
        result_string = eval(fin_string)
        self.result_field.setText(fin_string)

app = qtw.QApplication([])
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create('Fusion'))
app.exec_()