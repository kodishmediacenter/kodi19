# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,sys
import shutil
import urllib
import urllib.request,urllib.parse
from urllib.request import urlopen, Request
import re
import extract
import time
import downloader
import plugintools
import zipfile
import ntpath
import ssl
import base64
import traceback,sys
from libs import kodi
from libs import viewsetter


icon = os.path.join(xbmc.translatePath("special://home/addons/Kodish.repo.store/icon.png"))

if kodi.get_kversion() >16.5:
	#kodi.log(' VERSION IS ABOVE 16.5')
	ssl._create_default_https_context = ssl._create_unverified_context
else:
	#kodi.log(' VERSION IS BELOW 16.5')
	pass
from libs import addon_able


USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
base='http://kodish.esy.es'
ADDON=xbmcaddon.Addon(id='Kodish.repo.store')
    
    
VERSION = "1.0.2"
PATH = "kodish.esy.es"

def web_browser(urlcn):
        import webbrowser
        if xbmc . getCondVisibility ( 'system.platform.android' ) :
                ost = xbmc . executebuiltin ( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( ''+urlcn+'' ) )
        else:
                ost = webbrowser . open ( ''+urlcn+'' )

def donation():
        url = "https://uploaddeimagens.com.br/images/001/572/022/original/mercadopago.png"
        url2 = "https://goo.gl/ArZ2Gx"
        url3 = "https://pastebin.com/raw/5nMKfyPs"
        
        dialog = xbmcgui.Dialog()
        link = dialog.select('Forma de Doacao', ['App do Mercado Pago/Livre', 'PayPal','Deposito em Conta'])

        if link == 0:
        
                import webbrowser
                if xbmc . getCondVisibility ( 'system.platform.android' ) :
                    ost = xbmc . executebuiltin ( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( ''+url+'' ) )
                else:
                    ost = webbrowser . open ( ''+url+'' )

        if link == 1:
        
                import webbrowser
                if xbmc . getCondVisibility ( 'system.platform.android' ) :
                    ost = xbmc . executebuiltin ( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( ''+url2+'' ) )
                else:
                    ost = webbrowser . open ( ''+url2+'' )

        if link == 2:
        
                import webbrowser
                if xbmc . getCondVisibility ( 'system.platform.android' ) :
                    ost = xbmc . executebuiltin ( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( ''+url3+'' ) )
                else:
                    ost = webbrowser . open ( ''+url3+'' )

def CATEGORIES_IMG():
    link = OPEN_URL('https://raw.githubusercontent.com/kodishmediacenter/store/master/imagensprontas').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,1,iconimage,fanart,description)
    setView('movies', 'MAIN')

def CATEGORIES():
    link = OPEN_URL('https://raw.githubusercontent.com/kodishmediacenter/store/master/catsqueenDX').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,1,iconimage,fanart,description)
    setView('movies', 'MAIN')

def quasar_repo():
    link = OPEN_URL('https://raw.githubusercontent.com/kodishmediacenter/store/master/quasar-repo').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,1,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def KRATOSVIP():
    link = OPEN_URL('https://raw.githubusercontent.com/kodishmediacenter/store/master/kratosvip').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,1,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def CATEGORIES2():
    link = OPEN_URL('https://raw.githubusercontent.com/kodishmediacenter/store/master/kodishstoreraptor2').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,1,iconimage,fanart,description)
    setView('movies', 'MAIN')

def Reposkodish():
    link = OPEN_URL('https://raw.githubusercontent.com/kodishmediacenter/store/master/repos-kodishstore').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,1,iconimage,fanart,description)
    setView('movies', 'MAIN')

def quasardrive():
    link = OPEN_URL('https://raw.githubusercontent.com/kodishmediacenter/store/master/quasar-drive').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,1,iconimage,fanart,description)
    setView('movies', 'MAIN')

def RESTRITOM18():
    link = OPEN_URL('https://raw.githubusercontent.com/kodishmediacenter/store/master/so18').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,1,iconimage,fanart,description)
    setView('movies', 'MAIN')


def TVADDONS():
    link = OPEN_URL('https://raw.githubusercontent.com/kodishmediacenter/store/master/tvaadons').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,1,iconimage,fanart,description)
    setView('movies', 'MAIN')

