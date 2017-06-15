import re
unique=[]
fp = open("/Users/ssiddh/GIT/Flask_1/Interveiw_coding/1.txt",'r')
fp1 = fp.read()
out = re.findall("[a-zA-Z/_0-9]*\.(?!mp4)\w+",fp1)
out1 = re.findall("[a-zA-Z/_0-9]*\.mp4",fp1)
for i in out:
    op = i.split(".")
    if op[0]+".mp4" in out1:
       pass
    else:
        unique.append(i)
print unique
