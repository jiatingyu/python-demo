# 测试代码
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QMainWindow, QMenu, QTextEdit, \
    QLabel, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit
from PyQt6.QtGui import QFont,QAction,QIcon

# 全局 tooltip
QToolTip.setFont(QFont('Arial', 10))

class MyButton(QPushButton):
    def __init__(self, parent=None, title="关闭按钮", fn=None):
        super().__init__(title, parent)
        # 设置按钮，并指定归属那个显示控件
        self.setToolTip('这是一个关闭按钮，点击即可关闭窗口')
        # 绑定一个事件
        # button.clicked.connect(QApplication.instance().quit)
        if fn is not None:
            self.clicked.connect(fn)
        self.move(50, 50)

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.startUI()

    def startUI(self):
        # title
        self.setWindowTitle('PyQt6 demo')
        self.resize(400, 400)
        self.setToolTip('全局窗口')
        # 相对屏幕居中
        self.screen().availableGeometry().center()
        MyButton(self, '关闭按钮，点击关闭', self.quit)
        # 固定的位置
        # self.move(400, 400)
        # self.setGeometry(300,300,300,300)
        self.show()

    # 自定退出函数
    def quit(self):
        print('quit 执行')
        # 添加一个推出警告
        reply = QMessageBox.question(self, "警告", "你确认要推出", QMessageBox.StandardButton.Yes |
                                     QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            QApplication.instance().quit()
    # 窗体自带的关闭事件
    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                    "Are you sure to quit?", QMessageBox.StandardButton.Yes |
                    QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:

            event.accept()
        else:

            event.ignore()

class MenuBar(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        # 设置左下角状态栏
        self.statusBar()
        self.statusBar().showMessage('程序准备好了')
        # 这里创建了一个文本编辑器组件，并把它设置到 QMainWindow 的中央。居中布局组件撑满了所有空白的部分。
        textEdit = QTextEdit("这是一个文本输入框")
        self.setCentralWidget(textEdit)

        # 设置工具栏
        self.toolbar = self.addToolBar('退出')

        exitAct = QAction(QIcon('logo.png'), '&退出', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出应用')
        exitAct.triggered.connect(QApplication.instance().quit)

        self.toolbar.addAction(exitAct)
        # 设置菜单栏
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&操作')
        fileMenu.addAction(exitAct)

        childMenu = QMenu("子菜单",self)
        childAction= QAction("子事件",self)
        childMenu.addAction(childAction)

        fileMenu.addMenu(childMenu)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('主窗口示例')
        self.show()

    # 添加右键菜单
    def contextMenuEvent(self, event):
        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        openAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec(self.mapToGlobal(event.pos()))

        if action == quitAct:
            QApplication.instance().quit()

class Position(QWidget):

    def __init__(self):
        super().__init__()
        # 绝对的定位
        # self.absoluteLayout()
        # 水平垂直定位，不能跟 网格同时存在
        # self.HVLayout()
        # 网格定位
        # self.gridLayout()
        #
        # self.formLayout()
    def absoluteLayout(self):
        label1 = QLabel(self)
        label1.setText('姓名：')
        label1.move(40,40)

        label2 = QLabel(self)
        label2.setText('年龄：')
        label2.move(80, 80)

        self.resize(400, 400)
        self.move(300, 300)
        self.show()

    def HVLayout(self):
        btnOK = QPushButton(self)
        btnCancel = QPushButton(self)
        btnOK.setText('确认')
        btnCancel.setText('取消')

        Hlayout = QHBoxLayout(self)
        Hlayout.addStretch(1)
        Hlayout.addWidget(btnOK)
        Hlayout.addWidget(btnCancel)
        Vlayout = QVBoxLayout()
        Vlayout.addStretch(1)
        Vlayout.addLayout(Hlayout)
        self.setGeometry(300,300, 350, 250)
        self.setLayout(Vlayout)


    def gridLayout(self):
        grid = QGridLayout()
        self.setLayout(grid)
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue

            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.setGeometry(300,300, 350, 250)
        self.show()

    def formLayout(self):
        title = QLabel("标题")
        desc = QLabel('描述')
        content = QLabel('内容')


        titleEdit = QLineEdit("第一个篇文章")
        descEdit = QLineEdit('入坑指南')
        contentEdit = QTextEdit('内容:从入门到放弃')

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(title,1,0)
        grid.addWidget(titleEdit,1,1,1,8)

        grid.addWidget(desc, 2, 0)
        grid.addWidget(descEdit, 2, 1,1,8)

        grid.addWidget(content, 3, 0)
        grid.addWidget(contentEdit, 3, 1,2,8)

        grid.addWidget(QPushButton('提交'),6,5)
        grid.addWidget(QPushButton('重置'),6,7)

        self.setLayout(grid)
        self.setGeometry(300,300,450,350)
        self.show()


# 启动
def main():
    app = QApplication(sys.argv)
    # w = MyWidget()
    # m = MenuBar()
    d= Position()
    sys.exit(app.exec())



if __name__ == '__main__':
    main()





# Ctrl + Shift + Alt + j  选中多个相同变量
# alt + 鼠标  多光标
# alt + j  依次选择 相同变量
# ctrl双击 + ctrl(按住)+上下键.可以在同一列增加光标.
# ctrl + c 复制整行
# ctrl + shift + 箭头 : 上下移动

