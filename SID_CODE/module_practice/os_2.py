import os

# Where are we ?
op = os.getcwd()
print op

# Channge the directory
os.chdir("stringIO")
print "2",os.getcwd()
