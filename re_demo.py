import re
pattern = "python"
string = "abcdfasdfasdf123Python_pyafasdf"
result1 = re.search(pattern,string)
result2 = re.search(pattern,string,re.I)
print(result1)
print(result2)
print(result2.group(0))