#!/usr/bin/env python

import foo

from sys import argv
from PySide import QtGui
from PySide.QtCore import SIGNAL, SLOT
 
class Test(QtGui.QWidget):
 
    def __init__(self):
      super(Test, self).__init__()
      self.layout = QtGui.QVBoxLayout(self)

      self.btn = QtGui.QPushButton('Test', self)
      self.layout.addWidget(self.btn)

      self.txt = QtGui.QLineEdit(self)
      self.layout.addWidget(self.txt)

      self.lst = foo.MainW(self)
      self.layout.addWidget(self.lst)

      self.btn.clicked.connect(self.onBtnClick)
      self.connect(self,      SIGNAL('addTest(str)'), self.lst,  SLOT('addLine(str)'))
 
    def onBtnClick(self):
      text = 'Test (%s)' % self.txt.text()
      print('Add "%s" to the list!' % text)
      self.emit(SIGNAL('addText'), text)
 
if __name__ == '__main__':
    app = QtGui.QApplication(argv)
    test = Test()
    test.show()
    app.exec_()
