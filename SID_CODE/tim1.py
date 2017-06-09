from datetime import *
op ="2016-12-29T10:30:07.119045211Z"
op1 = "DEC 29 2016 10:30PM"
op1 = datetime.strptime(op1, '%b %d %Y %I:%M%p')
print op1
print date.today()
