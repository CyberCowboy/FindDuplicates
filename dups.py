import os, hashlib
hashdict = {}  # content signature -> list of filenames
dups = []

def Dups(rootdir):
    """goes through directory tree, compares md5 hash of all files,
    combines files with same hash value into list in hashmap directory"""
    for path, dirs, files in os.walk(rootdir):
        #this section goes through the given directory, and all subdirectories/files below
        #as part of a loop reading them in
        for filename in files:
            #steps through each file and starts the process of getting the MD5 hashes for the file
            #comparing that hash to known hashes that have already been calculated and either merges it
            #with the known hash (which indicates duplicates) or adds it so that it can be compared to future
            #files
            fullname = os.path.join(path, filename)
            with open(fullname) as f:
                #does the actual hashing
                md5 = hashlib.md5()
                while True:
                    d = f.read(4096)
                    if not d:
                        break
                    md5.update(d)
                h = md5.hexdigest()         
                filelist = hashdict.setdefault(h, [])         
                filelist.append(fullname)   

    for currenthash in hashdict.itervalues():
        #goes through and if has has more than one file listed with it
        #considers it a duplicate and adds it to the output list
        if len(currenthash) > 1:
            dups.append(currenthash)
    output = open('duplicates.txt','w')
    for x in dups:
        print x
        output.write(str(x))
        output.write('\n')
    #output.write(str(dups))
    output.close()