from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1231, 898)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 标题
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 1211, 31))
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily("Adobe 楷体 Std R")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 40, 1211, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)

        self.pushButton.clicked.connect(MainWindow.load_img)
        self.pushButton_2.clicked.connect(MainWindow.load_mask)
        self.pushButton_3.clicked.connect(MainWindow.segmentation)
        self.pushButton_4.clicked.connect(MainWindow.close)

        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 140, 1211, 711))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.vtkWidget = QVTKRenderWindowInteractor(self.gridLayoutWidget_2)
        self.vtkWidget.setObjectName("openGLWidget")
        self.gridLayout_3.addWidget(self.vtkWidget, 0, 0, 1, 1)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.gridLayoutWidget_2)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.gridLayout_3.addWidget(self.verticalScrollBar, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.gridLayout_2.addWidget(self.horizontalSlider_2, 1, 1, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_2.addWidget(self.horizontalSlider, 1, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")

        self.vtkWidget_3 = QVTKRenderWindowInteractor(self.gridLayoutWidget_2)
        self.vtkWidget_3.setObjectName("openGLWidget_3")
        self.gridLayout_5.addWidget(self.vtkWidget_3, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_5, 2, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.vtkWidget_2 = QVTKRenderWindowInteractor(self.gridLayoutWidget_2)
        self.vtkWidget_2.setObjectName("openGLWidget_2")
        self.gridLayout_4.addWidget(self.vtkWidget_2, 0, 0, 1, 1)
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(self.gridLayoutWidget_2)
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.gridLayout_4.addWidget(self.verticalScrollBar_2, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 0, 1, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")

        self.vtkWidget_4 = QVTKRenderWindowInteractor(self.gridLayoutWidget_2)
        self.vtkWidget_4.setObjectName("openGLWidget_4")
        self.gridLayout_6.addWidget(self.vtkWidget_4, 0, 0, 1, 1)
        self.verticalScrollBar_3 = QtWidgets.QScrollBar(self.gridLayoutWidget_2)
        self.verticalScrollBar_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_3.setObjectName("verticalScrollBar_3")
        self.gridLayout_6.addWidget(self.verticalScrollBar_3, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_6, 2, 1, 1, 1)
        self.horizontalSlider_3 = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.gridLayout_2.addWidget(self.horizontalSlider_3, 3, 1, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 110, 1211, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1231, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "肺叶分割软件"))
        self.pushButton.setText(_translate("MainWindow", "加载原始图像"))
        self.pushButton_2.setText(_translate("MainWindow", "加载Mask"))
        self.pushButton_3.setText(_translate("MainWindow", "分割肺叶"))
        self.pushButton_4.setText(_translate("MainWindow", "关闭"))
        self.label.setText(_translate("MainWindow", "欢迎使用肺叶分割软件"))
        MainWindow.setWindowIcon(QIcon('myico.ico'))
