import requests
import re
url = 'http://120.24.86.145:8002/qiumingshan/'
s = requests.Session()
source = s.get(url)
expression = re.search(r'(\d+[+\-*])+(\d+)', source.text).group()
result = eval(expression)
post = {'value': result}
print(s.post(url, data = post).text)
