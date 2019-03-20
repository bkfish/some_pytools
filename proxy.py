import urllib.request
proxies={
"http":"http://localhost:1080"
}
url="http://www.google.com"
proxy=urllib.request.ProxyHandler(proxies)
opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
urllib.request.install_opener(opener)
data=urllib.request.urlopen(url).read()
print(data)