from PyQt6 import QtCore, QtWidgets
import pygame
import os



MAIN_PATH = os.path.dirname(__file__)

KEY_MAP = {
    QtCore.Qt.Key.Key_A: 'C2',
    QtCore.Qt.Key.Key_S: 'D2',
    QtCore.Qt.Key.Key_D: 'E2',
    QtCore.Qt.Key.Key_F: 'F2',
    QtCore.Qt.Key.Key_G: 'G2',
    QtCore.Qt.Key.Key_H: 'A2',
    QtCore.Qt.Key.Key_J: 'B2',
    QtCore.Qt.Key.Key_K: 'C3',
    QtCore.Qt.Key.Key_W: 'C2H',
    QtCore.Qt.Key.Key_E: 'D2H',
    QtCore.Qt.Key.Key_T: 'F2H',
    QtCore.Qt.Key.Key_Y: 'G2H',
    QtCore.Qt.Key.Key_U: 'A2H',
    QtCore.Qt.Key.Key_Z: 'C3',
    QtCore.Qt.Key.Key_X: 'D3',
    QtCore.Qt.Key.Key_C: 'E3',
    QtCore.Qt.Key.Key_V: 'F3',
    QtCore.Qt.Key.Key_B: 'G3',
    QtCore.Qt.Key.Key_N: 'A3',
    QtCore.Qt.Key.Key_M: 'B3',
    QtCore.Qt.Key.Key_3: 'C3H',
    QtCore.Qt.Key.Key_4: 'D3H',
    QtCore.Qt.Key.Key_6: 'F3H',
    QtCore.Qt.Key.Key_7: 'G3H',
    QtCore.Qt.Key.Key_8: 'A3H',
}



