import os,stat
infile ="/Users/ssiddh/SID_CODE/module_practice/os_1.py"
st = os.stat(infile)
print "mode ::: %s"%(stat.S_IMODE(st[stat.ST_MODE]))
for i in st:
   print i
