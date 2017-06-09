import re
data = '''\
ashwin programmer india
amith programmer india'''
dict_word = {}
match_pattern = re.findall('[a-z]{3,15}',data)
print match_pattern
for word in match_pattern:
    count  = dict_word.get(word,0)
    dict_word[word] = count+1
print dict_word
