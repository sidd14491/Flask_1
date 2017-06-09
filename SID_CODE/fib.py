min1 = int(raw_input("Enter a lowest bound: "))
max1 = int(raw_input("Enter a highest bound: "))
def fibnc(n):
    op = []
    op1=[]
    for j in range(n):
        if j ==0:
           print op1.append(j)
        elif j ==1:
            print op1.append(j)
        else:
            sum1 = op1[j-1]+op1[j-2]
            op1.append(sum1)
    
    for k in range(len(op1)):
        if min1<=op1[k] and min1 >=op1[k-1]:
             h = k
             op.append(k)
             print k
        elif max1<=op1[k] and max1>=op1[k-1]:
             l = k
             op.append(k)
             print l
    return(op1,op)
    print op
             
op2,op3=fibnc(20)
print op2,op3
i = op3[0]+1
j = op3[1]
print op2[i:j]
            
