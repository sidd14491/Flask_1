import re
op = raw_input("Enter a string :: ")
p=re.finditer(r'[QWRTYPSDFGHJKLZXCVBNM][aeiou]{2,}[QWRTYPSDFGHJKLZXCVBNM]',op,re.I)
print p
for i in p:
   print i.group()
"""
if len(p)!= 0:
    for i  in range(len(p)):
        if p[i]:
           print p[i][1:-1] 
else:
   print -1
"""
