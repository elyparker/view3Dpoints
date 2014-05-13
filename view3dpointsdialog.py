# -*- coding: utf-8 -*-
"""
/***************************************************************************
 view3DpointDialog
                                 A QGIS plugin
 for see a 3d point in axis with visvis
                             -------------------
        begin                : 2014-02-06
        copyright            : (C) 2014 by Salvatore Caligiore
        email                : info@paraparlando.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from ui_view3dpoints import Ui_view3Dpoints
# create the dialog for zoom to point


class view3DpointsDialog(QtGui.QDialog, Ui_view3Dpoints):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.ui=Ui_view3Dpoints()
        self.ui.setupUi(self)
