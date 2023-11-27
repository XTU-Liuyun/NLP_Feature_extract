import re
import time
start=time.clock()
from Getdata import words_list


TF_value = []

for i in range(len(words_list)):
    wordvalue = {}
    for j in range(len(words_list[i])):
        word = words_list[i][j]
        if word not in wordvalue:
            #print(word)
            wordvalue[word] = 1
        else:
            wordvalue[word] = wordvalue[word]+1
    TF_value.append(wordvalue)


sorted_TF_value = [dict(sorted(d.items(), key=lambda item: item[1], reverse=True)) for d in TF_value]

for i, wordvalue in enumerate(TF_value):
    print(f"第 {i + 1} 个文档 TF 统计信息")
    top_20 = list(wordvalue.items())[:20]
    for j, (word, value) in enumerate(top_20):
        print(f"{j + 1}. {word}: {value}")
    print("\n")

end=time.clock()
print(f"程序运行时间为:{end-start}")