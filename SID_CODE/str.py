from itertools import groupby
op = str(raw_input("Enter a string::"))
n = int(raw_input("Enter a value::"))
op1 = list(op)
k = len(op1)/n
op3=[]
for i in range(0,len(op1),k):
    op2=""
    for j in range(i,n+i):
        #print op1[j]
        op2+=op1[j]
    op3.append(op2)
for i in range(len(op3)):
    import pdb;pdb.set_trace()
    for s in i:
        if s == s+1:
           out =s+1
           #del (s+1)
        else:
           print s
