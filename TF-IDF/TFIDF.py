import math

def TF(word,articals):
    #print(sum(articals.values()))
    return articals[word]/sum(articals.values())

def IDF(word,count_list):
    m=sum([count[word] for count in count_list if word in count])
    n=sum([sum(count.values()) for count in count_list])
    return math.log(n/(m+1))

def TF_IDF(word,articals,corpus):
    return TF(word,articals)*IDF(word,corpus)
