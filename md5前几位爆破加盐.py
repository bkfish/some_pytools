from hashlib import md5
allString = "1234567890-_,qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
salt="f13c"
part_hash="8089a"
for i in allString:
	string=i
	if(md5((string + salt).encode('utf-8')).hexdigest()[:5] == part_hash):
		print(string)
for i in allString:
	for j in allString:
		string=i+j
		#print(string)
		if(md5((string + salt).encode('utf-8')).hexdigest()[:5] == part_hash):
			print(string)
for x in allString:
	for i in allString:
		for j in allString:
			string=x+i+j
			#print(string)
			if(md5((string + salt).encode('utf-8')).hexdigest()[:5] == part_hash):
				print(string)
				exit(0)
for m in allString:
	for x in allString:
		for i in allString:
			for j in allString:
				string=m+x+i+j
				#print(string)
				if(md5((string + salt).encode('utf-8')).hexdigest()[:5] == part_hash):
					print(string)
					#print(part_hash)
					exit(0) 
