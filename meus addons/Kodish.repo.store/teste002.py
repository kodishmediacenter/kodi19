from urllib.request import urlopen, Request
url = "https://pastebin.com/raw/tT9PftLn"
data = urlopen(Request(url, headers={'User-Agent': 'Mozilla'}))
print(data)

