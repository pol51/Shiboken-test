#!/usr/bin/env python

import foo

from sys import argv
from PySide.QtCore import *
from PySide.QtGui  import *
 
class Test(QWidget):
 
  addText = Signal(str)

  def __init__(self):
    super(Test, self).__init__()
    self.setWindowTitle('Test widget')
    self.layout = QVBoxLayout(self)

    self.btn = QPushButton('Add value', self)
    self.layout.addWidget(self.btn)

    self.txt = QLineEdit(self)
    self.layout.addWidget(self.txt)

    self.lst = foo.MainW(self)
    self.layout.addWidget(self.lst)

    self.btn.clicked.connect(self.onBtnClick)
    self.addText.connect(self.lst.addLine)
    self.addText.connect(self.addLine)

  def onBtnClick(self):
    text = 'Test (%s)' % self.txt.text()
    print('Add "%s" to the list!' % text)
    self.addText.emit(text)
    
  @Slot(str)
  def addLine(self, text):
    print('Received: "%s"' % text)


if __name__ == '__main__':
  app = QApplication(argv)
  test = Test()
  test.show()
  exit(app.exec_())
