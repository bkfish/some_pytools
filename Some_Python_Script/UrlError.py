import urllib.request
import urllib.error
try:
    file=urllib.request.urlopen("http://www.baiduddd.com")
    print(file.read())
except urllib.error.URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)
# except urllib.error.URLError as e:
#     print(e.reason)
# except urllib.error.HTTPError as e:
#     print(e.code)
#     print(e.reason)