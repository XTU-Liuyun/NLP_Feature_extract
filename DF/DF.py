import re
from Getdata import words_list
def DF(word):
    num=0;
    for i in range(len(words_list)):
        for j in range(len(words_list[i])):
            if words_list[i][j]==word:
                num=num+1;
                break;

DF_value = []
wordvalue={}
for i in range(len(words_list)):
    wordexist=[]
    for j in range(len(words_list[i])):
        word = words_list[i][j]
        if word not in wordexist:
            if word not in wordvalue:
                wordvalue[word]=1
            else:
                wordvalue[word]=wordvalue[word]+1
        wordexist.append(word)

DF_value.append(wordvalue)
sorted_DF_value = [dict(sorted(d.items(), key=lambda item: item[1], reverse=True)) for d in DF_value]

for wordvalue in enumerate(sorted_DF_value):

    print(wordvalue)