import torch.nn as nn
import torch
class video_loss(nn.Module):
    def __init__(self,ignore_index: int = 255):
        super().__init__()
        self.ignore_index=ignore_index

    

    def forward(self,ground_truth,prediction):
        #ground truth:tensor of shape Bx1xframes
        #prediction: tensor of shape Bx48xframes
        actions_present=torch.unique(ground_truth,dim=1)#dim:batchxnumber 
        num_classes=prediction.shape[1]
        all_classes=torch.arange(0,num_classes)
        loss=0
        for batch in ground_truth.shape[0]:

            actions_present=torch.unique(ground_truth[batch])
            batch_predictions=prediction[batch]
            actions_present_predictions=batch_predictions[actions_present]
            actions_present_predictions=torch.max(actions_present_predictions,dim=1)
            indices = torch.ones_like(all_classes, dtype = torch.uint8, device = 'cuda')
            for elem in actions_present:
                indices = indices & (all_classes != elem)  
            classes_not_prestnt = all_classes[indices] 
            
            actions_not_present_predictions=batch_predictions[classes_not_prestnt]
            actions_not_present_predictions=torch.max(actions_not_present_predictions,dim=1)
            loss=loss-torch.sum(torch.log(actions_present_predictions))-torch.sum(torch.log(1-actions_not_present_predictions))
        return loss






