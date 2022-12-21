#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 00:00:00 2022

@author: sarahburnett
"""


#%% DOCUMENTATION
# There are two places to find documentation on PyQt.

# 1) https://www.riverbankcomputing.com/static/Docs/PyQt5/
#    This is for PyQt5.

# 2) https://doc.qt.io/qt-5/
#    This is more complete but it is for Qt5 in C++.
#    PyQt is a wrapper for the C++ version Qt.

# It is annoying that there is not very good documentation for PyQt.
# I'll try and tell you everything you need for this class here.
# But you should still be open to trying to look things up.


#%% OTHER RESOURCES
# As you make more progress, you may also find these tutorials useful:
# http://zetcode.com/gui/pyqt5/

# His tutorials cover lots of different material.
# The most important chapters for this class are:
# first programs, events and signals, painting.

# You may notice that I don't use
# QApplication(sys.argv) and sys.exit(app.exec_()).
# For larger applications, these may be important,
# but we don't need to be concerned about them right now.


#%% RUNNING FILES
# Because garbage collection is a confusing matter,
# running PyQt through Spyder can be annoying.

# I will run ALL of my PyQt files through the terminal.

# Rather than making many tutorial files,
# I will make ONE file which uses sys.argv
# to determine which part of it to run.
import sys


#%% THE MOST BASIC PyQt APPLICATION
from PyQt5.QtWidgets import QApplication, QWidget

def main():
    app = QApplication([])

    w = QWidget()
    w.show()

    app.exec_()

if len(sys.argv) == 2 and sys.argv[1] == '1':
    main()

# To run this code:
# . open up terminal (on Mac) or Anaconda Prompt (on Windows);
# . type 'cd [the directory where you have saved this file]';
# . then type 'python PyQt.py 1'.

# The construct that is always used is as follows:
# . instantiate a QApplication object;
# . make interesting objects like QWidgets;
# . exec_ute the QApplication object.
# However, we'll rarely think too much about this.
# It'll just be something we type every time.


#%% THE MOST IMPORTANT TEMPLATE
# We'll see that QWidgets are the most important object in PyQt.
# In order to make our QWidgets have interesting functionality,
# we'll write classes which inherit from QWidget and instantiate
# instances of these.

# If you want to build a GUI from scratch,
# this is the template you should be starting with...

from PyQt5.QtWidgets import QApplication, QWidget

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()  # initializes the QWidget
        self.initUI()

    def initUI(self):
        self.show()         # displays the QWidget

def main():
    app = QApplication([])
    w = MyWidget()
    app.exec_()

if len(sys.argv) == 2 and sys.argv[1] == '2':
    main()

# To run this code:
# . open up terminal (on Mac) or Anaconda Prompt (on Windows);
# . type 'cd [the directory where you have saved this file]';
# . then type 'python PyQt.py 2'.

# This does the same as the previous code,
# but now we have a framework in which to give our QWidget
# more functionality without editing our main function.


#%% SOME THINGS WE CAN DO
# Here I'll show some basic things we can do with QWidgets.
# They're not that amazing, but they get you into the mindset.

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MyWidget')
        self.initGeo()  # geometry
        self.initBtn()  # buttons
        self.initHov()  # hover behavior
        self.show()

    def initGeo(self):
        x, y = 200, 100
        w, h = 400, 150

        self.setGeometry(x, y, w, h)

        # The following quantities can differ...
        # https://doc.qt.io/qt-5/application-windows.html#window-geometry

        # print(self.x(), self.y(), self.width(), self.height())

        # geom = self.geometry()
        # print(geom.x(), geom.y(), geom.width(), geom.height())

        # fgeo = self.frameGeometry()
        # print(fgeo.x(), fgeo.y(), fgeo.width(), fgeo.height())

    def initBtn(self):
        # https://doc.qt.io/qt-5/qpushbutton.html

        # We're using the constructor that specifies
        # the text to display on the button and
        # the parent widget (our MyWidget).

        # https://doc.qt.io/qt-5/qpushbutton.html#QPushButton-1
        self.btn = QPushButton('Useless button', self)

        # These methods are fairly self explanatory.
        # They're inherited from QWidget.

        # https://doc.qt.io/qt-5/qwidget.html
        self.btn.move(50, 50)
        self.btn.resize(300, 50)

    def initHov(self):
        # Now when you hover over your widget
        # appropriate text will come up.
        self.setToolTip('This is a <b>QWidget</b>')
        self.btn.setToolTip('This is a <b>QPushButton</b>')

def main():
    app = QApplication([])
    w = MyWidget()
    app.exec_()

if len(sys.argv) == 2 and sys.argv[1] == '3':
    main()

# Notice that we could have written all of our code as part of
# MyWidget.__init__(self). Instead, we broke it up into pieces
# to make it easier to read.


#%% CONNECTING A BUTTON TO A METHOD
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.initGeo()
        self.initBtn()
        self.show()

    def initGeo(self):
        self.setGeometry(200, 100, 400, 150)

    def initBtn(self):
        # We'll have the button say how many times it has been clicked.
        self.i = 0
        self.btn = QPushButton('Clicked ' + str(self.i) + ' times', self)

        # We position it as before.
        self.btn.move(50, 50)
        self.btn.resize(300, 50)

        # This is the new part.
        # It is explained further below.
        self.btn.clicked.connect(self.btn_method)

    def btn_method(self):
        # This will print to the console.
        print('button clicked')

        # This will update the button's text.
        self.i += 1
        self.btn.setText('Clicked ' + str(self.i) + ' times')

def main():
    app = QApplication([])
    w = MyWidget()
    app.exec_()

if len(sys.argv) == 2 and sys.argv[1] == '4':
    main()

# How could we know QPushButton has this functionality?
# Well, for one, you'd hope it does! What else would you want
# a button to do but be clicked on and make things happen?
# So the question is: how do we learn the syntax?

# Go to https://doc.qt.io/qt-5/
# To the left is a heading that says "Reference".
# Underneath it, click "All Qt C++ Classes".
# Find "QPushButton" and click on it.
# This lists a lot of properties of QPushButtons...
# but not all of them because QPushButton inherits from
# QAbstractButton. It tells you this at the top.
# Click on "QAbstractButton".
# Now scroll down until you see a heading saying "Signals".
# There, we see "clicked". Click on "clicked".
# This is the documentation we need.
# In order to understand it we need to understand SIGNALS.


#%% SIGNALS AND SLOTS
# http://zetcode.com/gui/pyqt5/eventssignals/

# Above, we wrote self.btn.clicked.connect(self.btn_method)

# One of the key features of PyQt is its use of
# signals and slots to communicate between objects.

# A signal is emitted when something of potential interest happens;
# e.g. a button is clicked.

# A slot is a Python callable (a function or method); e.g. self.btn_method.

# If a signal is connected to a slot,
# then the slot is called when the signal is emitted;
# e.g. self.btn_method() is called when the button is clicked.

# If a signal isn't connected, then nothing happens;
# e.g. the previous code with the 'useless button'.

# The code (or component) that emits the signal
# does not know or care if the signal is being used.


# You will NOT need to make your own signals.
# That is NOT the purpose of the next example.

# The purpose of the next example is:

# 1) I write self.my_signal.connect(self.my_slot)
#    which highlights the general syntax.

# 2) It explains how to read the signature of a signal.
#    my_signal(int, int, int) means the signal emits 3 integers,
#    so a slot connected to it can receive up to 3 integers.
#    It can also choose to ignore some of these integers.

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSignal

class MyWidget(QWidget):
    # Here, I declare the signature of my_signal: int, int, int.
    my_signal = pyqtSignal(int, int, int)

    def __init__(self):
        super().__init__()                           # nothing new
        self.initUI()                                # nothing new

    def initUI(self):
        self.initGeo()                               # nothing new
        self.initBtn()                               # nothing new
        self.my_conn()
        self.show()                                  # nothing new

    def initGeo(self):
        self.setGeometry(200, 100, 400, 150)         # nothing new

    def initBtn(self):
        btn = QPushButton('Click me', self)          # nothing new
        btn.move(50, 50)                             # nothing new
        btn.resize(300, 50)                          # nothing new
        btn.clicked.connect(self.btn_method)         # nothing new

    def my_conn(self):
        # my_signal is connected to my_slot.
        self.my_signal.connect(self.my_slot)

    def btn_method(self):
        # Here, I emit a my_signal.
        # Since the signature said int, int, int,
        # it MUST emit 3 integers.
        self.my_signal.emit(8, 18, 88)

    def my_slot(self, i1, i2):
        # Since my_signal emits 3 integers,
        # the corresponding slot can receive up to 3 integers.
        # my_slot only takes in 2.
        print('my_signal was sent to my_slot')
        print('the signal sent the integers', i1, 'and', i2)

def main():
    app = QApplication([])                           # nothing new
    w = MyWidget()                                   # nothing new
    app.exec_()                                      # nothing new

if len(sys.argv) == 2 and sys.argv[1] == '5':
    main()


#%% USING ALL OF QPushButton's SIGNAL
# Going back to https://doc.qt.io/qt-5/qabstractbutton.html#clicked
# you'll see from the signature of clicked, that it emits a bool.
# The following code makes use of this bool.

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.initGeo()
        self.initBtn()
        self.show()

    def initGeo(self):
        self.setGeometry(200, 100, 400, 150)

    def initBtn(self):
        btn = QPushButton('Click me', self)
        btn.move(50, 50)
        btn.resize(300, 50)

        btn.setCheckable(True)
        # This is the new functionality we're exploring.
        # By setting this to be True,
        # the bool that "clicked" emits can be True or False.

        btn.clicked.connect(self.btn_method)

    def btn_method(self, checked):
        print('button clicked; checked ==', checked)

def main():
    app = QApplication([])
    w = MyWidget()
    app.exec_()

if len(sys.argv) == 2 and sys.argv[1] == '6':
    main()


#%% TIC-TAC-TOE 
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QPushButton, QMessageBox)
class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.initUI()

    def OX(self):
        if self.turn % 2 == 0:
            return 'O'
        return 'X'

    def initUI(self):
        self.setWindowTitle('Os and Xs')

        bw, bh = 100, 100     # these could be changed

        self.initGeo(bw, bh)  # geometry
        self.initBtn(bw, bh)  # buttons
        self.initSta()        # statuses: X, O, None
        self.show()

    def initGeo(self, bw, bh):
        self.setGeometry(100, 100, 3*bw, (7*bh) // 2)

    def initBtn(self, bw, bh):
        self.initOXs(bw, bh)  # X/O board
        self.initRes(bw, bh)  # restart

    def initSta(self):
        self.status = [None] * 9

    def initOXs(self, bw, bh):
        self.OX_btns = []

        for i in range(9):
            btn = QPushButton('', self)
            btn.move((i%3) * bw, (i//3) * bh)
            btn.resize(bw, bh)

            btn.setCheckable(True)
            btn.clicked.connect(self.OXs_func)

            self.OX_btns.append(btn)

    def initRes(self, bw, bh):
        btn = QPushButton('Restart', self)
        btn.move(0, 3*bh)
        btn.resize(3*bw, bh//2)

        btn.clicked.connect(self.restart_func)

    def OXs_func(self):
        # https://doc.qt.io/qt-5/qobject.html#sender
        # Quite a complicated function when you think about it.
        # Don't overthink it!
        # You won't need to use this function on your assignment.
        btn = self.sender()

        if btn.isChecked():           # there's some logic
            btn.setCheckable(False)   # to think through here
            btn.setText(self.OX())

            i = self.OX_btns.index(btn)
            self.status[i] = self.OX()

            self.checkStatus()

    def checkStatus(self):
        end = ((self.status[0] == self.status[1] == self.status[2] != None) or
               (self.status[3] == self.status[4] == self.status[5] != None) or
               (self.status[6] == self.status[7] == self.status[8] != None) or
               (self.status[0] == self.status[3] == self.status[6] != None) or
               (self.status[1] == self.status[4] == self.status[7] != None) or
               (self.status[2] == self.status[5] == self.status[8] != None) or
               (self.status[0] == self.status[4] == self.status[8] != None) or
               (self.status[2] == self.status[4] == self.status[6] != None))
        if end:
            # https://doc.qt.io/qt-5/qmessagebox.html
            msgBox = QMessageBox(self)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setText(self.OX() + ' wins!!')
            msgBox.show()

            self.stop()
        self.turn += 1

    def stop(self):
        for btn in self.OX_btns:
            btn.setCheckable(False)

    def restart_func(self):
        self.initSta()

        for btn in self.OX_btns:
            btn.setText('')
            btn.setCheckable(True)

def main():
    app = QApplication([])
    w = MyWidget()
    app.exec_()

if len(sys.argv) == 2 and sys.argv[1] == '7':
    main()


#%% EVENTS
# Widgets respond to events that are typically caused by user actions.
# PyQt delivers events to widgets by calling specific event handler functions.
# Instances of QEvent subclasses contain information about each event.


#%% MOUSE EVENTS
# The next example demonstrates how to use mouse events.
# We implement the event handling functions
#   - mousePressEvent
#   - mouseMoveEvent
#   - mouseDoubleClickEvent
# each of which receives a QMouseEvent.

from PyQt5.QtWidgets import QApplication, QWidget

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Mouse Events')
        self.show()

    def mousePressEvent(self, e):
        # https://doc.qt.io/qt-5/qwidget.html#mousePressEvent
        print('press')
        self.displayEventInfo(e)

    def mouseMoveEvent(self, e):
        # https://doc.qt.io/qt-5/qwidget.html#mouseMoveEvent
        print('move')
        self.displayEventInfo(e)

    def mouseDoubleClickEvent(self, e):
        # https://doc.qt.io/qt-5/qwidget.html#mouseDoubleClickEvent
        print('double click')
        self.displayEventInfo(e)

    def displayEventInfo(self, e):
        # https://doc.qt.io/qt-5/qmouseevent.html
        print('e.x() ==', e.x())
        print('e.y() ==', e.y())
        print('e.button() ==', e.button())
        print('')

def main():
    app = QApplication([])
    w = MyWidget()
    app.exec_()

if len(sys.argv) == 2 and sys.argv[1] == '8':
    main()


#%% QPAINTER
# https://doc.qt.io/qt-5/qwidget.html#paintEvent
# paintEvent is an event handling function that is
# called whenever a widget needs to be repainted.
# Every widget displaying custom content must implement it.

# The next example demonstrates how to use QPainter.
# Painting using an instance of QPainter can
# ONLY take place inside paintEvent or
# a function called by a paintEvent.

# If you want the widget to be repainted,
# it is best to call update:
# https://doc.qt.io/qt-5/qwidget.html#update

# In the next example, I've connected
# the clicked signal of a button to self.update.

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor
from random import randint

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Drawing')
        self.initGeo()
        self.initBtn()
        self.show()

    def initGeo(self):
        self.setGeometry(200, 100, 400, 150)

    def initBtn(self):
        btn = QPushButton('update', self)
        btn.move(0, 120)
        btn.resize(400, 30)

        # https://doc.qt.io/qt-5/qwidget.html#update
        btn.clicked.connect(self.update)

    # https://doc.qt.io/qt-5/qwidget.html#paintEvent
    def paintEvent(self, event):
        # https://doc.qt.io/qt-5/qpainter.html
        # https://doc.qt.io/qt-5/qpainter.html#begin
        qp = QPainter()
        qp.begin(self)

        self.drawPoints(qp)
        self.drawRectangles(qp)

        # https://doc.qt.io/qt-5/qpainter.html#end
        qp.end()

    def drawPoints(self, qp):
        # https://doc.qt.io/qt-5/qcolor.html#QColor-2
        # https://doc.qt.io/qt-5/qpainter.html#setPen-1
        qp.setPen(QColor(255, 0, 0))

        w = self.width()
        h = self.height()

        for i in range((w * h) // 40):
            x = randint(0, w-1)
            y = randint(0, h-1)

            # https://doc.qt.io/qt-5/qpainter.html#drawPoint-2
            qp.drawPoint(x, y)

    def drawRectangles(self, qp):
        # https://doc.qt.io/qt-5/qcolor.html#QColor-2
        yellow = QColor(236, 242, 32)

        # We're finally making use of alpha!
        red_orang = QColor(220,  78,  48, 255)
        ligh_purp = QColor(158, 128, 212, 220)
        dark_purp = QColor( 40,   0,  94, 160)

        # https://doc.qt.io/qt-5/qpainter.html#setPen-1
        qp.setPen(yellow)

        # https://doc.qt.io/qt-5/qpainter.html#setBrush
        # https://doc.qt.io/qt-5/qbrush.html#QBrush-2
        qp.setBrush(red_orang)
        qp.drawRect(10, 10, 380, 60)

        qp.setBrush(ligh_purp)
        qp.drawRect(50, 50, 300, 50)

        qp.setBrush(dark_purp)
        qp.drawRect(140, 30, 120, 90)

def main():
    app = QApplication([])
    w = MyWidget()
    app.exec_()

if len(sys.argv) == 2 and sys.argv[1] == '9':
    main()

#%% QTIMER
# https://doc.qt.io/qt-5/qtimer.html#details
# https://doc.qt.io/qt-5/qtimer.html#public-slots

# QTimer is a useful class.
# After creating an instance of QTimer and calling "start",
# "timeout" signals are emitted at constant intervals.

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QTimer

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initTimer()

    def initTimer(self):
        self.i = 0

        # https://doc.qt.io/qt-5/qtimer.html#timeout
        # https://doc.qt.io/qt-5/qtimer.html#start-1
        self.t = QTimer()
        self.t.timeout.connect(self.timer_method)
        self.t.start(500)

        # The following would also work.
        # t = QTimer(self)
        # t.timeout.connect(self.timer_method)
        # t.start(500)

        # To avoid the QTimer being garbage-collected,
        # we need to make sure that some reference to it exists.
        # The first way is to make it an instance variable.
        # The second way is to make it a child of our main widget.
        # Note: we always make buttons a child of our main widget
        # which is why we have not encountered this issue before.

    def timer_method(self):
        # We set flush to True to make sure that
        # print statements are not held in a buffer.
        print(self.i, flush = True)
        self.i += 1

def main():
    app = QApplication([])
    w = MyWidget()
    app.exec_()

if len(sys.argv) == 2 and sys.argv[1] == '10':
    main()


#%% QTIMER
# Another option is to use singleShot.
# https://doc.qt.io/qt-5/qtimer.html#singleShot-4

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QTimer

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initTimer()

    def initTimer(self):
        self.i = 0
        self.timer_method()

    def timer_method(self):
        print(self.i, flush = True)
        self.i += 1

        QTimer.singleShot(500, self.timer_method)

def main():
    app = QApplication([])
    w = MyWidget()
    app.exec_()

if len(sys.argv) == 2 and sys.argv[1] == '11':
    main()


#%% QTHREAD
# In my experience,
# having the QTimer run in a separate thread improves performance.

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QTimer, QThread

# https://doc.qt.io/qt-5/qthread.html
class MyTimer(QThread):
    def __init__(self, parent, func, t):
        super().__init__(parent)
        self.func = func
        self.t = t

    def run(self):
        timer = QTimer()
        timer.timeout.connect(self.func)
        timer.start(self.t)

        # https://doc.qt.io/qt-5/qthread.html#exec
        self.exec_()
        # Runs an event loop inside the thread.
        # This makes sure the run method does not finish executing.

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initTimer()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QTimer with QThread')
        self.initBtn()
        self.show()

    def initBtn(self):
        btn = QPushButton('start / stop', self)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.btn_method)

    def initTimer(self):
        self.i = 0
        self.thread = MyTimer(self, self.timer_method, 500)

        # https://doc.qt.io/qt-5/qthread.html#finished
        self.thread.finished.connect(self.threadFinished)

    def closeEvent(self, e):
        self.thread.quit()
        # This tells the thread's event loop to stop;
        # it does nothing if the thread does not have an event loop.

    def threadFinished(self):
        print('thread finished', flush = True)

    def btn_method(self):
        # https://doc.qt.io/qt-5/qthread.html#isRunning
        # https://doc.qt.io/qt-5/qthread.html#public-slots
        if self.thread.isRunning():
            self.thread.quit()
        else:
            self.thread.start()

    def timer_method(self):
        print(self.i, flush = True)
        self.i += 1

def main():
    app = QApplication([])
    w = MyWidget()
    app.exec_()

if len(sys.argv) == 2 and sys.argv[1] == '12':
    main()
