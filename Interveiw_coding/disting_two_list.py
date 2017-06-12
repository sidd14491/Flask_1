temp1 = ['One', 'Two', 'Three', 'Four']
temp2 = ['One', 'Two']
op=[]
for i in temp1:
    if i not in temp2:
        op.append(i)
print op
op1=[]
op1.extend(i for i in temp1 if i not in temp2)
print op1
