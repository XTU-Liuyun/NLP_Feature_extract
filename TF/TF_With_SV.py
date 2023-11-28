
import math
import numpy as np
import time
start=time.clock()
import random
from scipy.special import expit
from main import TF_value
from Getdata import words_list
ans=[]

rate=0.9
svm=2
for i in range(len(TF_value)):
    ans_vector=[]
    T = 1e10
    T_min = 1e-30
    length=len(words_list[i])-1
    average_value = 0
    print(f"第 {i + 1} 个文档模拟退火得到")

    for j in range(len(words_list[i])-1):
        average_value+=TF_value[i][words_list[i][j]]

    average_value=average_value/(len(words_list[i]))
    #print(average_value)
    j=random.randint(1, len(words_list[i])-1)
    #print(f"随机起始点:{j}")
    while T>T_min:
        if len(ans_vector) > 10:
            break
        #print(f"{i},{j},{length}")
        if TF_value[i][words_list[i][(j+1)%length]] >= TF_value[i][words_list[i][j]]:
            if math.fabs(TF_value[i][words_list[i][(j+1)%length]]-average_value)<=svm:
                if words_list[i][(j+1)%length] not in ans_vector:
                    ans_vector.append(words_list[i][(j+1)%length])#接受
        else:
            dE=TF_value[i][words_list[i][(j+1)%length]]-TF_value[i][words_list[i][j]]
            #print(f"text:{random.uniform(0, 1)}")
            if expit(-dE / T)>random.uniform(0, 1):
                if words_list[i][(j + 1) % length] not in ans_vector:
                    ans_vector.append(words_list[i][(j + 1) % length])  # 接受
            else:
                j=random.randint(1, len(words_list[i])-1)

        T=T*rate
        j=(j+1)%length
    ans.append(ans_vector);
    print(ans_vector)
end=time.clock()
print(f"程序运行时间为:{end-start}")



