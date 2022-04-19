import scipy.io as scio
import numpy as np
dataFile = r"/Applications/matlabCode/data2000.mat"
data = scio.loadmat(dataFile)
df=np.array(data.values())
a=0