def ATIVAR():
    link = OPEN_URL('https://raw.githubusercontent.com/kodishmediacenter/store/master/ative').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,1,iconimage,fanart,description)
    setView('movies', 'MAIN')


def PREMIUM():
    link = OPEN_URL('https://raw.githubusercontent.com/kodishmediacenter/store/master/premiun').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,1,iconimage,fanart,description)
    setView('movies', 'MAIN')

# https://raw.githubusercontent.com/kodishmediacenter/store/master/elementun-repo

def Lojink():
    link = OPEN_URL('https://pastebin.com/raw/sPH6k4h7').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,1,iconimage,fanart,description)
    setView('movies', 'MAIN')

def elementun():
    link = OPEN_URL('https://raw.githubusercontent.com/kodishmediacenter/store/master/elementun-repo').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,1,iconimage,fanart,description)
    setView('movies', 'MAIN')


def Traducao():
    link = OPEN_URL('https://raw.githubusercontent.com/kodishmediacenter/store/master/04062018/traducao').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,1,iconimage,fanart,description)
    setView('movies', 'MAIN')

def REPOHUNTER():
        keylink = xbmc.Keyboard('', 'Digite usuario do Github/dominio:')
        keylink.doModal()
        ulink = keylink.getText()
        link = OPEN_URL("https://raw.githubusercontent.com/"+ulink+"/master/repohunter.txt").replace('\n','').replace('\r','')
        match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
        for name,url,iconimage,fanart,description in match:
            addDir(name,url,1,iconimage,fanart,description)
        setView('movies', 'MAIN')


def REPOHUNTER2():
        keylink = xbmc.Keyboard('', 'Digite a fonte do seu addon com friend.txt:')
        keylink.doModal()
        ulink = keylink.getText()
        link = OPEN_URL(""+ulink+"/friend.txt").replace('\n','').replace('\r','')
        match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
        for name,url,iconimage,fanart,description in match:
            addDir(name,url,1,iconimage,fanart,description)
        setView('movies', 'MAIN') 

def ENCURTA_URL():
        keylink = xbmc.Keyboard('', 'Digite o Link do Addon a Ser Encurtado:')
        keylink.doModal()
        ulinks = keylink.getText()
        
        short = str(urllib.request.urlopen("http://tinyurl.com/api-create.php?url=%s" % urllib.parse.quote(ulinks)).read().decode('utf-8'))
        dialog = xbmcgui.Dialog()
        kb = short.replace("http://tinyurl.com","ks:/")
        link = dialog.select('Seu Link encurtado abaixo', [kb])
        
        
def EXTSETUP():
        keylink = xbmc.Keyboard('', 'Digite Um Friendly Link:')
        keylink.doModal()
        ulink = keylink.getText()
        link = OPEN_URL(""+ulink+"").replace('\n','').replace('\r','')
        match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
        for name,url,iconimage,fanart,description in match:
            addDir(name,url,1,iconimage,fanart,description)
        setView('movies', 'MAIN')

def EXTZSETUP():
        keylink = xbmc.Keyboard('', 'Cole o arquivo zip de um addon ou Repositorio:')
        keylink.doModal()
        ulink = keylink.getText()
        link = OPEN_URL("https://raw.githubusercontent.com/kodishmediacenter/store/master/zip").replace('\n','').replace('\r','')
        match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
        name = "Zip Instaler"
        #url  = ""+ulink+""
        iconimage = ""
        description = "[COLOR Yellow]Zip Instaler[/COLOR]"
        for name,url,iconimage,fanart,description in match:
            url  = ""+ulink+""
            addDir(name,url,1,iconimage,fanart,description)
            setView('movies', 'MAIN')


def EXTZSETUP2():
        keylink = xbmc.Keyboard('', 'Cole o link encurtado para instalar um addon ou Repositorio:')
        keylink.doModal()
        ulink2 = keylink.getText()
        liks = ulink2.replace("ks:/","http://tinyurl.com")
        link = OPEN_URL("https://raw.githubusercontent.com/kodishmediacenter/store/master/zip").replace('\n','').replace('\r','')
        match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
        name = "Zip Instaler"
        #url  = ""+ulink+""
        iconimage = ""
        description = "[COLOR Yellow]Zip Instaler[/COLOR]"
        for name,url,iconimage,fanart,description in match:
            url  = ""+liks+""
            addDir(name,url,1,iconimage,fanart,description)
            setView('movies', 'MAIN')

