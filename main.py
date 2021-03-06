from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from langauges import Languages,Trans

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 589)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons8-translation-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.TextInput = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(11)
        self.TextInput.setFont(font)
        self.TextInput.setObjectName("TextInput")
        self.gridLayout.addWidget(self.TextInput, 0, 0, 1, 1)
        self.TextOutput = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.TextOutput.setFont(font)
        self.TextOutput.setObjectName("TextOutput")
        self.gridLayout.addWidget(self.TextOutput, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 797, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon1)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon2)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("save_as.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_as.setIcon(icon4)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon5)
        self.actionExit.setObjectName("actionExit")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon6)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon7)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCut = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon8)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon9)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon10)
        self.actionPaste.setObjectName("actionPaste")
        self.actionHow_to = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons8-help-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHow_to.setIcon(icon11)
        self.actionHow_to.setObjectName("actionHow_to")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon12)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSave_translation = QtWidgets.QAction(MainWindow)
        self.actionSave_translation.setIcon(icon)
        self.actionSave_translation.setObjectName("actionSave_translation")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionSave_translation)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuHelp.addAction(self.actionHow_to)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionSave_as)
        self.toolBar.addAction(self.actionSave_translation)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionRedo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionHow_to)
        self.toolBar.addAction(self.actionAbout)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)
        self.addLangList()
        self.Trans = Trans()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.NewFileFlag = True
        self.Saved = False
        self.TransNew = True
        self.TranSaved = False
        self.actionOpen.triggered.connect(self.openFile)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionNew.triggered.connect(self.newFile)
        self.actionSave_as.triggered.connect(self.saveAsFile)
        self.actionExit.triggered.connect(self.exitApp)
       	self.TextInput.textChanged.connect(self.unsaved)
       	self.TextInput.textChanged.connect(self.wordCheck)
       	self.actionUndo.triggered.connect(self.undo)
       	self.actionRedo.triggered.connect(self.redo)
       	self.actionCut.triggered.connect(self.cut)
       	self.actionCopy.triggered.connect(self.copy)
       	self.actionPaste.triggered.connect(self.paste)
       	self.TranslateBtn.clicked.connect(self.translateData)
       	self.actionSave_translation.triggered.connect(self.saveTranslation)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Jtranslate"))
        self.TextInput.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft JhengHei UI\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionSave_as.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Shift+Z"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionHow_to.setText(_translate("MainWindow", "How to"))
        self.actionHow_to.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionSave_translation.setText(_translate("MainWindow", "Save translation"))
        self.actionSave_translation.setShortcut(_translate("MainWindow", "Ctrl+Q"))
    def addLangList(self):
    	self.SrcLangList = QComboBox()
    	self.SrcLabel = QLabel('  Src : ')
    	self.Destlabel = QLabel('   Dest : ')
    	self.TranslateBtn = QPushButton('',MainWindow)
    	self.DestLangList = QComboBox()
    	self.sep = QLabel('  | ')
    	self.LangList = Languages()
    	self.LangList = self.LangList.getLanguages()
    	self.SrcLangList.addItem('auto')
    	for i in self.LangList:
    		self.SrcLangList.addItem(i)
    		self.DestLangList.addItem(i)
    	self.toolBar.addWidget(self.SrcLabel)
    	self.toolBar.addWidget(self.SrcLangList)
    	self.toolBar.addWidget(self.Destlabel)
    	self.toolBar.addWidget(self.DestLangList)
    	self.toolBar.addWidget(self.sep)
    	self.toolBar.addWidget(self.TranslateBtn)
    	self.TranslateBtn.setIcon(QIcon('icons8-refresh-26.png'))
    def newFile(self):
    	data = self.TextInput.toPlainText()
    	if(data!=''):
    		SaveOption = QMessageBox.question(MainWindow,'Unsaved file','Do you want to save the file?',QMessageBox.Save|QMessageBox.Discard|QMessageBox.Cancel,QMessageBox.Save)
    		if(SaveOption==QMessageBox.Save):
    			self.saveFile()
    			if(self.Saved):
    				self.fname=""
		    		self.TextInput.setText("")
		    		self.TextOutput.setText("")
		    		self.NewFileFlag = True
		    	else:
		    		pass
    		elif(SaveOption==QMessageBox.Discard):
		    	self.fname=""
		    	self.TextInput.setText("")
		    	self.NewFileFlag = True
    		else:
		    	pass
    def openFile(self):
    	try:
	    	fname = QFileDialog.getOpenFileName(MainWindow,'Open a file',"","Text files(*.txt)")
	    	if(fname[0]!=''):
	    		self.fname = fname
		    	print('File opened : ',self.fname[0])
		    	file = open(self.fname[0],'r+',encoding='utf-8')
		    	data = file.read()
		    	self.TextInput.setText(data)
		    	self.NewFileFlag = False
		    	file.close()
		    	print(self.fname)
    	except:
	    	pass
    def saveFile(self):
    	data = self.TextInput.toPlainText()
    	if(self.NewFileFlag):
    		try:
		    	self.fname = QFileDialog.getSaveFileName(MainWindow,'Save file',"","Text files(*.txt)")
		    	if(self.fname[0]!=''):
			    	print(self.fname[0])
			    	file = open(self.fname[0],'w+')
			    	file.write(data)
			    	file.close()
			    	self.NewFileFlag = False
			    	self.Saved = True
		    	else:
			    	self.Saved = False
    		except Exception as error:
    			print('File saving error : ',error)
		    	pass
    	else:
	    	file = open(self.fname[0],'w+')
	    	file.write(data)
	    	file.close()
    		self.Saved = True
    def saveAsFile(self):
    	data = self.TextInput.toPlainText()
    	try:
	    	self.fnameAs = QFileDialog.getSaveFileName(MainWindow,'Save as file',"","Text files(*.txt)")
	    	print(self.fnameAs[0])
	    	file = open(self.fnameAs[0],'w+')
	    	file.write(data)
	    	file.close()
	    	self.NewFileFlag = False
    	except:
	    	pass
    def exitApp(self):
        if(not self.Saved):
            ExitOption = QMessageBox.question(MainWindow,'Unsaved file','Do you want to save the file?',QMessageBox.Save|QMessageBox.Discard|QMessageBox.Cancel,QMessageBox.Save)
            if(ExitOption==QMessageBox.Save):
            	self.saveFile()
            	if(self.Saved):
            		app.exit()
            elif(ExitOption==QMessageBox.Discard):
            	app.exit()
            else:
            	pass
        else:
            app.exit()
    def unsaved(self):
    	self.Saved = False
    def undo(self):
    	self.TextInput.undo()
    def redo(self):
    	self.TextInput.redo()
    def cut(self):
    	self.TextInput.cut()
    def copy(self):
    	self.TextInput.copy()
    def paste(self):
    	self.TextInput.paste()
    def translateData(self):
    	self.SrcLang = self.SrcLangList.currentText()
    	self.DestLang = self.DestLangList.currentText()
    	Data = self.TextInput.toPlainText()
    	self.TransData = self.Trans.translate(src=self.SrcLang,dest=self.DestLang,data=Data)
    	if(self.TransData==None):
    		QMessageBox.critical(MainWindow,'Network Error!','Bad network connection!')
    	else:
    		self.TextOutput.setText(self.TransData)
    def saveTranslation(self):
    	data = self.TextOutput.toPlainText()
    	if(self.TransNew):
    		try:
    			TransFname = QFileDialog.getSaveFileName(MainWindow,'Save Translation',"","Text file(*.txt)")
    			if(TransFname!=''):
    				self.TransFname = TransFname
    				file = open(self.TransFname[0],'w',encoding='utf-8')
    				file.write(data)
    				file.close()
    				self.TranSaved = True
    				self.TransNew = False

    		except Exception as error:
    			print('File saving error! : ',error)
    	else:
    		try:
    			file = open(self.TransFname[0],'w',encoding='utf-8')
    			file.write(data)
    			file.close()
    			self.TranSaved = True
    		except Exception as Error:
    			print('File saving error! : ',error)
    def wordCheck(self):
    	data = self.TextInput.toPlainText()
    	lenStr = len(data)
    	if(lenStr==0):
    		pass
    	else:
    		if(data[-1]=='.'):
    			self.translateData()
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
	def exitApp(self,ui):
		if(not ui.Saved):
			ExitOption = QMessageBox.question(MainWindow,'Unsaved file','Do you want to save the file?',QMessageBox.Save|QMessageBox.Discard,QMessageBox.Save)
			if(ExitOption==QMessageBox.Save):
				ui.saveFile()
				ui.saveTranslation()
				if(ui.Saved):
					app.exit()
			elif(ExitOption==QMessageBox.Discard):
				app.exit()
			else:
				print('Cancel')
	def closeEvent(self,event):
		self.exitApp(ui)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
