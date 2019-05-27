import re
pattern = "\w+([.+-]\w+)*@\w+([.-]\w+)*\.\w+([.-]\w+)*"
string = "<a href='http://www.baidu.com'>百度</a><br><a href='w.linkings@gail.com'>电邮</a>"
result = re.search(pattern,string)
print(result)
print(result.group(0))

# <_sre.SRE_Match object; span=(50, 69), match='w.linkings@gail.com'>