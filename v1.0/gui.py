# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myGui.ui'
#
# Created: Fri Jan 24 03:08:38 2014
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

state=[False,'',True]
timeScaleValue=[1,-8,-4,-2,2,4,8]
from PyQt4 import QtCore, QtGui
from myAudio import IO,MyWave
import wave,pyaudio

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_WaveMixer(object):

    def __init__(self):
        self.wave1=MyWave();
        self.wave2=MyWave();
        self.wave3=MyWave();
        self.waveModulated=MyWave();
        self.waveMixed=MyWave();
        self.waveRecorded=MyWave();
        self.io=IO();

    def setupUi(self, WaveMixer):
        WaveMixer.setObjectName(_fromUtf8("WaveMixer"))
        WaveMixer.setEnabled(True)
        WaveMixer.resize(1039, 695)
        WaveMixer.setAcceptDrops(False)
        WaveMixer.setAutoFillBackground(True)
        self.centralwidget = QtGui.QWidget(WaveMixer)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 51, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.timeShift1 = QtGui.QSlider(self.centralwidget)
        self.timeShift1.setGeometry(QtCore.QRect(310, 20, 541, 29))
        self.timeShift1.setAcceptDrops(False)
        self.timeShift1.setMinimum(-16000)
        self.timeShift1.setMaximum(16000)
        self.timeShift1.setPageStep(1)
        self.timeShift1.setTracking(True)
        self.timeShift1.setOrientation(QtCore.Qt.Horizontal)
        self.timeShift1.setTickPosition(QtGui.QSlider.TicksBelow)
        self.timeShift1.setTickInterval(1000)
        self.timeShift1.setObjectName(_fromUtf8("timeShift1"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(860, 16, 51, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 20, 81, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(230, 60, 81, 31))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(550, 60, 81, 31))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(640, 180, 211, 59))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_13.setMargin(0)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.timeScale2 = QtGui.QSlider(self.layoutWidget)
        self.timeScale2.setMaximum(6)
        self.timeScale2.setPageStep(1)
        self.timeScale2.setOrientation(QtCore.Qt.Horizontal)
        self.timeScale2.setTickPosition(QtGui.QSlider.TicksBelow)
        self.timeScale2.setTickInterval(1)
        self.timeScale2.setObjectName(_fromUtf8("timeScale2"))
        self.verticalLayout_13.addWidget(self.timeScale2)
        self.label_16 = QtGui.QLabel(self.layoutWidget)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.verticalLayout_13.addWidget(self.label_16)
        self.timeShift2 = QtGui.QSlider(self.centralwidget)
        self.timeShift2.setGeometry(QtCore.QRect(310, 140, 541, 29))
        self.timeShift2.setAcceptDrops(False)
        self.timeShift2.setMinimum(-16000)
        self.timeShift2.setMaximum(16000)
        self.timeShift2.setPageStep(1)
        self.timeShift2.setTracking(True)
        self.timeShift2.setOrientation(QtCore.Qt.Horizontal)
        self.timeShift2.setTickPosition(QtGui.QSlider.TicksBelow)
        self.timeShift2.setTickInterval(1000)
        self.timeShift2.setObjectName(_fromUtf8("timeShift2"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(550, 180, 81, 31))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.layoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(890, 140, 126, 101))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_14.setMargin(0)
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.mixing2 = QtGui.QCheckBox(self.layoutWidget_2)
        self.mixing2.setObjectName(_fromUtf8("mixing2"))
        self.verticalLayout_14.addWidget(self.mixing2)
        self.modulation2 = QtGui.QCheckBox(self.layoutWidget_2)
        self.modulation2.setObjectName(_fromUtf8("modulation2"))
        self.verticalLayout_14.addWidget(self.modulation2)
        self.reverse2 = QtGui.QCheckBox(self.layoutWidget_2)
        self.reverse2.setObjectName(_fromUtf8("reverse2"))
        self.verticalLayout_14.addWidget(self.reverse2)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(860, 136, 51, 31))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(230, 180, 81, 31))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_18 = QtGui.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(20, 130, 51, 31))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.layoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(310, 180, 161, 59))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.verticalLayout_15 = QtGui.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_15.setMargin(0)
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.amplitude2 = QtGui.QSlider(self.layoutWidget_3)
        self.amplitude2.setMaximum(100)
        self.amplitude2.setPageStep(1)
        self.amplitude2.setProperty("value", 20)
        self.amplitude2.setOrientation(QtCore.Qt.Horizontal)
        self.amplitude2.setTickPosition(QtGui.QSlider.TicksBelow)
        self.amplitude2.setTickInterval(20)
        self.amplitude2.setObjectName(_fromUtf8("amplitude2"))
        self.verticalLayout_15.addWidget(self.amplitude2)
        self.label_20 = QtGui.QLabel(self.layoutWidget_3)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.verticalLayout_15.addWidget(self.label_20)
        self.label_21 = QtGui.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(230, 140, 81, 31))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.layoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(640, 300, 211, 59))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.verticalLayout_16 = QtGui.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_16.setMargin(0)
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.timeScale3 = QtGui.QSlider(self.layoutWidget_4)
        self.timeScale3.setMaximum(6)
        self.timeScale3.setPageStep(1)
        self.timeScale3.setOrientation(QtCore.Qt.Horizontal)
        self.timeScale3.setTickPosition(QtGui.QSlider.TicksBelow)
        self.timeScale3.setTickInterval(1)
        self.timeScale3.setObjectName(_fromUtf8("timeScale3"))
        self.verticalLayout_16.addWidget(self.timeScale3)
        self.label_22 = QtGui.QLabel(self.layoutWidget_4)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.verticalLayout_16.addWidget(self.label_22)
        self.timeShift3 = QtGui.QSlider(self.centralwidget)
        self.timeShift3.setGeometry(QtCore.QRect(310, 260, 541, 29))
        self.timeShift3.setAcceptDrops(False)
        self.timeShift3.setMinimum(-16000)
        self.timeShift3.setMaximum(16000)
        self.timeShift3.setPageStep(1)
        self.timeShift3.setTracking(True)
        self.timeShift3.setOrientation(QtCore.Qt.Horizontal)
        self.timeShift3.setTickPosition(QtGui.QSlider.TicksBelow)
        self.timeShift3.setTickInterval(1000)
        self.timeShift3.setObjectName(_fromUtf8("timeShift3"))
        self.label_23 = QtGui.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(550, 300, 81, 31))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.layoutWidget_5 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_5.setGeometry(QtCore.QRect(890, 260, 126, 101))
        self.layoutWidget_5.setObjectName(_fromUtf8("layoutWidget_5"))
        self.verticalLayout_17 = QtGui.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_17.setMargin(0)
        self.verticalLayout_17.setObjectName(_fromUtf8("verticalLayout_17"))
        self.mixing3 = QtGui.QCheckBox(self.layoutWidget_5)
        self.mixing3.setObjectName(_fromUtf8("mixing3"))
        self.verticalLayout_17.addWidget(self.mixing3)
        self.modulation3 = QtGui.QCheckBox(self.layoutWidget_5)
        self.modulation3.setObjectName(_fromUtf8("modulation3"))
        self.verticalLayout_17.addWidget(self.modulation3)
        self.reverse3 = QtGui.QCheckBox(self.layoutWidget_5)
        self.reverse3.setObjectName(_fromUtf8("reverse3"))
        self.verticalLayout_17.addWidget(self.reverse3)
        self.label_25 = QtGui.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(860, 256, 51, 31))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.label_26 = QtGui.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(230, 300, 81, 31))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.label_27 = QtGui.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(20, 250, 51, 31))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.layoutWidget_6 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_6.setGeometry(QtCore.QRect(310, 300, 161, 59))
        self.layoutWidget_6.setObjectName(_fromUtf8("layoutWidget_6"))
        self.verticalLayout_18 = QtGui.QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_18.setMargin(0)
        self.verticalLayout_18.setObjectName(_fromUtf8("verticalLayout_18"))
        self.amplitude3 = QtGui.QSlider(self.layoutWidget_6)
        self.amplitude3.setMaximum(100)
        self.amplitude3.setPageStep(1)
        self.amplitude3.setSliderPosition(20)
        self.amplitude3.setOrientation(QtCore.Qt.Horizontal)
        self.amplitude3.setTickPosition(QtGui.QSlider.TicksBelow)
        self.amplitude3.setTickInterval(20)
        self.amplitude3.setObjectName(_fromUtf8("amplitude3"))
        self.verticalLayout_18.addWidget(self.amplitude3)
        self.label_28 = QtGui.QLabel(self.layoutWidget_6)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.verticalLayout_18.addWidget(self.label_28)
        self.label_29 = QtGui.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(230, 260, 81, 31))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.layoutWidget_7 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_7.setGeometry(QtCore.QRect(640, 420, 211, 59))
        self.layoutWidget_7.setObjectName(_fromUtf8("layoutWidget_7"))
        self.verticalLayout_19 = QtGui.QVBoxLayout(self.layoutWidget_7)
        self.verticalLayout_19.setMargin(0)
        self.verticalLayout_19.setObjectName(_fromUtf8("verticalLayout_19"))
        self.timeScaleModulated = QtGui.QSlider(self.layoutWidget_7)
        self.timeScaleModulated.setMaximum(6)
        self.timeScaleModulated.setPageStep(1)
        self.timeScaleModulated.setOrientation(QtCore.Qt.Horizontal)
        self.timeScaleModulated.setTickPosition(QtGui.QSlider.TicksBelow)
        self.timeScaleModulated.setTickInterval(1)
        self.timeScaleModulated.setObjectName(_fromUtf8("timeScaleModulated"))
        self.verticalLayout_19.addWidget(self.timeScaleModulated)
        self.label_30 = QtGui.QLabel(self.layoutWidget_7)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.verticalLayout_19.addWidget(self.label_30)
        self.timeShiftModulated = QtGui.QSlider(self.centralwidget)
        self.timeShiftModulated.setGeometry(QtCore.QRect(310, 380, 541, 29))
        self.timeShiftModulated.setAcceptDrops(False)
        self.timeShiftModulated.setMinimum(-16000)
        self.timeShiftModulated.setMaximum(16000)
        self.timeShiftModulated.setPageStep(1)
        self.timeShiftModulated.setTracking(True)
        self.timeShiftModulated.setOrientation(QtCore.Qt.Horizontal)
        self.timeShiftModulated.setTickPosition(QtGui.QSlider.TicksBelow)
        self.timeShiftModulated.setTickInterval(1000)
        self.timeShiftModulated.setObjectName(_fromUtf8("timeShiftModulated"))
        self.label_31 = QtGui.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(550, 420, 81, 31))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.layoutWidget_8 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_8.setGeometry(QtCore.QRect(890, 380, 126, 101))
        self.layoutWidget_8.setObjectName(_fromUtf8("layoutWidget_8"))
        self.verticalLayout_20 = QtGui.QVBoxLayout(self.layoutWidget_8)
        self.verticalLayout_20.setMargin(0)
        self.verticalLayout_20.setObjectName(_fromUtf8("verticalLayout_20"))
        self.reverseModulated = QtGui.QCheckBox(self.layoutWidget_8)
        self.reverseModulated.setObjectName(_fromUtf8("reverseModulated"))
        self.verticalLayout_20.addWidget(self.reverseModulated)
        self.label_32 = QtGui.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(860, 376, 51, 31))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.label_33 = QtGui.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(230, 420, 81, 31))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.label_34 = QtGui.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(20, 370, 121, 31))
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.layoutWidget_9 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_9.setGeometry(QtCore.QRect(310, 420, 161, 59))
        self.layoutWidget_9.setObjectName(_fromUtf8("layoutWidget_9"))
        self.verticalLayout_21 = QtGui.QVBoxLayout(self.layoutWidget_9)
        self.verticalLayout_21.setMargin(0)
        self.verticalLayout_21.setObjectName(_fromUtf8("verticalLayout_21"))
        self.amplitudeModulated = QtGui.QSlider(self.layoutWidget_9)
        self.amplitudeModulated.setMaximum(100)
        self.amplitudeModulated.setPageStep(1)
        self.amplitudeModulated.setSliderPosition(20)
        self.amplitudeModulated.setOrientation(QtCore.Qt.Horizontal)
        self.amplitudeModulated.setTickPosition(QtGui.QSlider.TicksBelow)
        self.amplitudeModulated.setTickInterval(20)
        self.amplitudeModulated.setObjectName(_fromUtf8("amplitudeModulated"))
        self.verticalLayout_21.addWidget(self.amplitudeModulated)
        self.label_35 = QtGui.QLabel(self.layoutWidget_9)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.verticalLayout_21.addWidget(self.label_35)
        self.label_36 = QtGui.QLabel(self.centralwidget)
        self.label_36.setGeometry(QtCore.QRect(230, 380, 81, 31))
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.layoutWidget_10 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_10.setGeometry(QtCore.QRect(640, 530, 211, 59))
        self.layoutWidget_10.setObjectName(_fromUtf8("layoutWidget_10"))
        self.verticalLayout_22 = QtGui.QVBoxLayout(self.layoutWidget_10)
        self.verticalLayout_22.setMargin(0)
        self.verticalLayout_22.setObjectName(_fromUtf8("verticalLayout_22"))
        self.timeScaleMixed = QtGui.QSlider(self.layoutWidget_10)
        self.timeScaleMixed.setMaximum(6)
        self.timeScaleMixed.setPageStep(1)
        self.timeScaleMixed.setOrientation(QtCore.Qt.Horizontal)
        self.timeScaleMixed.setTickPosition(QtGui.QSlider.TicksBelow)
        self.timeScaleMixed.setTickInterval(1)
        self.timeScaleMixed.setObjectName(_fromUtf8("timeScaleMixed"))
        self.verticalLayout_22.addWidget(self.timeScaleMixed)
        self.label_37 = QtGui.QLabel(self.layoutWidget_10)
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.verticalLayout_22.addWidget(self.label_37)
        self.timeShiftMixed = QtGui.QSlider(self.centralwidget)
        self.timeShiftMixed.setGeometry(QtCore.QRect(310, 490, 541, 29))
        self.timeShiftMixed.setAcceptDrops(False)
        self.timeShiftMixed.setMinimum(-16000)
        self.timeShiftMixed.setMaximum(16000)
        self.timeShiftMixed.setPageStep(1)
        self.timeShiftMixed.setTracking(True)
        self.timeShiftMixed.setOrientation(QtCore.Qt.Horizontal)
        self.timeShiftMixed.setTickPosition(QtGui.QSlider.TicksBelow)
        self.timeShiftMixed.setTickInterval(1000)
        self.timeShiftMixed.setObjectName(_fromUtf8("timeShiftMixed"))
        self.label_38 = QtGui.QLabel(self.centralwidget)
        self.label_38.setGeometry(QtCore.QRect(550, 530, 81, 31))
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.layoutWidget_11 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_11.setGeometry(QtCore.QRect(890, 490, 126, 101))
        self.layoutWidget_11.setObjectName(_fromUtf8("layoutWidget_11"))
        self.verticalLayout_23 = QtGui.QVBoxLayout(self.layoutWidget_11)
        self.verticalLayout_23.setMargin(0)
        self.verticalLayout_23.setObjectName(_fromUtf8("verticalLayout_23"))
        self.reverseMixed = QtGui.QCheckBox(self.layoutWidget_11)
        self.reverseMixed.setObjectName(_fromUtf8("reverseMixed"))
        self.verticalLayout_23.addWidget(self.reverseMixed)
        self.label_39 = QtGui.QLabel(self.centralwidget)
        self.label_39.setGeometry(QtCore.QRect(860, 486, 51, 31))
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.label_40 = QtGui.QLabel(self.centralwidget)
        self.label_40.setGeometry(QtCore.QRect(230, 530, 81, 31))
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.label_41 = QtGui.QLabel(self.centralwidget)
        self.label_41.setGeometry(QtCore.QRect(20, 490, 111, 31))
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.layoutWidget_12 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_12.setGeometry(QtCore.QRect(310, 530, 161, 61))
        self.layoutWidget_12.setObjectName(_fromUtf8("layoutWidget_12"))
        self.verticalLayout_24 = QtGui.QVBoxLayout(self.layoutWidget_12)
        self.verticalLayout_24.setMargin(0)
        self.verticalLayout_24.setObjectName(_fromUtf8("verticalLayout_24"))
        self.amplitudeMixed = QtGui.QSlider(self.layoutWidget_12)
        self.amplitudeMixed.setMaximum(100)
        self.amplitudeMixed.setPageStep(1)
        self.amplitudeMixed.setProperty("value", 20)
        self.amplitudeMixed.setOrientation(QtCore.Qt.Horizontal)
        self.amplitudeMixed.setTickPosition(QtGui.QSlider.TicksBelow)
        self.amplitudeMixed.setTickInterval(20)
        self.amplitudeMixed.setObjectName(_fromUtf8("amplitudeMixed"))
        self.verticalLayout_24.addWidget(self.amplitudeMixed)
        self.label_42 = QtGui.QLabel(self.layoutWidget_12)
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.verticalLayout_24.addWidget(self.label_42)
        self.label_43 = QtGui.QLabel(self.centralwidget)
        self.label_43.setGeometry(QtCore.QRect(230, 490, 81, 31))
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(640, 60, 211, 59))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.timeScale1 = QtGui.QSlider(self.layoutWidget1)
        self.timeScale1.setMaximum(6)
        self.timeScale1.setPageStep(1)
        self.timeScale1.setOrientation(QtCore.Qt.Horizontal)
        self.timeScale1.setTickPosition(QtGui.QSlider.TicksBelow)
        self.timeScale1.setTickInterval(1)
        self.timeScale1.setObjectName(_fromUtf8("timeScale1"))
        self.verticalLayout_2.addWidget(self.timeScale1)
        self.label_12 = QtGui.QLabel(self.layoutWidget1)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_2.addWidget(self.label_12)
        self.layoutWidget2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(890, 20, 126, 101))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_12.setMargin(0)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.mixing1 = QtGui.QCheckBox(self.layoutWidget2)
        self.mixing1.setObjectName(_fromUtf8("mixing1"))
        self.verticalLayout_12.addWidget(self.mixing1)
        self.modulation1 = QtGui.QCheckBox(self.layoutWidget2)
        self.modulation1.setObjectName(_fromUtf8("modulation1"))
        self.verticalLayout_12.addWidget(self.modulation1)
        self.reverse1 = QtGui.QCheckBox(self.layoutWidget2)
        self.reverse1.setObjectName(_fromUtf8("reverse1"))
        self.verticalLayout_12.addWidget(self.reverse1)
        self.layoutWidget3 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(310, 60, 161, 59))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.amplitude1 = QtGui.QSlider(self.layoutWidget3)
        self.amplitude1.setMaximum(100)
        self.amplitude1.setPageStep(1)
        self.amplitude1.setProperty("value", 20)
        self.amplitude1.setOrientation(QtCore.Qt.Horizontal)
        self.amplitude1.setTickPosition(QtGui.QSlider.TicksBelow)
        self.amplitude1.setTickInterval(20)
        self.amplitude1.setObjectName(_fromUtf8("amplitude1"))
        self.verticalLayout.addWidget(self.amplitude1)
        self.label_11 = QtGui.QLabel(self.layoutWidget3)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout.addWidget(self.label_11)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 610, 71, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 120, 1021, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 0, 1021, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 240, 1021, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(10, 360, 1021, 20))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(10, 480, 1021, 16))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(10, 590, 1021, 16))
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.line_7 = QtGui.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(0, 10, 20, 681))
        self.line_7.setFrameShape(QtGui.QFrame.VLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.line_8 = QtGui.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(10, 680, 1021, 20))
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.line_9 = QtGui.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(1020, 10, 20, 681))
        self.line_9.setFrameShape(QtGui.QFrame.VLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.layoutWidget4 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(110, 20, 92, 97))
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.select1 = QtGui.QPushButton(self.layoutWidget4)
        self.select1.setObjectName(_fromUtf8("select1"))
        self.verticalLayout_3.addWidget(self.select1)
        self.play1 = QtGui.QPushButton(self.layoutWidget4)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play1.setIcon(icon)
        self.play1.setObjectName(_fromUtf8("play1"))
        self.verticalLayout_3.addWidget(self.play1)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.stop1 = QtGui.QPushButton(self.layoutWidget4)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("images/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop1.setIcon(icon1)
        self.stop1.setObjectName(_fromUtf8("stop1"))
        self.verticalLayout_6.addWidget(self.stop1)
        self.layoutWidget5 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget5.setGeometry(QtCore.QRect(110, 140, 92, 97))
        self.layoutWidget5.setObjectName(_fromUtf8("layoutWidget5"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.select2 = QtGui.QPushButton(self.layoutWidget5)
        self.select2.setObjectName(_fromUtf8("select2"))
        self.verticalLayout_4.addWidget(self.select2)
        self.play2 = QtGui.QPushButton(self.layoutWidget5)
        self.play2.setIcon(icon)
        self.play2.setObjectName(_fromUtf8("play2"))
        self.verticalLayout_4.addWidget(self.play2)
        self.verticalLayout_7.addLayout(self.verticalLayout_4)
        self.stop2 = QtGui.QPushButton(self.layoutWidget5)
        self.stop2.setIcon(icon1)
        self.stop2.setObjectName(_fromUtf8("stop2"))
        self.verticalLayout_7.addWidget(self.stop2)
        self.layoutWidget6 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget6.setGeometry(QtCore.QRect(110, 260, 92, 97))
        self.layoutWidget6.setObjectName(_fromUtf8("layoutWidget6"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_8.setMargin(0)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.select3 = QtGui.QPushButton(self.layoutWidget6)
        self.select3.setObjectName(_fromUtf8("select3"))
        self.verticalLayout_5.addWidget(self.select3)
        self.play3 = QtGui.QPushButton(self.layoutWidget6)
        self.play3.setIcon(icon)
        self.play3.setObjectName(_fromUtf8("play3"))
        self.verticalLayout_5.addWidget(self.play3)
        self.verticalLayout_8.addLayout(self.verticalLayout_5)
        self.stop3 = QtGui.QPushButton(self.layoutWidget6)
        self.stop3.setIcon(icon1)
        self.stop3.setObjectName(_fromUtf8("stop3"))
        self.verticalLayout_8.addWidget(self.stop3)
        self.layoutWidget7 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget7.setGeometry(QtCore.QRect(110, 410, 87, 62))
        self.layoutWidget7.setObjectName(_fromUtf8("layoutWidget7"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.layoutWidget7)
        self.verticalLayout_9.setMargin(0)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.playModulated = QtGui.QPushButton(self.layoutWidget7)
        self.playModulated.setIcon(icon)
        self.playModulated.setObjectName(_fromUtf8("playModulated"))
        self.verticalLayout_9.addWidget(self.playModulated)
        self.stopModulated = QtGui.QPushButton(self.layoutWidget7)
        self.stopModulated.setIcon(icon1)
        self.stopModulated.setObjectName(_fromUtf8("stopModulated"))
        self.verticalLayout_9.addWidget(self.stopModulated)
        self.layoutWidget8 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget8.setGeometry(QtCore.QRect(110, 520, 87, 62))
        self.layoutWidget8.setObjectName(_fromUtf8("layoutWidget8"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.layoutWidget8)
        self.verticalLayout_10.setMargin(0)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.playMixed = QtGui.QPushButton(self.layoutWidget8)
        self.playMixed.setIcon(icon)
        self.playMixed.setObjectName(_fromUtf8("playMixed"))
        self.verticalLayout_10.addWidget(self.playMixed)
        self.stopMixed = QtGui.QPushButton(self.layoutWidget8)
        self.stopMixed.setIcon(icon1)
        self.stopMixed.setObjectName(_fromUtf8("stopMixed"))
        self.verticalLayout_10.addWidget(self.stopMixed)
        self.layoutWidget9 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget9.setGeometry(QtCore.QRect(110, 610, 91, 29))
        self.layoutWidget9.setObjectName(_fromUtf8("layoutWidget9"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget9)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.record = QtGui.QPushButton(self.layoutWidget9)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("images/record.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.record.setIcon(icon2)
        self.record.setObjectName(_fromUtf8("record"))
        self.horizontalLayout.addWidget(self.record)
        self.label_44 = QtGui.QLabel(self.centralwidget)
        self.label_44.setGeometry(QtCore.QRect(230, 610, 81, 31))
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.layoutWidget_13 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_13.setGeometry(QtCore.QRect(310, 610, 161, 59))
        self.layoutWidget_13.setObjectName(_fromUtf8("layoutWidget_13"))
        self.verticalLayout_25 = QtGui.QVBoxLayout(self.layoutWidget_13)
        self.verticalLayout_25.setMargin(0)
        self.verticalLayout_25.setObjectName(_fromUtf8("verticalLayout_25"))
        self.amplitudeRecord = QtGui.QSlider(self.layoutWidget_13)
        self.amplitudeRecord.setMaximum(100)
        self.amplitudeRecord.setPageStep(1)
        self.amplitudeRecord.setProperty("value", 20)
        self.amplitudeRecord.setOrientation(QtCore.Qt.Horizontal)
        self.amplitudeRecord.setTickPosition(QtGui.QSlider.TicksBelow)
        self.amplitudeRecord.setTickInterval(20)
        self.amplitudeRecord.setObjectName(_fromUtf8("amplitudeRecord"))
        self.verticalLayout_25.addWidget(self.amplitudeRecord)
        self.label_45 = QtGui.QLabel(self.layoutWidget_13)
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.verticalLayout_25.addWidget(self.label_45)
        self.layoutWidget_14 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_14.setGeometry(QtCore.QRect(890, 620, 126, 41))
        self.layoutWidget_14.setObjectName(_fromUtf8("layoutWidget_14"))
        self.verticalLayout_26 = QtGui.QVBoxLayout(self.layoutWidget_14)
        self.verticalLayout_26.setMargin(0)
        self.verticalLayout_26.setObjectName(_fromUtf8("verticalLayout_26"))
        self.reverseRecord = QtGui.QCheckBox(self.layoutWidget_14)
        self.reverseRecord.setObjectName(_fromUtf8("reverseRecord"))
        self.verticalLayout_26.addWidget(self.reverseRecord)
        self.saveRecord = QtGui.QPushButton(self.centralwidget)
        self.saveRecord.setGeometry(QtCore.QRect(20, 650, 85, 27))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("images/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveRecord.setIcon(icon3)
        self.saveRecord.setObjectName(_fromUtf8("saveRecord"))
        self.label_46 = QtGui.QLabel(self.centralwidget)
        self.label_46.setGeometry(QtCore.QRect(550, 610, 81, 31))
        self.label_46.setObjectName(_fromUtf8("label_46"))
        self.layoutWidget_15 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_15.setGeometry(QtCore.QRect(640, 610, 211, 59))
        self.layoutWidget_15.setObjectName(_fromUtf8("layoutWidget_15"))
        self.verticalLayout_27 = QtGui.QVBoxLayout(self.layoutWidget_15)
        self.verticalLayout_27.setMargin(0)
        self.verticalLayout_27.setObjectName(_fromUtf8("verticalLayout_27"))
        self.timeScaleRecord = QtGui.QSlider(self.layoutWidget_15)
        self.timeScaleRecord.setMaximum(6)
        self.timeScaleRecord.setPageStep(1)
        self.timeScaleRecord.setOrientation(QtCore.Qt.Horizontal)
        self.timeScaleRecord.setTickPosition(QtGui.QSlider.TicksBelow)
        self.timeScaleRecord.setTickInterval(1)
        self.timeScaleRecord.setObjectName(_fromUtf8("timeScaleRecord"))
        self.verticalLayout_27.addWidget(self.timeScaleRecord)
        self.label_47 = QtGui.QLabel(self.layoutWidget_15)
        self.label_47.setObjectName(_fromUtf8("label_47"))
        self.verticalLayout_27.addWidget(self.label_47)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(110, 650, 178, 29))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.playRecord = QtGui.QPushButton(self.widget)
        self.playRecord.setIcon(icon)
        self.playRecord.setObjectName(_fromUtf8("playRecord"))
        self.horizontalLayout_2.addWidget(self.playRecord)
        self.stopRecord = QtGui.QPushButton(self.widget)
        self.stopRecord.setIcon(icon1)
        self.stopRecord.setObjectName(_fromUtf8("stopRecord"))
        self.horizontalLayout_2.addWidget(self.stopRecord)
#        WaveMixer.setCentralWidget(self.centralwidget)

        #       Bind all changing value to func change

        #-----------------Horizontal Sliders--------------------------
        #time shift
        self.timeShift1.valueChanged.connect(self.change)
        self.timeShift2.valueChanged.connect(self.change)
        self.timeShift3.valueChanged.connect(self.change)
        self.timeShiftModulated.valueChanged.connect(self.change)
        self.timeShiftMixed.valueChanged.connect(self.change)

        #time scale
        self.timeScale1.valueChanged.connect(self.change)
        self.timeScale2.valueChanged.connect(self.change)
        self.timeScale3.valueChanged.connect(self.change)
        self.timeScaleModulated.valueChanged.connect(self.change)
        self.timeScaleMixed.valueChanged.connect(self.change)
        self.timeScaleRecord.valueChanged.connect(self.change)

        #amplitude
        self.amplitude1.valueChanged.connect(self.change)
        self.amplitude2.valueChanged.connect(self.change)
        self.amplitude3.valueChanged.connect(self.change)
        self.amplitudeModulated.valueChanged.connect(self.change)
        self.amplitudeMixed.valueChanged.connect(self.change)
        self.amplitudeRecord.valueChanged.connect(self.change)
        
         #-----------------Check Boxes---------------------------------
        #reverse
        self.reverse1.stateChanged.connect(self.change)
        self.reverse2.stateChanged.connect(self.change)
        self.reverse3.stateChanged.connect(self.change)
        self.reverseModulated.stateChanged.connect(self.change)
        self.reverseMixed.stateChanged.connect(self.change)
        self.reverseRecord.stateChanged.connect(self.change)

        #modulation
        self.modulation1.stateChanged.connect(self.change)
        self.modulation2.stateChanged.connect(self.change)
        self.modulation3.stateChanged.connect(self.change)

        #mixing
        self.mixing1.stateChanged.connect(self.change)
        self.mixing2.stateChanged.connect(self.change)
        self.mixing3.stateChanged.connect(self.change)

#       Bind all button to respective function

        #-----------------Buttons---------------------------------

        #play buttons
        self.play1.clicked.connect(self.play_1)
        self.play2.clicked.connect(self.play_2)
        self.play3.clicked.connect(self.play_3)
        self.playModulated.clicked.connect(self.play_modulated)
        self.playMixed.clicked.connect(self.play_mixed)
        self.playRecord.clicked.connect(self.play_recorded)

        #stop buttons     
        self.stop1.clicked.connect(self.stop_1)
        self.stop2.clicked.connect(self.stop_2)
        self.stop3.clicked.connect(self.stop_3)
        self.stopModulated.clicked.connect(self.stop_modulated)
        self.stopMixed.clicked.connect(self.stop_mixed)
        self.stopRecord.clicked.connect(self.stop_recorded)

        #select buttons     
        self.select1.clicked.connect(self.select_1)
        self.select2.clicked.connect(self.select_2)
        self.select3.clicked.connect(self.select_3)

        #save button  
        self.saveRecord.clicked.connect(self.save_recorded)

        #record button     
        self.record.clicked.connect(self.record_file)

        self.retranslateUi(WaveMixer)
        QtCore.QObject.connect(self.timeShift1, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_2.setNum)
        QtCore.QMetaObject.connectSlotsByName(WaveMixer)

    def retranslateUi(self, WaveMixer):
        WaveMixer.setWindowTitle(_translate("WaveMixer", "Wave Mixer v1.0", None))
        self.label.setText(_translate("WaveMixer", "Wave 1", None))
        self.label_2.setText(_translate("WaveMixer", "0", None))
        self.label_3.setText(_translate("WaveMixer", "Time Shift", None))
        self.label_7.setText(_translate("WaveMixer", "Amplitude", None))
        self.label_9.setText(_translate("WaveMixer", "Time Scale", None))
        self.label_16.setText(_translate("WaveMixer", " 0     1/8    1/4   1/2    2        4       8", None))
        self.label_10.setText(_translate("WaveMixer", "Time Scale", None))
        self.mixing2.setText(_translate("WaveMixer", "Mixing", None))
        self.modulation2.setText(_translate("WaveMixer", "Modulation", None))
        self.reverse2.setText(_translate("WaveMixer", "Time Reversal", None))
        self.label_6.setText(_translate("WaveMixer", "0", None))
        self.label_8.setText(_translate("WaveMixer", "Amplitude", None))
        self.label_18.setText(_translate("WaveMixer", "Wave 2", None))
        self.label_20.setText(_translate("WaveMixer", " 0      1      2      3      4      5", None))
        self.label_21.setText(_translate("WaveMixer", "Time Shift", None))
        self.label_22.setText(_translate("WaveMixer", " 0     1/8    1/4   1/2    2        4       8", None))
        self.label_23.setText(_translate("WaveMixer", "Time Scale", None))
        self.mixing3.setText(_translate("WaveMixer", "Mixing", None))
        self.modulation3.setText(_translate("WaveMixer", "Modulation", None))
        self.reverse3.setText(_translate("WaveMixer", "Time Reversal", None))
        self.label_25.setText(_translate("WaveMixer", "0", None))
        self.label_26.setText(_translate("WaveMixer", "Amplitude", None))
        self.label_27.setText(_translate("WaveMixer", "Wave 3", None))
        self.label_28.setText(_translate("WaveMixer", " 0      1      2      3      4      5", None))
        self.label_29.setText(_translate("WaveMixer", "Time Shift", None))
        self.label_30.setText(_translate("WaveMixer", " 0     1/8    1/4   1/2    2        4       8", None))
        self.label_31.setText(_translate("WaveMixer", "Time Scale", None))
        self.reverseModulated.setText(_translate("WaveMixer", "Time Reversal", None))
        self.label_32.setText(_translate("WaveMixer", "0", None))
        self.label_33.setText(_translate("WaveMixer", "Amplitude", None))
        self.label_34.setText(_translate("WaveMixer", "Modulated Wave ", None))
        self.label_35.setText(_translate("WaveMixer", " 0      1      2      3      4      5", None))
        self.label_36.setText(_translate("WaveMixer", "Time Shift", None))
        self.label_37.setText(_translate("WaveMixer", " 0     1/8    1/4   1/2    2        4       8", None))
        self.label_38.setText(_translate("WaveMixer", "Time Scale", None))
        self.reverseMixed.setText(_translate("WaveMixer", "Time Reversal", None))
        self.label_39.setText(_translate("WaveMixer", "0", None))
        self.label_40.setText(_translate("WaveMixer", "Amplitude", None))
        self.label_41.setText(_translate("WaveMixer", "Mixed Wave", None))
        self.label_42.setText(_translate("WaveMixer", " 0      1      2      3      4      5", None))
        self.label_43.setText(_translate("WaveMixer", "Time Shift", None))
        self.label_12.setText(_translate("WaveMixer", " 0     1/8    1/4   1/2    2        4       8", None))
        self.mixing1.setText(_translate("WaveMixer", "Mixing", None))
        self.modulation1.setText(_translate("WaveMixer", "Modulation", None))
        self.reverse1.setText(_translate("WaveMixer", "Time Reversal", None))
        self.label_11.setText(_translate("WaveMixer", " 0      1      2      3      4      5", None))
        self.label_4.setText(_translate("WaveMixer", "Recording", None))
        self.select1.setText(_translate("WaveMixer", "Select File", None))
        self.play1.setText(_translate("WaveMixer", "Play", None))
        self.stop1.setText(_translate("WaveMixer", "Stop", None))
        self.select2.setText(_translate("WaveMixer", "Select File", None))
        self.play2.setText(_translate("WaveMixer", "Play", None))
        self.stop2.setText(_translate("WaveMixer", "Stop", None))
        self.select3.setText(_translate("WaveMixer", "Select File", None))
        self.play3.setText(_translate("WaveMixer", "Play", None))
        self.stop3.setText(_translate("WaveMixer", "Stop", None))
        self.playModulated.setText(_translate("WaveMixer", "Play", None))
        self.stopModulated.setText(_translate("WaveMixer", "Stop", None))
        self.playMixed.setText(_translate("WaveMixer", "Play", None))
        self.stopMixed.setText(_translate("WaveMixer", "Stop", None))
        self.record.setText(_translate("WaveMixer", "Record", None))
        self.label_44.setText(_translate("WaveMixer", "Amplitude", None))
        self.label_45.setText(_translate("WaveMixer", " 0      1      2      3      4      5", None))
        self.reverseRecord.setText(_translate("WaveMixer", "Time Reversal", None))
        self.saveRecord.setText(_translate("WaveMixer", "Save", None))
        self.label_46.setText(_translate("WaveMixer", "Time Scale", None))
        self.label_47.setText(_translate("WaveMixer", " 0     1/8    1/4   1/2    2        4       8", None))
        self.playRecord.setText(_translate("WaveMixer", "Play", None))
        self.stopRecord.setText(_translate("WaveMixer", "Stop", None))

    def change(self,val):
        print val 

        self.wave1.ampFactor=self.amplitude1.value()/20.0
        self.wave2.ampFactor=self.amplitude2.value()/20.0
        self.wave3.ampFactor=self.amplitude3.value()/20.0
        self.waveModulated.ampFactor=self.amplitudeModulated.value()/20.0
        self.waveMixed.ampFactor=self.amplitudeMixed.value()/20.0
        self.waveRecorded.ampFactor=self.amplitudeRecord.value()/20.0

        self.wave1.timeShiftFactor=self.timeShift1.value()
        self.wave2.timeShiftFactor=self.timeShift2.value()
        self.wave3.timeShiftFactor=self.timeShift3.value()
        self.waveModulated.timeShiftFactor=self.timeShiftModulated.value()
        self.waveMixed.timeShiftFactor=self.timeShiftMixed.value()

        self.wave1.timeScaleFactor=timeScaleValue[self.timeScale1.value()]
        self.wave2.timeScaleFactor=timeScaleValue[self.timeScale2.value()]
        self.wave3.timeScaleFactor=timeScaleValue[self.timeScale3.value()]
        self.waveModulated.timeScaleFactor=timeScaleValue[self.timeScaleModulated.value()]
        self.waveMixed.timeScaleFactor=timeScaleValue[self.timeScaleMixed.value()]
        self.waveRecorded.timeScaleFactor=timeScaleValue[self.timeScaleRecord.value()]

        self.wave1.reverse=state[self.reverse1.checkState()]
        self.wave2.reverse=state[self.reverse2.checkState()]
        self.wave3.reverse=state[self.reverse3.checkState()]
        self.waveModulated.reverse=state[self.reverseModulated.checkState()]
        self.waveMixed.reverse=state[self.reverseMixed.checkState()]
        self.waveRecorded.reverse=state[self.reverseRecord.checkState()]

        self.wave1.modulateFlag=state[self.modulation1.checkState()]
        self.wave2.modulateFlag=state[self.modulation2.checkState()]
        self.wave3.modulateFlag=state[self.modulation3.checkState()]

        self.wave1.mixFlag=state[self.mixing1.checkState()]
        self.wave2.mixFlag=state[self.mixing2.checkState()]
        self.wave3.mixFlag=state[self.mixing3.checkState()]

    def play_1(self):
        self.wave1.apply_changes()
        self.io.make_wave("wave1.wav",self.wave1)
	if self.wave1.fPtr:
		self.wave1.fPtr.close()
        self.wave1.fPtr = wave.open("wave1.wav", 'rb')
        self.wave1.play_wave()
        self.wave1.stream.start_stream()
        print "play1"

    def play_2(self):
        self.wave2.apply_changes()
	if self.wave2.fPtr:
		self.wave2.fPtr.close()        
        self.io.make_wave("wave2.wav",self.wave2)
        self.wave2.fPtr = wave.open("wave2.wav", 'rb')
        self.wave2.play_wave()
        self.wave2.stream.start_stream()
        print "play2"

    def play_3(self):
        self.wave3.apply_changes()
        if self.wave3.fPtr:
		self.wave3.fPtr.close()
        self.io.make_wave("wave3.wav",self.wave3)
        self.wave3.fPtr = wave.open("wave3.wav", 'rb')
        self.wave3.play_wave()
        self.wave3.stream.start_stream()
        print "play3"

    def play_modulated(self):
        if not self.wave1.modulateFlag:
            self.wave1.pcmData=[1]
            self.wave1.length=1
        else:
            self.wave1.apply_changes()

        if not self.wave2.modulateFlag:
            self.wave2.pcmData=[1]
            self.wave2.length=1
        else:
            self.wave2.apply_changes()

        if not self.wave3.modulateFlag:
            self.wave3.pcmData=[1]
            self.wave3.length=1
        else:
            self.wave3.apply_changes()
        self.waveModulated. modulation_or_mixing(0,self.wave1,self.wave2,self.wave3)
        self.waveModulated.apply_changes()
        if self.waveModulated.fPtr:
		self.waveModulated.fPtr.close()
        self.io.make_wave("waveModulated.wav",self.waveModulated)
        self.waveModulated.fPtr = wave.open("waveModulated.wav", 'rb')
        self.waveModulated.play_wave()
        self.waveModulated.stream.start_stream()
        print "playModulated"

    def play_mixed(self):
        if not self.wave1.mixFlag:
            self.wave1.pcmData=[0]
            self.wave1.length=1
        else:
            self.wave1.apply_changes()

        if not self.wave2.mixFlag:
            self.wave2.pcmData=[0]
            self.wave2.length=1
        else:
            self.wave2.apply_changes()

        if not self.wave3.mixFlag:
            self.wave3.pcmData=[0]
            self.wave3.length=1
        else:
            self.wave3.apply_changes()

        self.waveMixed. modulation_or_mixing(1,self.wave1,self.wave2,self.wave3)
        self.waveMixed.apply_changes()
        if self.waveMixed.fPtr:
		self.waveMixed.fPtr.close()
        self.io.make_wave("waveMixed.wav",self.waveMixed)
        self.waveMixed.fPtr = wave.open("waveMixed.wav", 'rb')
        self.waveMixed.play_wave()
        self.waveMixed.stream.start_stream()
        print "playMixed"

    def play_recorded(self):
        if not self.waveRecorded.fileName:
            self.waveRecorded.fileName="waveRecorded.wav"
        if self.waveRecorded.recordFlag:
            self.waveRecorded.recordFlag=False
            self.io.save_recorded(self.waveRecorded.fileName,self.waveRecorded)
        self.io.read_wave(self.waveRecorded.fileName,self.waveRecorded)
        self.waveRecorded.apply_changes()
        self.io.make_wave("waveRecorded.wav",self.waveRecorded)
        if self.waveRecorded.fPtr:
		self.waveRecorded.fPtr.close()
        self.waveRecorded.fPtr = wave.open("waveRecorded.wav", 'rb')
        self.waveRecorded.play_wave()
        self.waveRecorded.stream.start_stream()
        print "playRecorded"

    def stop_1(self):
        self.wave1.stop_playing()
        print "stop1"

    def stop_2(self):
        self.wave2.stop_playing()
        print "stop2"

    def stop_3(self):
        self.wave3.stop_playing()
        print "stop3"

    def stop_modulated(self):
        self.waveModulated.stop_playing()
        print "stopModulated"

    def stop_mixed(self):
        self.waveMixed.stop_playing()
        print "stopMixed"

    def stop_recorded(self):
        if self.waveRecorded.recordFlag:
            self.waveRecorded.stop_recording()
            if not self.waveRecorded.fileName:
                self.waveRecorded.fileName="waveRecorded.wav"
            self.io.save_recorded(self.waveRecorded.fileName,self.waveRecorded)
            self.io.read_wave(self.waveRecorded.fileName,self.waveRecorded)
            self.waveRecorded.apply_changes()
            self.io.make_wave(self.waveRecorded.fileName,self.waveRecorded)
        if self.waveRecorded.playFlag:
            self.waveRecorded.stop_playing()
        print "stopRecorded"

    def select_1(self):
        self.wave1.fileName=str(QtGui.QFileDialog.getOpenFileName(None,'Select file'))
        print self.wave1.fileName
        if(self.wave1.fileName):
            self.io.read_wave(self.wave1.fileName,self.wave1)
        else:
            print "Please Select a File"
        print self.wave1.fileName

    def select_2(self):
        self.wave2.fileName=str(QtGui.QFileDialog.getOpenFileName(None,'Select file'))
        print self.wave2.fileName
        if(self.wave2.fileName):
            self.io.read_wave(self.wave2.fileName,self.wave2)
        else:
            print "Please Select a File"
        print self.wave2.fileName

    def select_3(self):
        self.wave3.fileName=str(QtGui.QFileDialog.getOpenFileName(None,'Select file'))
        print self.wave3.fileName
        if(self.wave3.fileName):
            self.io.read_wave(self.wave3.fileName,self.wave3)
        else:
            print "Please Select a File"
        print self.wave3.fileName

    def save_recorded(self):
        self.waveRecorded.fileName=str(QtGui.QFileDialog.getSaveFileName(None,'Select file'))
        print self.waveRecorded.fileName
        if(self.waveRecorded.fileName):
            if self.waveRecorded.recordFlag:
                self.waveRecorded.stop_recording()
                self.io.save_recorded(self.waveRecorded.fileName,self.waveRecorded)
            self.io.read_wave(self.waveRecorded.fileName,self.waveRecorded)
            self.waveRecorded.apply_changes()
            self.io.make_wave(self.waveRecorded.fileName,self.waveRecorded)
        else:
            print "Please Select a File"

    def record_file(self):
        self.waveRecorded.recordFlag=True
        self.waveRecorded.record_wave()
        print "recoding saved"

