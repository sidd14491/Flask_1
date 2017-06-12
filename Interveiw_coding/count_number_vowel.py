import re
ip_str = 'Hello, have you tried our turorial section yet?'
count = 0
out ={}
match_string = re.findall("[aeiou]",ip_str)
for i in match_string:
    #count = out.get(i,0)
    out[i] = out.get(i,0)+1
    #out[i] = count+1
print out
