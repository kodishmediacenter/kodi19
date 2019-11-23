import xbmc
import webbrowser


def webplayer(url):
    if xbmc . getCondVisibility ( 'system.platform.android' ) :
        ost = xbmc . executebuiltin ( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( ''+url+'' ) )
    else:
        ost = webbrowser . open ( ''+url+'' )   
