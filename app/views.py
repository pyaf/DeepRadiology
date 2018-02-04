from io import BytesIO

import torch
from PIL import Image
from django.shortcuts import render
from torchvision import transforms

from densenet.model import predict

data_transforms = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])])


def index(request):
    template_name = 'index.html'
    if request.method == 'POST':
        print(request.FILES)
        images_files = [request.FILES['images']]
        if not images_files:
            return render(request, template_name, {'status': "no_image"})
        images = []
        for img in images_files:
            image = Image.open(BytesIO(img.read()))
            image = image.convert('RGB')
            images.append(data_transforms(image))
        study = torch.stack(images)
        output, preds = predict(study)
        context = {'output': round(output.numpy()[0] * 100, 2),
                   'preds': "Normal" if preds.numpy()[0] == 0 else "Abnormal",
                   'status': "success"}
        return render(request, template_name, context)
    return render(request, template_name)