# mexus instruction

def limpapacotes():
    for a in ['special://home/addons/packages']:
        existe = xbmc.translatePath(a)
        if os.path.exists(existe)==True:
                shutil.rmtree(existe)
                killxbmc()

def limpaelementum():
    for a in ['special://home/addons/plugin.video.elementum','special://home/addons/script.elementum.burst','special://home/addons/context.elementum','special://home/userdata/addon_data/plugin.video.elementum']:
        existe = xbmc.translatePath(a)
        if os.path.exists(existe)==True:
                shutil.rmtree(existe)
                killxbmc()


def limpaquasar():
    for a in ['special://home/addons/plugin.video.quasar','special://home/addons/script.quasar.burst','special://home/userdata/addon_data/plugin.video.quasar']:
        existe = xbmc.translatePath(a)
        if os.path.exists(existe)==True:
                shutil.rmtree(existe)
                killxbmc()


def byebyeKeltech():
    for a in ['special://home/addons/KeltecMP.repository','special://home/addons/ElementumKTMP.repository','special://home/addons/plugin.program.keltecmpleiawizard','special://home/addons/plugin.video.KelTec-MP.torrents','special://home/addons/plugin.video.KeltecMP','special://home/addons/plugin.video.KeltecMPIPTV','special://home/addons/script.KelTecMP.Builds','special://home/addons/script.keltecmpmaintenance']:
        existe = xbmc.translatePath(a)
        if os.path.exists(existe)==True:
                shutil.rmtree(existe)
		
		

		
def mexus_kernel():
        mexus = xbmc.Keyboard('', '1 Visualizar Log do Kodi:')
        mexus.doModal()
        chavemexus = mexus.getText()
        
        if chavemexus == "1":
                logr = os.path.join(xbmc.translatePath("special://home/addons/webinterface.kratos/log.html"))
                logrr = os.path.join(xbmc.translatePath("special://logpath/kodi.log"))
                arq = open(logrr, 'r')
                arq2 = open(logr, 'w')
                texto = arq.readlines()
                arq2.write("<PRE>")
                for linha in texto :
                    arq2.write(linha)
                arq2.write("</PRE>")
                arq.close()
                arq2.close()

        if chavemexus == "2":
                logr = os.path.join(xbmc.translatePath("special://home/addons/webinterface.kratos/virtualaddon.txt"))
                logrr = os.path.join(xbmc.translatePath("special://home/addons/plugin.video.kractosbr/vaddon.xml"))
                arq = open(logrr, 'r')
                arq2 = open(logr, 'w')
                texto = arq.readlines()
                arq2.write("")
                arq2.write("Cole como Virtual addon")
                arq2.write("\n \n")
                for linhas in texto :
                    data = linhas
                    encoded2 = base64.b64encode(data)
                    arq2.write(encoded2)
                #arq2.write("</PRE>")
                arq.close()
                arq2.close()


        
                
        
    

def SETUP_REPO():
        
        xbmc.executebuiltin("ActivateWindow(10040,&quot;addons://install/&quot;,return)")

def SETUP_ADDONS():
        
        xbmc.executebuiltin("ActivateWindow(addons://sources/video/addons)")


def encurta_menu():
       dialog = xbmcgui.Dialog()
       link = dialog.select('Instalação Via KS', ['Gerar KS','Instalar ks'])

       if link == 0:
            ENCURTA_URL()
       if link == 1:
            EXTZSETUP2()
 

def setup_op():
       dialog = xbmcgui.Dialog()
       link = dialog.select('Bem Vindo Area Homebrew', ['Friend Link', 'Instalação via Link (Tem saber as dependencias)','Repo Hunter Github'])

       if link == 0:
            EXTSETUP()
       if link == 1:
            EXTZSETUP()
       if link == 2:
            REPOHUNTER()


