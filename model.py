import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

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