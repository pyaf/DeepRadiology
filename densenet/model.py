import os
import torch
import time
from torch.autograd import Variable
from .densenet import densenet169
from DeepRadiology.settings import BASE_DIR

model_path = os.path.join(BASE_DIR, 'densenet/v2.2.pth')
model = densenet169(pretrained=True)
model.load_state_dict(torch.load(model_path, 
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
