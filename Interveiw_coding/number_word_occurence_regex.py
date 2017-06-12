import re
dict_count = {}
fp = open("test.txt",'r')
text_string = fp.read().lower()
#match_pattern = re.findall('[a-z]{3,15}',text_string)
match_pattern = re.findall('[aeiou]',text_string)
for word in match_pattern:
     count = dict_count.get(word,0)
     dict_count[word] = count+1
print dict_count
