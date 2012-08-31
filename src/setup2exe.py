#!/usr/bin/env python
# filename:          setup2exe.py
# kind:              Python file
# first created:     15.08.2011
# created by:        zas
# last edited:       15.08.2011
# last change by:    zas
#
################################################################################
# History:
#
# v0.1 : zas 15.08.2011
#
################################################################################
# Description: 
# script to generate a Windows executable (no Python required afterwards)
################################################################################
# Installation: 
# Module     : py2exe
# Win only   : py2exe installer, Microsoft Visual C++ 2008 Redistributable Package
# DLL needed : Python26/DLLs/msvcp90.dll 
################################################################################
__author__ = "Zahno Silvan"
__date__   = "15.08.2011"

################################################################################
# Import modules
#
from distutils.core import setup
import py2exe, sys

################################################################################
# Constants
#
includes = ['sip']
excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
            'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
            'Tkconstants', 'Tkinter']
packages = []
dll_excludes = ['libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll', 'tcl84.dll',
                'tk84.dll']

################################################################################
# Py2exe setup
#
sys.argv.append('py2exe')

setup(
    name = 'TimeLapseCalc',
    version = '1.0',
    description = 'Time Lapse Video Parameter Calculator',
    author = 'Zahno Silvan',
    options = {"py2exe": {"compressed": 2,
                          "optimize": 0,
                          "includes": includes,
                          "excludes": excludes,
                          "packages": packages,
                          "dll_excludes": dll_excludes,
                          "bundle_files": 3,
                          "dist_dir": "bin",
                          "xref": False,
                          "skip_archive": False,
                          "ascii": False,
                          "custom_boot_script": '',
                         }
              },
    windows = ['gui.pyw'],
    data_files=[("icons",
                 ["icons/back.png", 
                  "icons/exit.png",
                  "icons/info.png",
                  "icons/help.png",
                  "icons/reset.png",
                  "icons/run.png",
                  "icons/zas.png"])]
    )
