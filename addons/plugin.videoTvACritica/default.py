
# -*- coding: utf-8 -*-

import sys
import xbmcaddon, xbmcgui, xbmcplugin

# Plugin Info
ADDON_ID      = 'plugin.videoTvACritica'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME    = REAL_SETTINGS.getAddonInfo('name')
ICON          = REAL_SETTINGS.getAddonInfo('icon')
FANART        = REAL_SETTINGS.getAddonInfo('fanart')
YOUTUBE_CHANNEL_ID1=  "channel/UCnLSKfHkgZ6ujEYCO9jq7Sw/playlists"
YOUTUBE_CHANNEL_ID2=  "channel/UCnLSKfHkgZ6ujEYCO9jq7Sw/live"


def addDir(title, url):
    liz=xbmcgui.ListItem(title)
    liz.setProperty('IsPlayable', 'false')
    liz.setInfo(type="Video", infoLabels={"label":title,"title":title} )
    liz.setArt({'thumb':ICON,'fanart':FANART})
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)
    
if __name__ == '__main__':
    addDir(title="TV A Critica Ao Vivo"            , url="plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID2+"/")
    addDir(title="TV A Critica VOD"                , url="plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID1+"/")
    xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)
