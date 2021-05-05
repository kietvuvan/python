import math
file1=open("doc1.txt",'r')
file2=open("doc2.txt",'r')
line1=file1.readline()
line2=file2.readline()

words_1=line1.split()
words_2=line2.split()

word_total=set(words_1).union(words_2)

dic_words_1=dict.fromkeys(word_total,0)
dic_words_2=dict.fromkeys(word_total,0)

for word in words_1:
    dic_words_1[word]+=1
for word in words_2:
    dic_words_2[word]+=1
def FT(t,d):
    f_dic_words={}

    for word, count in t.items():
        f_dic_words[word]=count/len(d)
    return f_dic_words

tf_dic_word1=FT(dic_words_1,words_1)
tf_dic_word2=FT(dic_words_2,words_2)

def IDF(list_doc):
    f_word_in_docs={}
    N=len(list_doc)
    f_word_in_docs=dict.fromkeys(list_doc[0],0)
    for doc in list_doc:
        for word, count in doc.items():
            if count>0:
                f_word_in_docs[word]+=1
    for word,count in f_word_in_docs.items():
        f_word_in_docs[word]=math.log(N/count)
    return f_word_in_docs

idf=IDF([dic_words_1,dic_words_2])
print(idf)
            
    