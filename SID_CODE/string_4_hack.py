op = "ABCDCDC"
op1 ="CDC"
for i in range(0,len(op),len(op1)):
    #print op[0:len(op1)]
    if op1 == op[0:len(op1)-1]:
       print op1
    
