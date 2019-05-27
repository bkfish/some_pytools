import urllib.request
import urllib.parse
url = "http://www.iqianyue.com/mypost"
postdata = urllib.parse.urlencode({
"name":"Kitty",
"pass":"haha"
}).encode("utf-8") 
req = urllib.request.Request(url,postdata)
req.add_header("User-Agent","Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Mobile Safari/537.36")
data = urllib.request.urlopen(req).read().decode('utf-8')
print(data)