def KodishLoja():
       dialog = xbmcgui.Dialog()
       link = dialog.select('Bem Vindo a Loja da Kodish', ['The Best Iptv', 'Dropship Brasil','China Cupons','Ativa Box'])

       if link == 0:
           dialog = xbmcgui.Dialog()
           tbiptv = dialog.select('THE BEST IPTV ', ['[COLOR yellow]Solicitar Teste[/COLOR]', '[COLOR yellow]Apartir R$ 25,00[/COLOR]','','[COLOR yellow]Revendedora Katia[/COLOR]'])

           if tbiptv == 0:

               urlt = 'http://bit.ly/2ACuIby'
               import webbrowser
               if xbmc . getCondVisibility ( 'system.platform.android' ) :
                            ost = xbmc . executebuiltin ( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( ''+urlt+'' ) )
               else:
                            ost = webbrowser . open ( ''+urlt+'' )    
       if link == 1:
               urld = 'https://www.facebook.com/groups/2159332667716973/'
               import webbrowser
               if xbmc . getCondVisibility ( 'system.platform.android' ) :
                            ost = xbmc . executebuiltin ( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( ''+urld+'' ) )
               else:
                            ost = webbrowser . open ( ''+urld+'' )   
       if link == 2:
            urlcn = 'https://web.telegram.org/#/im?p=@melhorescupons'
            import webbrowser
            if xbmc . getCondVisibility ( 'system.platform.android' ) :
                    ost = xbmc . executebuiltin ( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( ''+urlcn+'' ) )
            else:
                    ost = webbrowser . open ( ''+urlcn+'' )

       if link == 3:
            import loja
            loja.ativa_box()
                
        
def menukodish():
       dialog = xbmcgui.Dialog()
       ret = dialog.select('[COLOR yellow]Bem Vindo a Kodish Store Amaterasu MX[/COLOR]', ['Donation Here !!! Doe aqui !!!','Loja da Kodish','','Addons Gerais','Instalacao via Fonte', 'Gerar e Instalar ks','Kodi Repositorios','Quasar Instaler', 'Elementun Instaler','Quasar Drive','Ativar Addon (kodi17)','Ativar Addon Manualmente (kodi17)','Addons Nao Homologados Homebrew','Salvar o Log do Kodi','Deixar o Kodi em PT-BR','Limpar Pacotes','Remover Elementun','Remover Quasar'])
       ret = int(ret)

       if ret == 0:
            donation()
       if ret == 1:
            KodishLoja()
       if ret == 3:
            CATEGORIES2()
            CATEGORIES()
       if ret == 4:
            REPOHUNTER2()
       if ret == 5:
            encurta_menu()
       if ret == 6:
            Reposkodish()
       if ret == 7:
            quasar_repo()
       if ret == 8:
            elementun()
       if ret == 9:
            quasardrive()
       if ret == 10:
            ATIVAR()
       if ret == 11:
            SETUP_REPO()
       if ret == 12:
            setup_op()
       if ret == 13: 
            mexus_kernel()      
       if ret == 14:
           dialog = xbmcgui.Dialog()
           ret2 = dialog.select('[COLOR yellow]Traduza seu Kodi pera Pt-Br[/COLOR]', ['Traduzir', 'Ativar a Traducao'])
           if ret2 == 0:
                   Traducao()
           if ret2 == 1:
                   xbmc.executebuiltin("ActivateWindow(10040,addons://user/kodi.resource.language)")
       if ret == 15:
               limpapacotes()
       if ret == 16:
               limpaelementum()
       if ret == 17:
               limpaquasar()
        
			   

           
           
           
               

        
        
def OPEN_URL(url):
    req = data = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}))
    link=req.read().decode('utf-8')
    return link
    
    
def wizard(name,url,description):
    path = xbmc.translatePath(os.path.join('special://home','media'))
    dp = xbmcgui.DialogProgress()
    dp.create("Addon Selecionado","Baixando ",'', 'Por Favor Espere')
    lib=os.path.join(path, name+'.zip')
    try:
       os.remove(lib)
    except:
       pass
    
    downloader.download(url, lib, dp)
    addonfolder = xbmc.translatePath(os.path.join('special://','home/','addons'))
    time.sleep(2)
    dp.update(0,"", "Instalando Por Favor Espere")
    print ('=======================================')
    print (addonfolder)
    print ('=======================================')
    extract.all(lib,addonfolder,dp)
    #dialog = xbmcgui.Dialog()
    #dialog.ok("Baixado com Sucesso:)", 'Para continuar a Instalacao irar ser solicitado que desligue o Kodi', 'Se for uma Box precione [COLOR yellow]NAO[/COLOR] depois sai do kodi para terminar a instalacao.','[COLOR yellow][B][Kodi 17][/B][/COLOR]Ao Voltar vai Addons em Meus Addons ativa o addons instalado')
    time.sleep(2)
    xbmc.executebuiltin("XBMC.UpdateLocalAddons()");
    addon_able.set_enabled("")
    addon_able.setall_enable()
    #killxbmc()
        
      
        
