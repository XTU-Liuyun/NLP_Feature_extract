import jieba
import jieba.analyse
sentence = '中华蜜蜂原产于中国，是中国的土著蜂，适应中国各地的气候和蜜源条件，适于定地饲养且稳产，尤其是在南方山区，有着其他蜂种不可替代的地位'

seg_list = jieba.cut(sentence, cut_all=True)
print(", ".join(seg_list))
keywords = jieba.analyse.extract_tags(sentence, topK=20, withWeight=True, allowPOS=('n','nr','ns'))
print(keywords)
