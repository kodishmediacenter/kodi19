# -*- coding: utf-8 -*-

import xbmc
import xbmcgui
import webbrowser


def web_browser(urlcn):
        import webbrowser
        if xbmc . getCondVisibility ( 'system.platform.android' ) :
                ost = xbmc . executebuiltin ( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( ''+urlcn+'' ) )
        else:
                ost = webbrowser . open ( ''+urlcn+'' )


def ativa_box():                
    dialog = xbmcgui.Dialog()
    linkmx = dialog.select('Bem Vindo Ativa Box', ['Contato', 'Preços','Como Ativar','Downloads'])

    if linkmx ==0:
        web = "https://web.telegram.org/#/im?p=@voddublado"
        web_browser(web)

    if linkmx ==1:
        web2 ="https://www.ativabox.com/#pricing"
        web_browser(web2)
                        
    if linkmx ==2:
        web3 ="https://www.ativabox.com/#como-ativar"
        web_browser(web3)

    if linkmx ==3:
        dialog = xbmcgui.Dialog()
        linkdown = dialog.select('Download', ['MFC Mobile', 'MFC Box','Super Tv','Super Cinema','Tv Express','Plex','Star Br','App Lista Android','App Lista IOS'])

        linkdic = {
                    0:"http://www.mediafire.com/file/cath95joa2qv38b/MFC_Mobile.apk/file",
                    1:"http://www.mediafire.com/file/nyeaoxvv774dksa/MFC_Tvbox.apk/file",
                    2:"http://bit.ly/supertv-tv",
                    3:"http://bit.ly/supertv-cinema",
                    4:"http://bit.ly/app-TVExpress",
                    5:"https://www.plex.tv/apps-devices/#players",
                    6:"http://iptv.starbr.in/StarBR.apk",
                    7:"https://play.google.com/store/apps/details?id=com.nathnetwork.painel",
                    8:"https://itunes.apple.com/us/app/iptv-smarters-player/id1383614816?mt=8",
                  }
        web_browser(linkdic[linkdown])
