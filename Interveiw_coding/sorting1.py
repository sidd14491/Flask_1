op = [1,10,9,7,8]
op1=[3,4,2,5]
c= op+op1
import pdb;pdb.set_trace()
for i in range(len(c)):
    for j in range(len(c)-1):
       if c[i]<c[j+1]:
          pass
       else:
         temp = c[i]
         c[i] = c[j+1]
         c[j+1] = temp
print c
