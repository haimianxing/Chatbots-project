import torch
import torch.nn as nn

from config import Config


class Model(nn.Module):
    def __init__(self, config):
        super(Model, self).__init__()
        self.embeding = nn.Embedding(config.n_vocab,
                                     config.embed_size,
                                     padding_idx=config.n_vocab - 1)
        self.lstm = nn.LSTM(config.embed_size,
                            config.hidden_size,
                            config.num_layers,
                            bidirectional=True,
                            batch_first=True)
        self.fc = nn.Linear(config.hidden_size * 2,config.num_classes)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        embed = self.embeding(x) # [batchsize, seqlen, embed_size]
        out, _ = self.lstm(embed) # [batchsize, seqlen, 2*embed_size]
        out = out.permute(1, 0, 2) # [seqlen, batchsize, 2*embed_size]
#         out = out[-1]
        out = torch.max(out, 0).values  #[batchsize, 2*embed_size]
        out = self.fc(out)
        out = self.softmax(out)
        return out

def read_dict(voc_dict_path):
    voc_dict = {}
    dict_list = open(voc_dict_path, encoding="utf-8").readlines()
    for item in dict_list:
        item = item.split(",")
        voc_dict[item[0]] = int(item[1].strip())
    return voc_dict

# 加载模型
cfg = Config()
model_text_cls = Model(cfg)
model_text_cls.to(cfg.devices) #to()函数指定你的模型在什么设备运行
model_text_cls.load_state_dict(torch.load("models/0.pth"))
# 定义一个函数，用于将输入的文本转换为模型可以接受的输入格式
def text_to_tensor(text, word2index):
    # 将文本分词并转换为对应的id
    words = text.split()
    indexes = [word2index.get(word, word2index['<unk>']) for word in words]
    # 将id序列转换为Tensor格式
    tensor = torch.tensor(indexes, dtype=torch.long).unsqueeze(0)
    return tensor
# 定义一个函数，用于将模型输出的类别标签转换为对应的情感类别
def label_to_sentiment(label):
    if label == 0:
        return "负面情感"
    elif label == 1:
        return "正面情感"
    else:
        return "情感不确定"

