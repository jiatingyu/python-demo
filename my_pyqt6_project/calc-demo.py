import sys
from PyQt6.QtWidgets import (QWidget, QPushButton, QApplication, QMainWindow, QGridLayout, QLineEdit)
from PyQt6.QtGui import QFont

class mainWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.edit = QLineEdit("123")
        self.edit.setFont(QFont('Arial', 20))
        self.start()

    def add(self,*args):
        sender = self.sender()
        print('print',args)
        print('print',sender.text())

    def start(self):
        grid = QGridLayout(self)
        grid.setSpacing(10)


        self.setGeometry(300,300,400,300)
        grid.addWidget(self.edit, 0, 0,1,4)

        names = ['Cls', 'Bck', '', '',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i+1, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue

            button = QPushButton(name)
            button.setFont(QFont('Arial', 12))
            button.clicked.connect(lambda: self.on_button_click(name))

            grid.addWidget(button, *position)

        back = QPushButton("Bck")
        back.setFont(QFont('Arial', 12))
        back.clicked.connect(lambda: self.back())
        grid.addWidget(back,1,1)

        equal = QPushButton("=")
        equal.setFont(QFont('Arial', 12))
        equal.clicked.connect(lambda: self.calculate_result())
        grid.addWidget(equal, 5, 2)

        Cls = QPushButton("Cls")
        Cls.setFont(QFont('Arial', 12))
        Cls.clicked.connect(lambda: self.clear_screen())
        grid.addWidget(Cls, 1, 0)

    def calculate(self,expression):
        try:
            result = eval(expression)
            return str(result)
        except Exception as e:
            return "Error"

    # 按钮点击事件
    def on_button_click(self,*args):
        current_expression = self.edit.text()
        text = self.sender().text()
        print(current_expression , text)
        self.edit.setText( current_expression +text)



    # # 清除屏幕
    def clear_screen(self):
        self.edit.setText('')

    # 计算结果
    def calculate_result(self):
        current_expression = self.edit.text()
        result = self.calculate(current_expression)
        print(result)
        self.edit.setText(result)
   # 计算结果
    def back(self):
        current_expression = self.edit.text()
        result =current_expression[0:len(current_expression)-1]
        self.edit.setText(result)


class calc(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.statusBar().showMessage('计算器准备就绪')

        widget = mainWidget()
        self.setCentralWidget(widget)

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('PyQt6 制作计算器')
        self.show()


def main():

    app = QApplication(sys.argv)
    ex = calc()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()