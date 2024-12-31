
import tkinter as tk

import torch

from datasets import read_dict
from demo import text_to_tensor, model_text_cls, label_to_sentiment

# 创建主窗口
root = tk.Tk()
root.title("情感分类聊天机器人")
# 创建聊天记录框
chatlog = tk.Text(root, width=50, height=20)
chatlog.config(state=tk.DISABLED)  # 禁止编辑
chatlog.pack()
# 创建输入框和发送按钮
input_frame = tk.Frame(root)
input_frame.pack(side=tk.BOTTOM, fill=tk.X)
input_box = tk.Entry(input_frame)
input_box.pack(side=tk.LEFT, fill=tk.X, expand=True)
send_button = tk.Button(input_frame, text="发送")
send_button.pack(side=tk.RIGHT)
# 定义发送消息的函数
def send_message(event=None):
    message = input_box.get()
    if message:
        chatlog.config(state=tk.NORMAL)
        chatlog.insert(tk.END, "我: " + message + "\n")
        # 判断情感正负并打印出来
        word2index = read_dict('sources/dict')
        tensor = text_to_tensor(message, word2index)
        prediction = model_text_cls(tensor)
        label = torch.argmax(prediction, dim=1).item()
        sentiment = label_to_sentiment(label)
        chatlog.insert(tk.END, "机器人: " + sentiment + "\n")
        chatlog.config(state=tk.DISABLED)
        input_box.delete(0, tk.END)
# 绑定发送按钮和回车键
send_button.bind("<Button-1>", send_message)
input_box.bind("<Return>", send_message)
# 进入主循环
root.mainloop()