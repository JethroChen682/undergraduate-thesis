import torch
from torch.autograd import Variable
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import torch.nn as nn
#load
net=torch.load('bpnn1.pth')
net.eval()
file='evalX.xlsx'
df=pd.read_excel(file)
x=df.values
x = torch.tensor(x)
x=x.to(torch.float32)
y=net(x)
pre=y.detach().numpy()
pre=pd.DataFrame(pre,columns=['迁入量(万人)'])
pre.to_excel('pre.xlsx')