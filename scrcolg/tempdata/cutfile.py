import csv
import os, codecs
import jieba
from collections import Counter


def clean_words():

    for word in open('nouse.txt'):
        jieba.del_word(word.replace('\n',''))

def same_word(word):
    if word=='dnf':
        return 'DNF'
    elif word == '普雷妮':
        return '普雷尼'
    elif word =='伊西丝':
        return '伊西斯'
    elif word == '王室':
        return "亡誓"
    elif word =='坐飞机':
        return '飞机'
    else:
        return word


def get_words(txt):
    clean_words()
    jieba.add_word('稳')
    seg_list = jieba.cut(txt, HMM=True)

    c = Counter()
    for x in seg_list:
        if len(x) > 1 and x != '\r\n' and x!='kankan' and x!='...':
            c[same_word(x)] += 1

    print('常用词频度统计结果')
    csvfile = open("result.csv",'w')

    writer= csv.writer(csvfile)
    writer.writerow(["单词", "数量"])
    for (k, v) in c.most_common(200):
        writer.writerow([k,v])
        print('%s %d' % (k,v))


if __name__ == '__main__':
    with codecs.open('countreply', 'r') as f:
        txt = f.read()
    get_words(txt)
