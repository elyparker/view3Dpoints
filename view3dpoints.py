# -*- coding: utf-8 -*-
"""
/***************************************************************************
 view3Dpoints
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from osgeo import ogr

import visvis
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from view3dpointsdialog import view3DpointsDialog
import os.path


class view3Dpoints:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'view3dpoints_{}.qm'.format(locale))
        
        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = view3DpointsDialog()

    def initGui(self):
    
        
        def handleLayerChange(layer):
            self.cLayer = self.canvas.currentLayer() 
   
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/view3dpoints/icon.png"),
            u"View 3D  points of layer ", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)
        
        self.canvas=self.iface.mapCanvas()        
        self.cLayer=self.canvas.currentLayer()              
           
        self.iface.currentLayerChanged.connect(handleLayerChange)




        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&view3Dpoints", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&view3Dpoints", self.action)
        self.iface.removeToolBarIcon(self.action)
    
    def viewRender(self,elevation):       
        
        
        if self.cLayer.type()==QgsMapLayer.RasterLayer: return
        x=[]
        y=[]
        z=[]
        for feat in self.cLayer.getFeatures():
           
            geom=feat.geometry()
            wkb=geom.asWkb()
            point3d = ogr.CreateGeometryFromWkb(wkb)       
          
            x.append(point3d.GetX())
            y.append(point3d.GetY())
            if elevation!='Z value' :
                z.append(feat[elevation] or 0)
            else : z.append(point3d.GetZ() or 0)
            
        print z
        f = visvis.gca()
        m = visvis.plot(x,y,z, lc='k', ls='', mc='g', mw=2, lw=2, ms='.')

        f.daspect = 1,1,20
        
    
    
    # run method that performs all the real work
    def run(self):
        def initLayerCombobox(combobox,default,lv):
            
            combobox.clear()
            combobox.addItem("Z value")
            if lv.type()!=QgsMapLayer.RasterLayer:
                
                listacampi=lv.dataProvider().fields().toList()
            
                
                for campo in listacampi:
                    if campo.typeName() == 'Real'  :
        
                        combobox.addItem( campo.name() )
            
                idx=-1
                if (default!=None) : idx = combobox.findText( default )
                if idx != -1:
                    combobox.setCurrentIndex( idx)
                    
        if self.cLayer==None : return            
        initLayerCombobox(self.dlg.ui.zCB,"Z value",self.cLayer)
         
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
           self.viewRender(self.dlg.ui.zCB.currentText())
