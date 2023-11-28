
import time
start=time.clock()
from CountWord import count_list
from TFIDF import TF_IDF

wordvalue_list = []

for i, count in enumerate(count_list):
    wordvalue = {j: TF_IDF(j, count, count_list) for j in count}
    wordvalue_list.append(wordvalue)
    #print(wordvalue_list)
sorted_wordvalue_list = [dict(sorted(d.items(), key=lambda item: item[1], reverse=True)) for d in wordvalue_list]

for i, wordvalue in enumerate(sorted_wordvalue_list):
    print("第 {} 个文档 TF-IDF 统计信息".format(i + 1))

    # 取前20个
    top_20 = list(wordvalue.items())[:20]

    for j, (word, value) in enumerate(top_20):
        print(f"{j + 1}. {word}: {value}")

    print("\n")
end=time.clock()
print(f"程序运行时间为:{end-start}")