def killxbmc():
    choice = xbmcgui.Dialog().yesno('Desligando o Kodi', 'Opa Blz vc Limpou Pacotes mas para Continuar vc tem Desligar seu Kodi', 'Posso Continuar', nolabel='Nao',yeslabel='Sim Preciso Continuar Instalando')
    if choice == 0:
        return
    elif choice == 1:
        pass
    myplatform = platform()
    print ("Platform: " + str(myplatform))
    if myplatform == 'osx': # OSX
        print ("############   try osx force close  #################")
        try: os.system('killall -9 XBMC')
        except: pass
        try: os.system('killall -9 Kodi')
        except: pass
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=blue]DO NOT[/COLOR] exit cleanly via the menu.",'')
    elif myplatform == 'linux': #Linux
        print ("############   try linux force close  #################")
        try: os.system('killall XBMC')
        except: pass
        try: os.system('killall Kodi')
        except: pass
        try: os.system('killall -9 xbmc.bin')
        except: pass
        try: os.system('killall -9 kodi.bin')
        except: pass
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=blue]DO NOT[/COLOR] exit cleanly via the menu.",'')
    elif myplatform == 'android': # Android  
        print ("############   try android force close  #################")
        try: os.system('adb shell am force-stop org.xbmc.kodi')
        except: pass
        try: os.system('adb shell am force-stop org.kodi')
        except: pass
        try: os.system('adb shell am force-stop org.xbmc.xbmc')
        except: pass
        try: os.system('adb shell am force-stop org.xbmc')
        except: pass        
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "Your system has been detected as Android, you ", "[COLOR=yellow][B]MUST[/COLOR][/B] force close XBMC/Kodi. [COLOR=blue]DO NOT[/COLOR] exit cleanly via the menu.","Pulling the power cable is the simplest method to force close.")
    elif myplatform == 'windows': # Windows
        print ("############   try windows force close  #################")
        try:
            os.system('@ECHO off')
            os.system('tskill XBMC.exe')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('tskill Kodi.exe')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im Kodi.exe /f')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im XBMC.exe /f')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im SPMC.exe /f')
        except: pass
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=blue]DO NOT[/COLOR] exit cleanly via the menu.","Use task manager and NOT ALT F4")
    else: #ATV
        print ("############   try atv force close  #################")
        try: os.system('killall AppleTV')
        except: pass
        print ("############   try raspbmc force close  #################") #OSMC / Raspbmc
        try: os.system('sudo initctl stop kodi')
        except: pass
        try: os.system('sudo initctl stop xbmc')
        except: pass
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=blue]DO NOT[/COLOR] exit via the menu.","Your platform could not be detected so just pull the power cable.")    

def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'



def addDir(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.parse.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.parse.quote_plus(name)+"&iconimage="+urllib.parse.quote_plus(iconimage)+"&fanart="+urllib.parse.quote_plus(fanart)+"&description="+urllib.parse.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz, isFolder=False)
        #filekodi = xbmc.translatePath('special://home/media/abra.txt')
        #arqf = open(filekodi,'w')
        #arqf.write()
        #arqf.close()
        return ok
        
       
        
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param
        
                      
params=get_params()
url=None
name=None
mode=None
iconimage=None
fanart=None
description=None


try:
        url=urllib.unquote(params["url"])
except:
        pass
try:
        name=urllib.unquote(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote(params["description"])
except:
        pass
        
        
print (str(PATH)+': '+str(VERSION))
print ("Mode: "+str(mode))
print ("URL: "+str(url))
print ("Name: "+str(name))
print ("IconImage: "+str(iconimage))


def setView(content, viewType):
    # set content type so library shows more views and info
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )
        
        
if mode==None or url==None or len(url)<1:
        byebyeKeltech()
        menukodish()
        
       
elif mode==1:
        
        wizard(name,url,description)

elif mode==101:
        TVADDONS()
        CATEGORIES()
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

        
xbmcplugin.endOfDirectory(int(sys.argv[1]))

