op = "HackerRank.com presents Pythonist 2"
def swap_case(s):
   newstring = ""
   for i in s:
       if i.isupper():
          newstring+=i.lower()
       else:
           newstring+=i.upper()
   return newstring
print swap_case(op) 

