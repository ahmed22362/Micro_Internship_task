import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget
from random import choice

window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.label = QLabel()
        self.input = QLineEdit()

        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def the_button_was_clicked(self):
        print("Clicked!")
        new_windows_title = choice(window_titles)
        print("setting title: %s" %new_windows_title)
        self.setWindowTitle(new_windows_title) 

    def the_window_title_changed(self,window_title):
        print("window title changed %s" %window_title)
        if window_title == "Something went wrong":
            self.button.setText("something went wrong")
            self.button.setDisabled(True)

app = QApplication(sys.argv)

window =MainWindow()
window.show()

app.exec()
