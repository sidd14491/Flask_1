lower = int(raw_input("Enter a lower bound value :: "))
upper = int(raw_input("Enter a upper bound value :: "))
print 2**3
def fib(lower,upper):
    for number in range(lower,upper,1):
        order = len(str(number))
        sum = 0
        tmp =  number
        while tmp>0:
             digit = tmp%10
             sum+=(digit**order)
             tmp//=10
        if number == sum:
           print number
fib(lower,upper)
