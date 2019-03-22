import re
pattern = "[a-zA-Z]+://[^\s]*[.com|.cn]"
string = "<a href='http://www.baidu.com'>百度首页</a>"
result1 = re.search(pattern,string)
print(result1)
print(result1.group(0))
