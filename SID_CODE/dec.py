import pdb
#pdb.set_trace()
def timing_fun(some_func):
    def wrapper(name):
       print "Hi Sid"
       some_func(name)
       print "Bye Sid"
    return wrapper

@timing_fun
def call_func(name):
   print "Dhanbad::%s"%name

print call_func("Vikash")
