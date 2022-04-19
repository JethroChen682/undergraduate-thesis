import torch
from torch.autograd import Variable
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import torch.nn as nn
#提取数据
file='Data.xlsx'
df=pd.read_excel(file)
df=df.iloc[:,4:]
df_norm = (df - df.min()) / (df.max() - df.min())
x=df_norm.iloc[:,0:4]
y=df_norm.iloc[:,4]
#to tensor
x=x.values
y=y.values
x = torch.tensor(x)
y = torch.tensor(y)
x=x.to(torch.float32)
y=y.to(torch.float32)
y=torch.unsqueeze(y,1)

#神经网络训练
net=nn.Sequential(
    nn.Linear(4,20),
    nn.ReLU(),
    nn.Linear(20, 40),
    nn.Tanh(),
    nn.Linear(40, 20),
    nn.ReLU(),
    nn.Linear(20,1)
)

cri=torch.nn.MSELoss()
opt=torch.optim.Adam(net.parameters())
net.train()
for e in range(1,1000):
    y_=net(x)
    loss=cri(y_,y)
    opt.zero_grad()
    loss.backward()
    opt.step()
    if e%20==0:
        print(f"e:{e} loss:{loss.data}\n")
torch.save(net,r"bpnn1.pth")