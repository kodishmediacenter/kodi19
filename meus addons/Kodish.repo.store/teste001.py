import urllib.request

def ENCURTA_URL():
        keylink = "https://intellipaat.com/community/25654/python-sockets-error-typeerror-a-bytes-like-object-is-required-not-str-with-send-function"
        ulinks = keylink.encode('utf-8')
        short = str(urllib.request.urlopen("http://tinyurl.com/api-create.php?url=%s" % urllib.parse.quote(ulinks)).read().decode('utf-8'))
        
        kb = short.replace("http://tinyurl.com","ks:/").encode('utf-8')
        print(kb.decode('utf-8'))
                           
        
        


ENCURTA_URL()
