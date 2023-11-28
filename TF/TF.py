
def TF(word,corpus):
    print(word)
    num=0;
    for i in range(len(corpus)):
        for j in range(len(corpus[i])):
            print(f"{corpus[i][j]} {word}")
            if corpus[i][j]==word:

                num=num+1;
    return num;