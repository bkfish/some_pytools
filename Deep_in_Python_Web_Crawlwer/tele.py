import re
pattern = "\d{4}-\d{7}|\d{3}-\d{8}"
string = "0551-54321234513451451345"
result1 = re.search(pattern,string)
print(result1)
print(result1.group(0))