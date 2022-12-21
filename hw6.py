#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 00:00:00 2022

@author: nick lewis
"""


import sys

#%% Question 1
# https://doc.qt.io/qt-5/qcolordialog.html
# https://doc.qt.io/qt-5/qcolordialog.html#signals
# https://doc.qt.io/qt-5/qcolordialog.html#colorSelected
# since QColorDialog inherits from QWidget, it has a show method

from PyQt5.QtWidgets import QApplication, QWidget, QColorDialog
from PyQt5.QtGui import QPainter, QColor
from random import randint

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.q = QColorDialog(self.squareColor, self)
        self.q.colorSelected.connect(self.colorChange)

    def initUI(self):
        self.setGeometry(0, 0, 600, 400)
        w = self.width()
        h = self.height()
        #Inst vars x,y,l store the top left coordinate and length of the square
        self.x = randint(0, w-51)
        self.y = randint(0, h-51)
        self.l = 50
        self.squareColor = QColor(255, 0, 0)
        self.show()
        
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.fillRect(0, 0, self.width(), self.height(), QColor(255,255,255))
        self.drawSquare(qp)
        qp.end()

    def drawSquare(self, qp):
        qp.setPen(self.squareColor)
        qp.setBrush(self.squareColor)
        qp.drawRect(self.x, self.y, self.l, self.l)
        
    def mousePressEvent(self, e):
        self.a = e.x() - self.x
        self.b = e.y() - self.y
    
    def mouseMoveEvent(self, e):
        if 0 <= self.a <= self.l and 0 <= self.b <= self.l:
            self.x = e.x() - self.a
            self.y = e.y() - self.b
            self.update()
            
    def mouseDoubleClickEvent(self, e):
        if 0 <= self.a <= self.l and 0 <= self.b <= self.l:
            self.q.show()
       
    def colorChange(self, q):
        self.squareColor = self.q.selectedColor()
        self.update()
        
def main():
    app = QApplication([])
    w = MyWidget()
    app.exec_()

if len(sys.argv) == 2 and sys.argv[1] == '1':
    main()


#%% Question 2
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QTimer, QThread

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initTimer()

    def initUI(self):
        self.setGeometry(0, 0, 600, 400)
        #Inst vars x,y,d store the top left coordinate and diam of the circle
        self.x = 0
        self.y = 0
        self.d = 30
        #X,Y velocity of the ball
        self.vx = 1
        self.vy = 1
        self.show()
    
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.fillRect(0, 0, self.width(), self.height(), QColor(255,255,255))
        self.drawCircle(qp)
        qp.end()

    def drawCircle(self, qp):
        qp.setPen(QColor(255, 0, 0))
        qp.setBrush(QColor(255, 0, 0))
        qp.drawEllipse(self.x, self.y, self.d, self.d)
        
    def animate(self):
        self.x += self.vx
        self.y += self.vy
        self.checkCollision()
        self.update()
    
    def initTimer(self):
        self.t = QTimer()
        self.t.timeout.connect(self.animate)
        self.t.start(25)
    
    def checkCollision(self):
        if self.x <= 0:
            self.vx = 1
        if self.x + 30 >= self.width():
            self.vx = -1
        if self.y <= 0:
            self.vy = 1
        if self.y + 30 >= self.height():
            self.vy = -1
        
def main():
    app = QApplication([])
    w = MyWidget()
    app.exec_()

if len(sys.argv) == 2 and sys.argv[1] == '2':
    main()
