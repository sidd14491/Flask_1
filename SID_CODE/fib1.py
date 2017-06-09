def fib(lowerbound, upperbound):
    x = 0
    y = 1
    while x <= upperbound:
        if (x >= lowerbound):
            print  x
            #yield x
        x, y = y, x + y

startNumber = 10
endNumber = 100
import pdb;pdb.set_trace()
fib(startNumber, endNumber)
#for fib_sequence in fib(startNumber, endNumber):
#    print "And the next number is... %d!" % fib_sequence
