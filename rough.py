import torch
x=torch.randint(0,5,size=(2,5))
print(x)
print(torch.unique(x,dim=0))