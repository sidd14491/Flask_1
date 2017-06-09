op="abracadabra"
def mutate_string(string,n,charachter):
   print string[:n]+charachter+string[n+1:]
   op1=list(op)
   op1[5] = charachter
   print ''.join(op1)
mutate_string(op,5,'k')  
