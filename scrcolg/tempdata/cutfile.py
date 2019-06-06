import csv
import os, codecs
import jieba
from collections import Counter


def clean_words():

    for word in open('nouse.txt'):
        jieba.del_word(word.replace('\n',''))

def get_words(txt):
    clean_words()
    seg_list = jieba.cut(txt, HMM=True)
    c = Counter()
    for x in seg_list:
        if len(x) > 1 and x != '\r\n' and x!='kankan' and x!='...':
            c[x] += 1
    print('常用词频度统计结果')
    csvfile = open("result.csv",'w')

    writer= csv.writer(csvfile)
    writer.writerow(["单词", "数量"])
    for (k, v) in c.most_common(200):
        writer.writerow([k,v])
        print('%s %d' % (k,v))


if __name__ == '__main__':
    with codecs.open('counttopic', 'r') as f:
        txt = f.read()
    get_words(txt)
