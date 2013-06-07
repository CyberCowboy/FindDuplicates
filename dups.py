import os, hashlib
#rootdir = 'c:\Python Test'
hashlist = {}  # content signature -> list of filenames
dups = []

def get_hash(rootdir):
#	"""goes through directory tree, compares md5 hash of all files,
#	combines files with same hash value into list in hashmap directory"""
	#try:
	for path, dirs, files in os.walk(rootdir):
	    for filename in files:
	        fullname = os.path.join(path, filename)
	        with open(fullname) as f:
	            md5 = hashlib.md5()
	            while True:
	            	d = f.read(4096)
            		if not d:
            			break
        			md5.update(d)
	            h = md5.hexdigest()         
	            filelist = hashlist.setdefault(h, [])         
	            filelist.append(fullname)   

	for x in hashlist:
		currenthash = hashlist[x]
		if len(currenthash) > 1:
			dups.append(currenthash)
			#print currenthash
		#else:
		#	print "nothing to do here"

	output = open('duplicates.txt','w')
	output.write(str(dups))
	output.close()
			
			
	#except:
	#	print "something went pear-shaped: "
	#	pass