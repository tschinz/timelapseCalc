#!/usr/bin/env python
# filename:          gui.py
# kind:              Python file
# first created:     14.08.2011
# created by:        zas
# last edited:       14.08.2011
# last change by:    zas
#
################################################################################
# History:
#
# v0.1 : zas 14.08.2011
#
################################################################################
# Description: 
# GUI to Calculate TimeLapse Video parameters (Zeitraffer Video)
################################################################################
# Installation: 
# Module : python26 ,pyqt4
# Linux  : sudo apt-get install python2.6 python-qt4
################################################################################
__author__ = "Zahno Silvan"
__date__   = "14.08.2011"

################################################################################
# Import modules
#
import sys, os
import PyQt4
from PyQt4 import QtGui, Qt
from PyQt4 import QtCore

################################################################################
# Constants
#
indent = '  '
windowsize = (700,600)

fps_values = ["8", "12", "15", "23", "24", "25", "30", "60"]
units      = ["second(s)", "minute(s)", "hour(s)", "day(s)", "second(s)/picture", "minute(s)/picture", "hour(s)/picture", "day(s)/picture"]

################################################################################
# Define gui class
#
class MainUI(QtGui.QMainWindow):
    
    def __init__(self, win_parent = None):
        # Init the base class
        QtGui.QMainWindow.__init__(self, win_parent)
        self.init_UI()
    #=============================================================================
    # Function definitions of class
    #
    
    #-----------------------------------------------------------------------------
    # initialise UI
    # 
    def init_UI(self):
        # variable
        self.verbosity = 0
        
        ####
        # Toolbar
        #
        self.run = QtGui.QAction(QtGui.QIcon('icons/run.png'), 'Run Script', self)
        self.run.setShortcut('Ctrl+R')
        self.connect(self.run, QtCore.SIGNAL('triggered()'), self.exe)
        
        self.rst = QtGui.QAction(QtGui.QIcon('icons/reset.png'), 'Reset Fields', self)
        self.rst.setShortcut('Ctrl+Shift+R')
        self.connect(self.rst, QtCore.SIGNAL('triggered()'), self.reset)
        
        self.info = QtGui.QAction(QtGui.QIcon('icons/info.png'), 'Info', self)
        self.info.setShortcut('Ctrl+Q')
        self.connect(self.info, QtCore.SIGNAL('triggered()'), self.displayInfo)
        
        self.help = QtGui.QAction(QtGui.QIcon('icons/help.png'), 'Help', self)
        self.help.setShortcut('Ctrl+H')
        self.connect(self.help, QtCore.SIGNAL('triggered()'), self.displayHelp)
        
        self.exit = QtGui.QAction(QtGui.QIcon('icons/exit.png'), 'Exit', self)
        self.exit.setShortcut('Ctrl+Q')
        self.connect(self.exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        
        # Create Toolbar
        self.toolbar = self.addToolBar('Actions')
        self.toolbar.addAction(self.run)
        self.toolbar.addAction(self.rst)
        self.toolbar.addAction(self.help)
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(self.info)
        self.toolbar.addAction(self.exit)
        
        self.displayMainContent()
        
    # END init_UI
    
    #-----------------------------------------------------------------------------
    # Display Main Content of the program
    #
    def displayMainContent(self):
        ####
        # Widgets
        #
        # Title label
        self.script_label = QtGui.QLabel("Time Lapse Video Parameter Calculator - TLVPCalc")
        
        # Input Parameters
        #self.input_fps_cb = QtGui.QCheckBox()
        self.input_pic_interval_cb = QtGui.QCheckBox()
        self.input_pictime_cb = QtGui.QCheckBox()
        self.input_playback_cb = QtGui.QCheckBox()
        self.input_nbrofpic_cb = QtGui.QCheckBox()
        
        self.input_fps_label     = QtGui.QLabel("Framerate:")
        self.input_fps_edit      = QtGui.QComboBox()
        self.input_fps_edit.insertItem(0, fps_values[0])
        self.input_fps_edit.insertItem(1, fps_values[1])
        self.input_fps_edit.insertItem(2, fps_values[2])
        self.input_fps_edit.insertItem(3, fps_values[3])
        self.input_fps_edit.insertItem(4, fps_values[4])
        self.input_fps_edit.insertItem(5, fps_values[5])
        self.input_fps_edit.insertItem(6, fps_values[6])
        self.input_fps_edit.insertItem(7, fps_values[7])
        self.input_fps_edit.setCurrentIndex(6)
        self.input_fps_label_fps = QtGui.QLabel("fps")
		
        self.input_pic_interval_label = QtGui.QLabel("Picture interval:")
        self.input_pic_interval_edit  = QtGui.QLineEdit("")
        self.input_pic_interval_unit  = QtGui.QComboBox()
        self.input_pic_interval_unit.insertItem(0, units[4])
        self.input_pic_interval_unit.insertItem(1, units[5])
        self.input_pic_interval_unit.insertItem(2, units[6])
        self.input_pic_interval_unit.insertItem(3, units[7])
        self.input_pic_interval_unit.setCurrentIndex(0)
        
        self.input_pictime_label = QtGui.QLabel("Picture time:")
        self.input_pictime_edit = QtGui.QLineEdit("")
        self.input_pictime_unit  = QtGui.QComboBox()
        self.input_pictime_unit.insertItem(0, units[0])
        self.input_pictime_unit.insertItem(1, units[1])
        self.input_pictime_unit.insertItem(2, units[2])
        self.input_pictime_unit.insertItem(3, units[3])
        self.input_pictime_unit.setCurrentIndex(2)
        
        self.input_playback_label = QtGui.QLabel("Playback time:")
        self.input_playback_edit = QtGui.QLineEdit("")
        self.input_playback_unit  = QtGui.QComboBox()
        self.input_playback_unit.insertItem(0, units[0])
        self.input_playback_unit.insertItem(1, units[1])
        self.input_playback_unit.insertItem(2, units[2])
        self.input_playback_unit.insertItem(3, units[3])
        self.input_playback_unit.setCurrentIndex(0)
        
        
        self.input_nbrofpic_label = QtGui.QLabel("Number of Pictures:")
        self.input_nbrofpic_edit = QtGui.QLineEdit("")
        self.input_nbrofpic_unit = QtGui.QLabel("picture(s)")
        
        # Layout
        grid1 = QtGui.QGridLayout()
        #grid1.addWidget(self.input_fps_cb, 0, 0)
        grid1.addWidget(QtGui.QLabel(''), 0, 0)
        grid1.addWidget(self.input_fps_label, 0, 1)
        grid1.addWidget(self.input_fps_edit, 0, 2)
        grid1.addWidget(self.input_fps_label_fps, 0, 3)
        grid1.addWidget(self.input_pic_interval_cb, 1, 0)
        grid1.addWidget(self.input_pic_interval_label, 1, 1)
        grid1.addWidget(self.input_pic_interval_edit, 1, 2)
        grid1.addWidget(self.input_pic_interval_unit, 1, 3)
        grid1.addWidget(self.input_pictime_cb, 2, 0)
        grid1.addWidget(self.input_pictime_label, 2, 1)
        grid1.addWidget(self.input_pictime_edit, 2, 2)
        grid1.addWidget(self.input_pictime_unit, 2, 3)
        grid1.addWidget(self.input_playback_cb, 3, 0)
        grid1.addWidget(self.input_playback_label, 3, 1)
        grid1.addWidget(self.input_playback_edit, 3, 2)
        grid1.addWidget(self.input_playback_unit, 3, 3)
        grid1.addWidget(self.input_nbrofpic_cb, 4, 0)
        grid1.addWidget(self.input_nbrofpic_label, 4, 1)
        grid1.addWidget(self.input_nbrofpic_edit, 4, 2)
        grid1.addWidget(self.input_nbrofpic_unit, 4, 3)
        
        main_layout = QtGui.QVBoxLayout()
        main_layout.addLayout(grid1)
        
        # Create central widget, add layout and set
        main_widget = QtGui.QWidget()
        main_widget.setLayout(main_layout)
        self.winCenter()
        
        # set Windows infos
        self.setWindowTitle('Time Lapse Video Parameter Calculator')
        self.setWindowIcon(QtGui.QIcon('icons/zas.png'))
        self.statusBar().showMessage('Ready')
        #self.resize(windowsize[0], windowsize[1])
        
        self.setCentralWidget(main_widget)
    # END DisplayMainContent
    

    #-----------------------------------------------------------------------------
    # browse File
    #
    def browseFile(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '')
        self.input_edit.setText(filename)
        if not(filename == ''):
            self.statusBar().showMessage('Ready: File OK')
        else:
            self.statusBar().showMessage('Error: File NOK')
    # END browseFile
    
    #-----------------------------------------------------------------------------
    # browse Directory
    #
    def browseDir(self):
        dirname = QtGui.QFileDialog.getExistingDirectory(self, 'Open directory', '')
        self.output_edit.setText(dirname)
        if not(dirname == ''):
            self.statusBar().showMessage('Ready: Directory OK')
        else:
            self.statusBar().showMessage('Error: Directory NOK')
    # END browseDir
    
    #-----------------------------------------------------------------------------
    # execute Script
    #
    def exe(self):
        # Declare Variables
        update = [1,1,1,1,1]
        parameterscheck = True
        
        fps = None
        pic_interval = None
        pic_interval_unit = None
        pictime = None
        pictime_unit = None
        playback = None
        playback_unit = None
        nbr_of_pics = None
        
        # Read parameters
        try:
            #if self.input_fps_cb.isChecked():
            fps = float(fps_values[self.input_fps_edit.currentIndex()])
            #    update[0] = 0
            if self.input_pic_interval_cb.isChecked():
                pic_interval = float(self.input_pic_interval_edit.text())
                pic_interval_unit = units[self.input_pic_interval_unit.currentIndex()+4]
                [pic_interval, pic_interval_unit] = self.into_sec(pic_interval, pic_interval_unit)
                update[1] = 0
            if self.input_pictime_cb.isChecked():
                pictime = float(self.input_pictime_edit.text())
                pictime_unit = units[self.input_pictime_unit.currentIndex()]
                [pictime, pictime_unit] = self.into_sec(pictime, pictime_unit)
                update[2] = 0    
            if self.input_playback_cb.isChecked():
                playback = float(self.input_playback_edit.text())
                playback_unit = units[self.input_playback_unit.currentIndex()]
                [playback, playback_unit] = self.into_sec(playback, playback_unit)
                update[3] = 0
            if self.input_nbrofpic_cb.isChecked():
                nbr_of_pics = float(self.input_nbrofpic_edit.text())
                update[4] = 0
        except (ValueError, IndexError):
            self.statusBar().showMessage('Error: Bad Value')
            parameterscheck = False
        
        if parameterscheck:
            for i in range(5):
                # Calculate Parameters
                #if update[0] == 1:
                    #if pictime != None and pic_interval != None and playback != None: 
                    #    fps = (pictime * pic_interval) / playback
                    #elif nbr_of_pics != None and playback != None:
                    #    fps = nbr_of_pics / playback
                    #else:
                    #    self.statusBar().showMessage('Error: Picture Time, Picture interval, Playback or Number of Pictures, Playback not defined')
                if update[1] == 1:
                    if fps != None and playback != None and pictime != None:
                        pic_interval = 1/(playback * fps / pictime)
                        pic_interval_unit = units[4]
                    elif nbr_of_pics != None and pictime != None:
                        pic_interval = 1/(nbr_of_pics / pictime)
                        pic_interval_unit = units[4] 
                    else:
                        self.statusBar().showMessage('Error: FPS, Playback, Picture Time or Number of Pictures, Picture Time not defined')
                if update[2] == 1:
                    if playback != None and fps != None and pic_interval != None:
                        pictime = playback * fps / (1/pic_interval)
                        pictime_unit = units[0]
                    elif nbr_of_pics != None and pic_interval != None:
                        pictime = nbr_of_pics / (1/pic_interval)
                        pictime_unit = units[0]
                    else:
                        self.statusBar().showMessage('Error: FPS, Playback, Picture Interval or Number of Pictures, Picture Interval not defined')
                if update[3] == 1:
                    if pictime != None and pic_interval != None and fps != None:
                        playback = (pictime * (1/pic_interval)) / fps
                        playback_unit = units[0]
                    elif nbr_of_pics != None and fps != None: 
                        playback = nbr_of_pics / fps
                        playback_unit = units[0]
                    else:
                        self.statusBar().showMessage('Error: Picture Time, Picture Interval, FPS or Number of Pictures, FPS not defined')
                if update[4] == 1:
                    if pictime != None and pic_interval != None:
                        nbr_of_pics = pictime * (1/pic_interval)
                    elif fps != None and playback != None:
                        nbr_of_pics = playback * fps
                    else:
                        self.statusBar().showMessage('Error: Picture Time, Picture Interval or Playback, FPS not defined')
                        
            # Transform values into a readable unit
            [pic_interval, pic_interval_unit] = self.into_unit(pic_interval, pic_interval_unit)
            [pictime, pictime_unit] = self.into_unit(pictime, pictime_unit)
            [playback, playback_unit] = self.into_unit(playback, playback_unit)
            
            # Set calculated values
            #self.input_fps_edit.setText(str(fps))
            self.input_pic_interval_edit.setText(str(pic_interval))
            if pic_interval_unit == units[0]:
                pic_interval_unit = units[4]
            self.input_pic_interval_unit.setCurrentIndex(units.index(pic_interval_unit)-4)
            self.input_pictime_edit.setText(str(pictime))
            self.input_pictime_unit.setCurrentIndex(units.index(pictime_unit))
            self.input_playback_edit.setText(str(playback))    
            self.input_playback_unit.setCurrentIndex(units.index(playback_unit))
            self.input_nbrofpic_edit.setText(str(nbr_of_pics))
            
    # END exe
    
    #-----------------------------------------------------------------------------
    # Transform values into a readable unit
    #
    def into_unit(self, value, unit):
        
        result = [value, unit]
        if result[0] == None or result[1] == None:
            result[0] = None
            result[1] = units[0]
        else:
            for i in range(4):
                if result[1] == units[0] and result[0] >= 60:   # seconds
                    # into minutes
                    result = [result[0]/60, units[1]]
                elif result[1] == units[1] and result[0] >= 60: # minutes
                    # into hours
                    result = [result[0]/60, units[2]]
                elif result[1] == units[2] and result[0] >= 24: # hours
                    # into days
                    result = [result[0]/24, units[3]]
                elif result[1] == units[3]:                     # days
                    # already days
                    result = [result[0], result[1]]
                
                elif result[1] == units[4] and result[0] >= 60: # second(s) / picture
                    # into minutes / picture
                    result = [result[0]/60, units[5]]
                elif result[1] == units[5] and result[0] >= 60: # minute(s) / picture
                    # into hours / picture
                    result = [result[0]/60, units[6]]
                elif result[1] == units[6] and result[0] >= 24: # hour(s) / picture
                    # into days / picture
                    result = [result[0]/24, units[7]]
                elif result[1] == units[7]:                     # day(s) / picture
                    # already days
                    result = [result[0], result[1]]
                
        return result
    # END into_Sec
    
    #-----------------------------------------------------------------------------
    # into sec transform values into seconds
    #
    def into_sec(self, value, unit):
        result = [0.0, unit]
        if unit == units[3]:   # days
            result =  [(value * 24 * 60 * 60), units[0]]
        elif unit == units[2]: # hours
            result = [(value * 60 * 60), units[0]]
        elif unit == units[1]: # minutes
            result = [(value * 60), units[0]]
        elif unit == units[0]: # seconds
            # already seconds
            result = [value, units[0]]
        elif unit == units[7]:
            result = [(value * 24 * 60 * 60), units[4]]
        elif unit == units[6]:
            result = [(value * 60 * 60), units[4]]
        elif unit == units[5]:
            result = [(value * 60), units[4]]
        elif unit == units[4]:
            # already second/pic
            result = [value, units[4]]
        else:
            result = [-1, units[4]]
        
        return result
    # END into_Sec
    
    #-----------------------------------------------------------------------------
    # reset fields
    #
    def reset(self):
        self.input_fps_edit.setCurrentIndex(6)
        self.input_pic_interval_edit.setText("")
        self.input_pictime_edit.setText("")
        self.input_playback_edit.setText("")
        self.input_nbrofpic_edit.setText("")
        
        self.input_playback_unit.setCurrentIndex(0)
        self.input_pictime_unit.setCurrentIndex(2)
        self.input_pic_interval_unit.setCurrentIndex(0)
        
        self.input_fps_cb.setChecked(True)
        self.input_pic_interval_cb.setChecked(False)
        self.input_nbrofpic_cb.setChecked(False)
        self.input_pictime_cb.setChecked(False)
        self.input_playback_cb.setChecked(False)
        
        self.statusBar().showMessage('Ready: Fields reset')
    # END reset
    
    #-----------------------------------------------------------------------------
    # display help
    #
    def displayHelp(self):
        self.statusBar().showMessage('Ready: Open Help dialog')
        QtGui.QMessageBox.information(self, "TLVPC Help", "TLVPC Help\n\nFrame Rate\t - How many frames per second should the video has\nPicture Interval - How many second between two pictures\nPicture time\t - For how long you want to make pictures\nPlayback time\t - Length of the final video\nNbr of Pictures\t - How many pictures will be taken")
            
    # END Displayinfo
    
    
    #-----------------------------------------------------------------------------
    # display informations
    #
    def displayInfo(self):
        self.statusBar().showMessage('Ready: Open Info dialog')
        QtGui.QMessageBox.about(self,
                          "About me",
                          "Time Lapse Video Parameter Calculator - TLVPC\n\n Version:  v0.1\n Written in Python 2.7\n\n (c) Copyright by zas 2011 \n All rights reserved. \n\n Visit http://zawiki.dyndns.org")
    # END Displayinfo
    
    #-----------------------------------------------------------------------------
    # center window
    #
    def winCenter(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
    # END win_center
# END Class MainUI

################################################################################
# Launch Window
#
if __name__ == "__main__":
    # Someone is launching this directly
    # Create the QApplication
    app = QtGui.QApplication(sys.argv)
    # The Main window
    main_window = MainUI()
    main_window.show()
    # Enter the main loop
    app.exec_()