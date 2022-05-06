class video_loss(nn.Module):
    def __init__(self,ignore_index: int = 255):

    

    def forward(self,ground_truth,prediction):
        #ground truth:tensor of shape Bx1xframes
        #prediction: tensor of shape Bx48xframes


