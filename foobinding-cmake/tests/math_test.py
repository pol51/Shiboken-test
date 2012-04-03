#!/usr/bin/env python

import foo

from sys import argv
from PySide import QtGui
from PySide.QtCore import SIGNAL, SLOT
 
class Test(QtGui.QWidget):
 
    def onClick(self):
      self.mainW.addLine('Test 0')
 
    def test(self):
        '''Test case for Math class from foo module.'''
        
        self.mainW = foo.MainW()
        self.mainW.show()
        self.b = QtGui.QPushButton('Test')
        self.b.connect(self.b, SIGNAL('clicked()'), self, SLOT('onClick()'))
        self.b.show()
 
if __name__ == '__main__':
    app = QtGui.QApplication(argv)
    test = Test()
    test.test()
    app.exec_()
