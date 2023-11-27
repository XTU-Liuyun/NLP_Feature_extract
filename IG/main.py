import time
start=time.clock()
from Getdata import words_list
from IG import GetIG
ig_value_total = []

for i in range(len(words_list)):
    ig_value = []
    #print(words_list[i])
    for j in range(len(words_list[i]) - 1):
        ig_value.append((words_list[i][j], GetIG(words_list[i][j], words_list)))
    # 排序并去重
    ig_value_sorted = sorted(set(ig_value), key=lambda x: x[1], reverse=True)
    ig_value_total.append(ig_value_sorted)

# 打印排序后的结果
for i in range(len(ig_value_total)):
    print(f"文档 {i + 1}:")
    for k, (word, ig) in enumerate(ig_value_total[i][:20]):
        print(f"{k + 1}. {word}: {ig}")
    print("\n")
end=time.clock()
print(f"程序运行时间为:{end-start}")