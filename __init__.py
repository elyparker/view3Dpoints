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
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load view3Dpoints class from file view3Dpoints
    from view3dpoints import view3Dpoints
    return view3Dpoints(iface)
