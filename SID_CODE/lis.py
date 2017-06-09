def fun(*arg):
    arg = list(arg)
    op = max(arg[0],arg[1],arg[2])
    S = (op[0]^2+op[1]^2+op[2]^2)%arg[3][-1]
    print arg[3][-1]
    print S
a=[1,2,3]
b=[4,5,6]
c=[7,8,9]
d = [3,1000]
fun(a,b,c,d)
