"""
利用当前语料库建立词典，需先对数据进行分词，并除语料库中的停用词，进而统计词典，再对词典进行编码
"""
import jieba

data_stop_path = "sources/hit_stopwords.txt"  #停用词文件
stops_word = []       #存储停用词
data_path = "sources/weibo_senti_100k.csv"   #语料库文件
voc_dict = {}             #保存词典

#读取停用词
stops_word = open(data_stop_path, encoding="utf-8").readlines()
stops_word = [line.strip() for line in stops_word]
stops_word.append(" ")  #将空格和换行符也加入停用词列表
stops_word.append("\n")
# for word in stops_word:
#     print(word)

#读取语料库, 进行分词，获取词汇，去除停用词,将词汇存入词典
data_list = open(data_path, encoding="utf-8").readlines()[1:]

for item in data_list:
    label = item[0]   #标签
    content = item[2:].strip() #微博内容
    seg_list = jieba.cut(content, cut_all=False)
    for seg_item in seg_list:
        if seg_item in stops_word:
            continue
        if seg_item in voc_dict.keys():
            voc_dict[seg_item] = voc_dict[seg_item] + 1
        else:
            voc_dict[seg_item] = 1
# print(voc_dict)

#去除词典中频次<1的词，对词典中的词进行倒序排序及编码，提取前1000个高频词汇
min_seq = 1
top_n = 1000
#添加两个特殊字符进入词典
UNK = "<UNK>" #字典中不存在的词，用UNK进行替换
PAD = "<PAD>"

voc_list = [item for item in voc_dict.items() if item[1] > min_seq]
voc_list= sorted(voc_list, key=lambda x:x[1], reverse=True) #根据词频高低从新进行排序
voc_list = voc_list[:top_n] #筛选出前top_n个词汇
# print(voc_list)

#从0-1001进行编码
voc_dict = {item[0]: idx for idx, item in enumerate(voc_list)}
# print(voc_dict)
#添加两个字段UNK和PAD的编码
voc_dict.update({
    UNK: len(voc_dict),
    PAD: len(voc_dict)+1
})

#保存词典到文件
# ff = open("sources/dict", "w", encoding="utf-8")
# for key in voc_dict.keys():
#     print(key, voc_dict[key])
#     ff.writelines("{},{}\n".format(key, voc_dict[key]))
# ff.close()