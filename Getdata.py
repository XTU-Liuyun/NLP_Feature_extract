import os
import re
from nltk.stem import WordNetLemmatizer
category_num = {}
total_num = 0
words_list = list()

def TextClean(corpus):


    cleaned_text = re.sub(r'[.,;!]', '', corpus)
    cleaned_text = cleaned_text.lower()

    return cleaned_text

def Getdata():
    global total_num
    global category_num
    global words_list
    for filename in os.listdir('D:/TF_IDF/prodata'):
        if filename.endswith(".txt"):
            parts = filename.split('-')
            if parts[1][0].isdigit():
                with open(f'D:/TF_IDF/prodata/{filename}', encoding="utf-8") as file:
                    content = file.read()
                k = content[len(content)-1]
                total_num += 1
                if k not in category_num:
                    category_num[k] = 1
                else:
                    category_num[k] += 1
                processed_text = TextClean(content)
                # print(processed_text)
                # print(processed_text)
                # print('\n')
                lemmatizer = WordNetLemmatizer()
                lemmatized_text = ' '.join([lemmatizer.lemmatize(word) for word in processed_text.split()])
                words_list.append(lemmatized_text.split(' '))
                #print(words_list)

Getdata()
print("Total Number of Documents:", total_num)
print("Category Counts:", category_num)

