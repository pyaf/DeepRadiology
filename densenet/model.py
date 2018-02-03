import torch
import time
from torch.autograd import Variable
from .densenet import densenet169


model = densenet169(pretrained=True)
model.load_state_dict(torch.load('densenet/v2.2.pth', 
			map_location=lambda storage, loc: storage))

def predict(study):
    since = time.time()
    inputs = Variable(study)
    outputs = model(inputs)
    output = torch.mean(outputs)
    preds = output.data > 0.5
    time_elapsed = time.time() - since
    print('Time elapsed: {:.0f}m {:.0f}s'.format(
                time_elapsed // 60, time_elapsed % 60))
    return (output.data, preds)
