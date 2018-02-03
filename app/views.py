from django.shortcuts import render
import torch
from torchvision import transforms
from PIL import Image
from io import BytesIO
from densenet.model import predict

data_transforms = transforms.Compose([
					transforms.Resize((224, 224)),
					transforms.ToTensor(),
					transforms.Normalize([0.485, 0.456, 0.406],
									 [0.229, 0.224, 0.225])])


def index(request):
	template_name = 'index.html'
	if request.method == 'POST':
		images_files = [request.FILES[file] for file in 
							request.FILES if "image" in file]
		images = []
		for img in images_files:
			image = Image.open(BytesIO(img.read()))
			image.convert('RGB')
			images.append(data_transforms(image))
		study = torch.stack(images)
		output, preds = predict(study)
		context = {'output': output.numpy()[0],
					'preds': preds.numpy()[0],
					'status': True}
		return render(request, template_name, context)
	return render(request, template_name)
