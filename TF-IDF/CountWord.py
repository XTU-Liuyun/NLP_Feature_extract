from collections import Counter
from GetWord import words_list

count_list = list()
for i in range(len(words_list)):
    count = Counter(words_list[i])
    #print(count)
    count_list.append(count)

