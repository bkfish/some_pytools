from hashlib import md5
allString = "1234567890-_,qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
part_hash="33c2ac"
for m in allString:
	string=m
	print(string)
	if(md5(string.encode('utf-8')).hexdigest()[:6] == part_hash):
		print(string)
		#print(part_hash)
		exit(0) 

for m in allString:
	for x in allString:
		string=m+x
		print(string)
		if(md5(string.encode('utf-8')).hexdigest()[:6] == part_hash):
			print(string)
			#print(part_hash)
			exit(0) 
for m in allString:
	for x in allString:
		for i in allString:
			string=m+x+i
			print(string)
			if(md5(string.encode('utf-8')).hexdigest()[:6] == part_hash):
				print(string)
				#print(part_hash)
				exit(0) 
for m in allString:
	for x in allString:
		for i in allString:
			for j in allString:
				string=m+x+i+j
				print(string)
				if(md5(string.encode('utf-8')).hexdigest()[:6] == part_hash):
					print(string)
					#print(part_hash)
					exit(0) 

for m in allString:
	for x in allString:
		for i in allString:
			for j in allString:
				for a in allString:
					string=m+x+i+j+a
					print(string)
					if(md5(string.encode('utf-8')).hexdigest()[:6] == part_hash):
						print(string)
						#print(part_hash)
						exit(0) 

for m in allString:
	for x in allString:
		for i in allString:
			for j in allString:
				for a in allString:
					for b in allString:
						string=m+x+i+j+a+b
						print(string)
						if(md5(string.encode('utf-8')).hexdigest()[:6] == part_hash):
							print(string)
							#print(part_hash)
							exit(0) 
