# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'swipetool.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(465, 250)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMinimumSize(QSize(465, 250))
        Widget.setMaximumSize(QSize(465, 250))
        self.layoutWidget = QWidget(Widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 200, 446, 51))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.start_button = QPushButton(self.layoutWidget)
        self.start_button.setObjectName(u"start_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.start_button.sizePolicy().hasHeightForWidth())
        self.start_button.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.start_button)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.stop_button = QPushButton(self.layoutWidget)
        self.stop_button.setObjectName(u"stop_button")
        sizePolicy1.setHeightForWidth(self.stop_button.sizePolicy().hasHeightForWidth())
        self.stop_button.setSizePolicy(sizePolicy1)
        self.stop_button.setAutoFillBackground(False)

        self.horizontalLayout_2.addWidget(self.stop_button)

        self.layoutWidget1 = QWidget(Widget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 20, 446, 149))
        self.gridLayout_2 = QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.end_x_axis_lineedit = QLineEdit(self.layoutWidget1)
        self.end_x_axis_lineedit.setObjectName(u"end_x_axis_lineedit")

        self.gridLayout_2.addWidget(self.end_x_axis_lineedit, 2, 1, 1, 1)

        self.start_y_axis_label = QLabel(self.layoutWidget1)
        self.start_y_axis_label.setObjectName(u"start_y_axis_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.start_y_axis_label.sizePolicy().hasHeightForWidth())
        self.start_y_axis_label.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.start_y_axis_label, 1, 2, 1, 1)

        self.swipe_times_label = QLabel(self.layoutWidget1)
        self.swipe_times_label.setObjectName(u"swipe_times_label")
        sizePolicy2.setHeightForWidth(self.swipe_times_label.sizePolicy().hasHeightForWidth())
        self.swipe_times_label.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.swipe_times_label, 3, 2, 1, 1)

        self.swipe_times_spinbox = QSpinBox(self.layoutWidget1)
        self.swipe_times_spinbox.setObjectName(u"swipe_times_spinbox")
        sizePolicy1.setHeightForWidth(self.swipe_times_spinbox.sizePolicy().hasHeightForWidth())
        self.swipe_times_spinbox.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.swipe_times_spinbox, 3, 3, 1, 1)

        self.end_y_axis_lineedit = QLineEdit(self.layoutWidget1)
        self.end_y_axis_lineedit.setObjectName(u"end_y_axis_lineedit")

        self.gridLayout_2.addWidget(self.end_y_axis_lineedit, 2, 3, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pause_duration_spinbox = QSpinBox(self.layoutWidget1)
        self.pause_duration_spinbox.setObjectName(u"pause_duration_spinbox")
        sizePolicy1.setHeightForWidth(self.pause_duration_spinbox.sizePolicy().hasHeightForWidth())
        self.pause_duration_spinbox.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.pause_duration_spinbox)

        self.second = QLabel(self.layoutWidget1)
        self.second.setObjectName(u"second")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.second.sizePolicy().hasHeightForWidth())
        self.second.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.second)


        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 1, 1, 1)

        self.end_x_axis_label = QLabel(self.layoutWidget1)
        self.end_x_axis_label.setObjectName(u"end_x_axis_label")
        sizePolicy2.setHeightForWidth(self.end_x_axis_label.sizePolicy().hasHeightForWidth())
        self.end_x_axis_label.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.end_x_axis_label, 2, 0, 1, 1)

        self.start_y_axis_lineedit = QLineEdit(self.layoutWidget1)
        self.start_y_axis_lineedit.setObjectName(u"start_y_axis_lineedit")

        self.gridLayout_2.addWidget(self.start_y_axis_lineedit, 1, 3, 1, 1)

        self.start_x_axis_label = QLabel(self.layoutWidget1)
        self.start_x_axis_label.setObjectName(u"start_x_axis_label")
        sizePolicy2.setHeightForWidth(self.start_x_axis_label.sizePolicy().hasHeightForWidth())
        self.start_x_axis_label.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.start_x_axis_label, 1, 0, 1, 1)

        self.end_y_axis_label = QLabel(self.layoutWidget1)
        self.end_y_axis_label.setObjectName(u"end_y_axis_label")

        self.gridLayout_2.addWidget(self.end_y_axis_label, 2, 2, 1, 1)

        self.pause_duration_label = QLabel(self.layoutWidget1)
        self.pause_duration_label.setObjectName(u"pause_duration_label")
        sizePolicy2.setHeightForWidth(self.pause_duration_label.sizePolicy().hasHeightForWidth())
        self.pause_duration_label.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.pause_duration_label, 3, 0, 1, 1)

        self.device_label = QLabel(self.layoutWidget1)
        self.device_label.setObjectName(u"device_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.device_label.sizePolicy().hasHeightForWidth())
        self.device_label.setSizePolicy(sizePolicy4)
        self.device_label.setLayoutDirection(Qt.LeftToRight)
        self.device_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.device_label, 0, 0, 1, 1)

        self.start_x_axis_lineedit = QLineEdit(self.layoutWidget1)
        self.start_x_axis_lineedit.setObjectName(u"start_x_axis_lineedit")

        self.gridLayout_2.addWidget(self.start_x_axis_lineedit, 1, 1, 1, 1)

        self.comboBox = QComboBox(self.layoutWidget1)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy5)
        self.comboBox.setMouseTracking(False)
        self.comboBox.setModelColumn(0)

        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Phone Swipe Tool", None))
        self.start_button.setText(QCoreApplication.translate("Widget", u"Start Swipe", None))
        self.stop_button.setText(QCoreApplication.translate("Widget", u"Stop Swipe", None))
        self.start_y_axis_label.setText(QCoreApplication.translate("Widget", u"Start Y Axis", None))
        self.swipe_times_label.setText(QCoreApplication.translate("Widget", u"Swipe Times", None))
        self.second.setText(QCoreApplication.translate("Widget", u"second", None))
        self.end_x_axis_label.setText(QCoreApplication.translate("Widget", u"End X Axis", None))
        self.start_x_axis_label.setText(QCoreApplication.translate("Widget", u"Start X Axis", None))
        self.end_y_axis_label.setText(QCoreApplication.translate("Widget", u"End Y Axis", None))
        self.pause_duration_label.setText(QCoreApplication.translate("Widget", u"Pause Duration", None))
        self.device_label.setText(QCoreApplication.translate("Widget", u"Device", None))
    # retranslateUi

