import math
from Getdata import total_num,category_num

CONST_PROBILITY=1.0#如果没有特殊说明(不考虑大小) 则概率:1/文档总数
def GetIG(word,corpus):#i——第几个文档 corpus——文档集合
        length=len(corpus)
        Hc=0;
        Pci=0
        Pnci=0;
        Pnt=0;
        occur_time=0
        occur_time_ci=0
        occur_time_nci=total_num;
        total_word=0
        for key, value in category_num.items():
                P=value/total_num
                Hc=Hc+(P*math.log(P))
        Hc=-Hc
        #比如P(t)，就是特征T出现的概率，只要用出现过T的文档数除以总文档数就可以了
        for i in range(length):
                for j in range(len(corpus[i])-1):
                        if corpus[i][j]==word:
                                occur_time+=1
                                break
        Pt=occur_time/total_num

        #比如P(Ci|t)表示出现T的时候，类别Ci出现的概率，只要用出现了T并且属于类别Ci的文档数除以出现了T的文档数就可以了。
        for key,value in category_num.items():
                for i in range(length):
                        if corpus[i][len(corpus[i])-1] == key:
                                for j in range(len(corpus[i]) - 1):
                                        if corpus[i][j]==word:
                                                occur_time_ci+=1
                                                break;
                        Pci_1=occur_time_ci/occur_time
                        Pci=Pci+(Pci_1*math.log(Pci_1+1,2))

        for key,value in category_num.items():
                for i in range(len(corpus)):
                        if corpus[i][len(corpus[i])-1] == key:
                                for j in range(len(corpus[i]) - 1):
                                        if corpus[i][j]==word:
                                                occur_time_nci-=1
                                                break;
                        Pnci_1=occur_time_nci/((total_num-occur_time)+1)
                        #print(Pnci_1)
                        Pnci=Pnci+(Pnci_1*math.log(Pnci_1+1))
        IG=Hc+Pt*Pci+(1-Pt)*Pnci
        return IG;
