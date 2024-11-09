import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
          
    def set_size_of_window(self):
        self.setGeometry(500, 500, 250, 250)
            
    def create_title(self):
        self.setWindowTitle('information') 
            
    def create_button(self):
        self.btn = QPushButton(self)
        self.btn.setText('Enter')
        self.btn.move(95, 170)
          
    def create_label(self):
        self.lbl_1 = QLabel(self)
        self.lbl_1.setText('Name : ')
        self.lbl_1.move(10, 10)
        self.lbl_2 = QLabel(self)
        self.lbl_2.setText('Last name : ')
        self.lbl_2.move(10, 50)
        self.lbl_3 = QLabel(self)
        self.lbl_3.setText('Student number : ')
        self.lbl_3.move(10, 90)
        self.lbl_4 = QLabel(self)
        self.lbl_4.setText('Birth year : ')
        self.lbl_4.move(10, 130)
        self.lbl_5 = QLabel(self)
        self.lbl_5.setText('please enter your information in the boxes.')
        self.lbl_5.move(0, 210)
        
    def create_line_edit(self):
        self.line_edit_1 = QLineEdit(self)
        self.line_edit_1.move(60, 10)
        self.line_edit_2 = QLineEdit(self)
        self.line_edit_2.move(90, 50)
        self.line_edit_3 = QLineEdit(self)
        self.line_edit_3.move(120, 90)
        self.line_edit_4 = QLineEdit(self)
        self.line_edit_4.move(90 , 130)
        
    def clicked(self):
        self.lbl_5.setText(f'{self.line_edit_1.text()}-{self.line_edit_2.text()}-{self.line_edit_3.text()}-{self.line_edit_4.text()}')
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.set_size_of_window()
    window.create_title()
    window.create_button()
    window.create_label()
    window.create_line_edit()
    window.btn.clicked.connect(window.clicked)
    window.show()
    sys.exit(app.exec()) 
    