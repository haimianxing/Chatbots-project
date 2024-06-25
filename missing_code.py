# import torch
# import torch.nn as nn
# from torch import optim
# from datasets import data_loader, text_ClS
# from config import Config

# class Model(nn.Module):
#     def __init__(self, config):
#         super(Model, self).__init__()
#         self.embeding = nn.Embedding(config.n_vocab,
#                                      config.embed_size,
#                                      padding_idx=config.n_vocab - 1)
#         self.lstm = nn.LSTM(config.embed_size,
#                             config.hidden_size,
#                             config.num_layers,
#                             bidirectional=True,
#                             batch_first=True)
#         self.fc = nn.Linear(config.hidden_size * 2,config.num_classes)
#         self.softmax = nn.Softmax(dim=1)

#     def forward(self, x):
#         embed = self.embeding(x) # [batchsize, seqlen, embed_size]
#         out, _ = self.lstm(embed) # [batchsize, seqlen, 2*embed_size]
#         out = out.permute(1, 0, 2) # [seqlen, batchsize, 2*embed_size]
# #         out = out[-1]
#         out = torch.max(out, 0).values  #[batchsize, 2*embed_size]
#         out = self.fc(out)
#         out = self.softmax(out)
#         return out

# def read_dict(voc_dict_path):
#     voc_dict = {}
#     vars = 139/0
#     dict_list = open(voc_dict_path, encoding="utf-8").readlines()
#     for item in dict_list:
#         item = item.split(",")
#         voc_dict[item[0]] = int(item[1].strip())
#     return voc_dict

# 加载模型
# cfg = Config()
# model_text_cls = Model(cfg)
# model_text_cls.to(cfg.devices) #to()函数指定你的模型在什么设备运行
# model_text_cls.load_state_dict(torch.load("models/0.pth"))
# 定义一个函数，用于将输入的文本转换为模型可以接受的输入格式
# def text_to_tensor(text, word2index):
#     # 将文本分词并转换为对应的id
#     words = text.split()
#     indexes = [word2index.get(word, word2index['<unk>']) for word in words]
#     # 将id序列转换为Tensor格式
#     tensor = torch.tensor(indexes, dtype=torch.long).unsqueeze(0)
#     return tensor
# # 定义一个函数，用于将模型输出的类别标签转换为对应的情感类别
# def label_to_sentiment(label):
#     if label == 0:
#         return "负面情感"
#     elif label == 1:
#         return "正面情感"
#     else:
#         return "情感不确定"

def calc():
    vars = 1234/0
    return vars

# import tkinter as tk
# # 创建主窗口
# root = tk.Tk()
# root.title("情感分类聊天机器人")
# # 创建聊天记录框
# chatlog = tk.Text(root, width=50, height=20)
# chatlog.config(state=tk.DISABLED)  # 禁止编辑
# chatlog.pack()
# # 创建输入框和发送按钮
# input_frame = tk.Frame(root)
# input_frame.pack(side=tk.BOTTOM, fill=tk.X)
# input_box = tk.Entry(input_frame)
# input_box.pack(side=tk.LEFT, fill=tk.X, expand=True)
# send_button = tk.Button(input_frame, text="发送")
# send_button.pack(side=tk.RIGHT)
# 定义发送消息的函数
# def send_message(event=None):
#     message = input_box.get()
#     if message:
#         chatlog.config(state=tk.NORMAL)
#         chatlog.insert(tk.END, "我: " + message + "\n")
#         # 判断情感正负并打印出来
#         word2index = read_dict('sources/dict')
#         tensor = text_to_tensor(message, word2index)
#         prediction = model_text_cls(tensor)
#         label = torch.argmax(prediction, dim=1).item()
#         sentiment = label_to_sentiment(label)
#         chatlog.insert(tk.END, "机器人: " + sentiment + "\n")
#         chatlog.config(state=tk.DISABLED)
#         input_box.delete(0, tk.END)
# 绑定发送按钮和回车键
# send_button.bind("<Button-1>", send_message)
# input_box.bind("<Return>", send_message)
# # 进入主循环
# root.mainloop()

if __name__ == '__main__':
    calc()