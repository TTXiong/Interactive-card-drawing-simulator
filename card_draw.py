# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'card_draw.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(731, 423)
        self.one_draw = QtWidgets.QPushButton(Form)
        self.one_draw.setGeometry(QtCore.QRect(350, 300, 91, 51))
        self.one_draw.setObjectName("one_draw")
        self.ten_draw = QtWidgets.QPushButton(Form)
        self.ten_draw.setGeometry(QtCore.QRect(600, 300, 91, 51))
        self.ten_draw.setObjectName("ten_draw")
        self.result = QtWidgets.QTextBrowser(Form)
        self.result.setGeometry(QtCore.QRect(320, 40, 371, 221))
        self.result.setObjectName("result")
        self.guarantee_text = QtWidgets.QLabel(Form)
        self.guarantee_text.setGeometry(QtCore.QRect(260, 370, 131, 31))
        self.guarantee_text.setObjectName("guarantee_text")
        self.count = QtWidgets.QLabel(Form)
        self.count.setGeometry(QtCore.QRect(400, 370, 31, 31))
        self.count.setObjectName("count")
        self.prob_label = QtWidgets.QLabel(Form)
        self.prob_label.setGeometry(QtCore.QRect(30, 110, 101, 41))
        self.prob_label.setObjectName("prob_label")
        self.prob = QtWidgets.QLineEdit(Form)
        self.prob.setGeometry(QtCore.QRect(140, 110, 41, 31))
        self.prob.setObjectName("prob")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.one_draw.setText(_translate("Form", "单抽"))
        self.ten_draw.setText(_translate("Form", "十连"))
        self.guarantee_text.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">距离大保底次数：</span></p></body></html>"))
        self.count.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">80</span></p></body></html>"))
        self.prob_label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">五星概率（%）：</span></p></body></html>"))
