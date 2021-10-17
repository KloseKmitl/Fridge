import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Simple Calculator')
        self.setLayout(qtw.QVBoxLayout())
        self.keypad()

        self.show()

    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        #Buttons
        self.result_field = qtw.QLineEdit()
        btn_9 = qtw.QPushButton('9')
        btn_8 = qtw.QPushButton('8')
        btn_7 = qtw.QPushButton('7')
        btn_6 = qtw.QPushButton('6')
        btn_5 = qtw.QPushButton('5')
        btn_4 = qtw.QPushButton('4')
        btn_3 = qtw.QPushButton('3')
        btn_2 = qtw.QPushButton('2')
        btn_1 = qtw.QPushButton('1')
        btn_0 = qtw.QPushButton('0')
        btn_plus = qtw.QPushButton('+')
        btn_mins = qtw.QPushButton('-')
        btn_mult = qtw.QPushButton('*')
        btn_divd = qtw.QPushButton('/')
        btn_result = qtw.QPushButton('=')
        btn_clearall = qtw.QPushButton('C')
        btn_clear = qtw.QPushButton('CE')
        btn_float = qtw.QPushButton('.')

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
        
app = qtw.QApplication([])
mw = MainWindow()
app.exec_()