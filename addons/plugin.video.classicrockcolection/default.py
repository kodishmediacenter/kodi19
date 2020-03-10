#   Copyright (C) 2018 Lunatixz
#
#
# This file is part of ComicBook.com - YouTube.
#
# ComicBook.com - YouTube is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ComicBook.com - YouTube is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ComicBook.com - YouTube.  If not, see <http://www.gnu.org/licenses/>.


# -*- coding: utf-8 -*-

import sys
import xbmcaddon, xbmcgui, xbmcplugin

# Plugin Info
ADDON_ID      = 'plugin.video.classicrockcolection'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME    = REAL_SETTINGS.getAddonInfo('name')
ICON          = REAL_SETTINGS.getAddonInfo('icon')
FANART        = REAL_SETTINGS.getAddonInfo('fanart')
YOUTUBE_CHANNEL_ID1 = "playlist/PLNxOe-buLm6cz8UQ-hyG1nm3RTNBUBv3K"

def addDir(title, url):
    liz=xbmcgui.ListItem(title)
    liz.setProperty('IsPlayable', 'false')
    liz.setInfo(type="Video", infoLabels={"label":title,"title":title} )
    liz.setArt({'thumb':ICON,'fanart':FANART})
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)
    
if __name__ == '__main__':
    addDir(title = "Classic Rock Collection",url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID1+"/")
    xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)