class KeyboardUI(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(850, 224)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.C2 = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.C2.sizePolicy().hasHeightForWidth())
        self.C2.setSizePolicy(sizePolicy)
        self.C2.setStyleSheet("background-color: white;")
        self.C2.setObjectName("C2")
        self.horizontalLayout.addWidget(self.C2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.C2H = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.C2H.sizePolicy().hasHeightForWidth())
        self.C2H.setSizePolicy(sizePolicy)
        self.C2H.setMinimumSize(QtCore.QSize(31, 121))
        self.C2H.setAutoFillBackground(False)
        self.C2H.setStyleSheet("QPushButton { background-color: black; }")
        self.C2H.setDefault(False)
        self.C2H.setFlat(False)
        self.C2H.setObjectName("C2H")
        self.verticalLayout.addWidget(self.C2H)
        spacerItem = QtWidgets.QSpacerItem(20, 78, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.D2 = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.D2.sizePolicy().hasHeightForWidth())
        self.D2.setSizePolicy(sizePolicy)
        self.D2.setStyleSheet("background-color: white;")
        self.D2.setObjectName("D2")
        self.horizontalLayout.addWidget(self.D2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.D2H = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.D2H.sizePolicy().hasHeightForWidth())
        self.D2H.setSizePolicy(sizePolicy)
        self.D2H.setMinimumSize(QtCore.QSize(31, 121))
        self.D2H.setStyleSheet("QPushButton { background-color: black; }")
        self.D2H.setObjectName("D2H")
        self.verticalLayout_2.addWidget(self.D2H)
        spacerItem1 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.E2 = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.E2.sizePolicy().hasHeightForWidth())
        self.E2.setSizePolicy(sizePolicy)
        self.E2.setStyleSheet("background-color: white;")
        self.E2.setObjectName("E2")
        self.horizontalLayout.addWidget(self.E2)
        self.F2 = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.F2.sizePolicy().hasHeightForWidth())
        self.F2.setSizePolicy(sizePolicy)
        self.F2.setStyleSheet("background-color: white;")
        self.F2.setObjectName("F2")
        self.horizontalLayout.addWidget(self.F2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.F2H = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.F2H.sizePolicy().hasHeightForWidth())
        self.F2H.setSizePolicy(sizePolicy)
        self.F2H.setMinimumSize(QtCore.QSize(31, 121))
        self.F2H.setStyleSheet("QPushButton { background-color: black; }")
        self.F2H.setObjectName("F2H")
        self.verticalLayout_3.addWidget(self.F2H)
        spacerItem2 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.G2 = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.G2.sizePolicy().hasHeightForWidth())
        self.G2.setSizePolicy(sizePolicy)
        self.G2.setStyleSheet("background-color: white;")
        self.G2.setObjectName("G2")
        self.horizontalLayout.addWidget(self.G2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.G2H = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.G2H.sizePolicy().hasHeightForWidth())
        self.G2H.setSizePolicy(sizePolicy)
        self.G2H.setMinimumSize(QtCore.QSize(31, 121))
        self.G2H.setStyleSheet("QPushButton { background-color: black; }")
        self.G2H.setObjectName("G2H")
        self.verticalLayout_4.addWidget(self.G2H)
        spacerItem3 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.A2 = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.A2.sizePolicy().hasHeightForWidth())
        self.A2.setSizePolicy(sizePolicy)
        self.A2.setStyleSheet("background-color: white;")
        self.A2.setObjectName("A2")
        self.horizontalLayout.addWidget(self.A2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.A2H = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.A2H.sizePolicy().hasHeightForWidth())
        self.A2H.setSizePolicy(sizePolicy)
        self.A2H.setMinimumSize(QtCore.QSize(31, 121))
        self.A2H.setStyleSheet("QPushButton { background-color: black; }")
        self.A2H.setObjectName("A2H")
        self.verticalLayout_5.addWidget(self.A2H)
        spacerItem4 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_5.addItem(spacerItem4)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.B2 = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.B2.sizePolicy().hasHeightForWidth())
        self.B2.setSizePolicy(sizePolicy)
        self.B2.setStyleSheet("background-color: white;")
        self.B2.setObjectName("B2")
        self.horizontalLayout.addWidget(self.B2)
        self.C3 = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.C3.sizePolicy().hasHeightForWidth())
        self.C3.setSizePolicy(sizePolicy)
        self.C3.setStyleSheet("background-color: white;")
        self.C3.setObjectName("C3")
        self.horizontalLayout.addWidget(self.C3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.C3H = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.C3H.sizePolicy().hasHeightForWidth())
        self.C3H.setSizePolicy(sizePolicy)
        self.C3H.setMinimumSize(QtCore.QSize(31, 121))
        self.C3H.setStyleSheet("QPushButton { background-color: black; }")
        self.C3H.setObjectName("C3H")
        self.verticalLayout_6.addWidget(self.C3H)
        spacerItem5 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_6.addItem(spacerItem5)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.D3 = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.D3.sizePolicy().hasHeightForWidth())
        self.D3.setSizePolicy(sizePolicy)
        self.D3.setStyleSheet("background-color: white;")
        self.D3.setObjectName("D3")
        self.horizontalLayout.addWidget(self.D3)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.D3H = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.D3H.sizePolicy().hasHeightForWidth())
        self.D3H.setSizePolicy(sizePolicy)
        self.D3H.setMinimumSize(QtCore.QSize(31, 121))
        self.D3H.setStyleSheet("QPushButton { background-color: black; }")
        self.D3H.setObjectName("D3H")
        self.verticalLayout_7.addWidget(self.D3H)
        spacerItem6 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_7.addItem(spacerItem6)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.E3 = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.E3.sizePolicy().hasHeightForWidth())
        self.E3.setSizePolicy(sizePolicy)
        self.E3.setStyleSheet("background-color: white;")
        self.E3.setObjectName("E3")
        self.horizontalLayout.addWidget(self.E3)
        self.F3 = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.F3.sizePolicy().hasHeightForWidth())
        self.F3.setSizePolicy(sizePolicy)
        self.F3.setStyleSheet("background-color: white;")
        self.F3.setAutoDefault(False)
        self.F3.setDefault(True)
        self.F3.setObjectName("F3")
        self.horizontalLayout.addWidget(self.F3)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.F3H = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.F3H.sizePolicy().hasHeightForWidth())
        self.F3H.setSizePolicy(sizePolicy)
        self.F3H.setMinimumSize(QtCore.QSize(31, 121))
        self.F3H.setStyleSheet("QPushButton { background-color: black; }")
        self.F3H.setObjectName("F3H")
        self.verticalLayout_8.addWidget(self.F3H)
        spacerItem7 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_8.addItem(spacerItem7)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.G3 = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.G3.sizePolicy().hasHeightForWidth())
        self.G3.setSizePolicy(sizePolicy)
        self.G3.setStyleSheet("background-color: white;")
        self.G3.setObjectName("G3")
        self.horizontalLayout.addWidget(self.G3)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.G3H = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.G3H.sizePolicy().hasHeightForWidth())
        self.G3H.setSizePolicy(sizePolicy)
        self.G3H.setMinimumSize(QtCore.QSize(31, 121))
        self.G3H.setStyleSheet("QPushButton { background-color: black; }")
        self.G3H.setObjectName("G3H")
        self.verticalLayout_9.addWidget(self.G3H)
        spacerItem8 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_9.addItem(spacerItem8)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        self.A3 = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.A3.sizePolicy().hasHeightForWidth())
        self.A3.setSizePolicy(sizePolicy)
        self.A3.setStyleSheet("background-color: white;")
        self.A3.setObjectName("A3")
        self.horizontalLayout.addWidget(self.A3)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.A3H = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.A3H.sizePolicy().hasHeightForWidth())
        self.A3H.setSizePolicy(sizePolicy)
        self.A3H.setMinimumSize(QtCore.QSize(31, 121))
        self.A3H.setStyleSheet("QPushButton { background-color: black; }")
        self.A3H.setObjectName("A3H")
        self.verticalLayout_10.addWidget(self.A3H)
        spacerItem9 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_10.addItem(spacerItem9)
        self.horizontalLayout.addLayout(self.verticalLayout_10)
        self.B3 = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.B3.sizePolicy().hasHeightForWidth())
        self.B3.setSizePolicy(sizePolicy)
        self.B3.setStyleSheet("background-color: white;")
        self.B3.setAutoDefault(True)
        self.B3.setObjectName("B3")
        self.horizontalLayout.addWidget(self.B3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Piano"))
        self.C2.setText(_translate("Form", "C2"))
        self.C2H.setText(_translate("Form", "C2#"))
        self.D2.setText(_translate("Form", "D2"))
        self.D2H.setText(_translate("Form", "D2#"))
        self.E2.setText(_translate("Form", "E2"))
        self.F2.setText(_translate("Form", "F2"))
        self.F2H.setText(_translate("Form", "F2#"))
        self.G2.setText(_translate("Form", "G2"))
        self.G2H.setText(_translate("Form", "G2#"))
        self.A2.setText(_translate("Form", "A2"))
        self.A2H.setText(_translate("Form", "A2#"))
        self.B2.setText(_translate("Form", "B2"))
        self.C3.setText(_translate("Form", "C3"))
        self.C3H.setText(_translate("Form", "C3#"))
        self.D3.setText(_translate("Form", "D3"))
        self.D3H.setText(_translate("Form", "D3#"))
        self.E3.setText(_translate("Form", "E3"))
        self.F3.setText(_translate("Form", "F3"))
        self.F3H.setText(_translate("Form", "F3#"))
        self.G3.setText(_translate("Form", "G3"))
        self.G3H.setText(_translate("Form", "G3#"))
        self.A3.setText(_translate("Form", "A3"))
        self.A3H.setText(_translate("Form", "A3#"))
        self.B3.setText(_translate("Form", "B3"))



class QtPiano(KeyboardUI, QtWidgets. QWidget):
    def __init__(self):
        super(QtPiano, self).__init__()
        self.pressed_keys = []

        self.setupUi(self)
        self.initialize_sounds()
        self.init_connection()
        self.init_button_map()


    def init_button_map(self):
        self.button_map = {
            QtCore.Qt.Key.Key_A: self.C2,
            QtCore.Qt.Key.Key_S: self.D2,
            QtCore.Qt.Key.Key_D: self.E2,
            QtCore.Qt.Key.Key_F: self.F2,
            QtCore.Qt.Key.Key_G: self.G2,
            QtCore.Qt.Key.Key_H: self.A2,
            QtCore.Qt.Key.Key_J: self.B2,
            QtCore.Qt.Key.Key_K: self.C3,
            QtCore.Qt.Key.Key_Z: self.C3,
            QtCore.Qt.Key.Key_X: self.D3,
            QtCore.Qt.Key.Key_C: self.E3,
            QtCore.Qt.Key.Key_V: self.F3,
            QtCore.Qt.Key.Key_B: self.G3,
            QtCore.Qt.Key.Key_N: self.A3,
            QtCore.Qt.Key.Key_M: self.B3,
        }
        self.button_map_H = {
            QtCore.Qt.Key.Key_W: self.C2H,
            QtCore.Qt.Key.Key_E: self.D2H,
            QtCore.Qt.Key.Key_T: self.F2H,
            QtCore.Qt.Key.Key_Y: self.G2H,
            QtCore.Qt.Key.Key_U: self.A2H,
            QtCore.Qt.Key.Key_3: self.C3H,
            QtCore.Qt.Key.Key_4: self.D3H,
            QtCore.Qt.Key.Key_6: self.F3H,
            QtCore.Qt.Key.Key_7: self.G3H,
            QtCore.Qt.Key.Key_8: self.A3H
        }

    def set_button(self, button, on=True, black=False):
        button.setStyleSheet("background-color: yellow" if on else (
            "background-color: black" if black else "background-color: white;"))


    def init_connection(self):
        for note in ['C2', 'C2H', 'D2', 'D2H', 'E2', 'F2', 'F2H', 'G2', 'G2H', 'A2', 'A2H', 'B2',
                     'C3', 'C3H', 'D3', 'D3H', 'E3', 'F3', 'F3H', 'G3', 'G3H', 'A3', 'A3H', 'B3']:
            button = getattr(self, note)
            button.clicked.connect(lambda checked, note=note: self.sounds[note].play())

    def initialize_sounds(self):
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.mixer.init()
        self.sounds = {}
        for note in ['C2','C2H','D2','D2H','E2','F2','F2H','G2','G2H','A2','A2H','B2',
                     'C3','C3H','D3','D3H','E3','F3','F3H','G3','G3H','A3','A3H','B3']:
            self.sounds[note] = pygame.mixer.Sound(os.path.join(MAIN_PATH, f'Notes/{note}.mp3'))


    def keyPressEvent(self, event):
        if event.key() in KEY_MAP and KEY_MAP.get(event.key()) not in self.pressed_keys:
            self.pressed_keys.append(KEY_MAP[event.key()])
            self.sounds[KEY_MAP[event.key()]].play()
            if event.key() in self.button_map:
                self.set_button(self.button_map[event.key()])
            elif event.key() in self.button_map_H:
                self.set_button(self.button_map_H[event.key()], black=True)

    def keyReleaseEvent(self, event):
        if event.isAutoRepeat():
            return
        if KEY_MAP.get(event.key()) in self.pressed_keys:
            self.pressed_keys.remove(KEY_MAP[event.key()])
        if event.key() in self.button_map:
            self.set_button(self.button_map[event.key()], False)
        elif event.key() in self.button_map_H:
            self.set_button(self.button_map_H[event.key()], False, True)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = QtPiano()
    main.show()
    sys.exit(app.exec())