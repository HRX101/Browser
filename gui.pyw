import sys
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import random 
def rand_color():
    col=["red","blue","black","orange","white","violet","pink","#ADD8E6","#00008B"]
    s=random.randint(0,8)
    return col[s]
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.setWindowIcon(QIcon("gui.ico"))
        self.browser.setUrl(QUrl('http://google.com'))
        self.browser.setStyleSheet("border:3px solid black;")
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)
        navbar.setStyleSheet("color:yellow;font:bold 14px;")
        back_btn = QAction('Back', self)
        back_btn.setIcon(QIcon("back.png"))
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.setIcon(QIcon("forward.png"))
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.setIcon(QIcon("reload.png"))
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Qutoes', self)
        home_btn.setIcon(QIcon("qutoes.png"))
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        starting_part=QAction("Start",self)
        starting_part.setIcon(QIcon("start.png"))
        starting_part.triggered.connect(self.navigate_start)
        navbar.addAction(starting_part)
       
        colors=QAction("change_bgcolor",self)
        colors.setIcon(QIcon("color_change.png"))
        colors.triggered.connect(lambda:self.change_color(rand_color()))
        navbar.addAction(colors)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://hrithikpaul-qutoes.herokuapp.com/'))
    def navigate_start(self):
        self.browser.setUrl(QUrl('https://google.com/'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())
    def change_color(self,color):
        self.setStyleSheet(f"background-color:{color};")



app = QApplication(sys.argv)
QApplication.setApplicationName('GUI browser')
window = MainWindow()
app.exec_() 