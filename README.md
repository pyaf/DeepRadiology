# DeepRadiology
Source code for Microsoft Code Fun Do Hackathon 2018 organized at IIT (BHU), Varanasi.

## Idea
To assist radiologists using deep learning. We aim to build a abnormality detection model to detect and predict abnormality in musculoskeletal radiographs, such a model could be utilized for worklist prioritization. In this scenario, the studies detected as abnormal could be moved ahead in the image interpretation workflow, allowing the sickest patients to receive quicker diagnoses and treatment.

## Product
We developed a 169 layer Dense Convolutional Neural Network ([DenseNet](https://arxiv.org/abs/1608.06993)) for predicting abnormality on musculoskeletal radiographs. The model was trained on [MURA](https://stanfordmlgroup.github.io/projects/mura/) dataset, achieving 79.41% accuracy on validation set. We developed a Django webserver with a basic user interface to upload and test radiographic images on our model. The Django site was hosted on a Microsof Azure Ubuntu virtual machine.

Trained model state is stored [here](https://github.com/pyaf/DeepRadiology/blob/master/densenet/v2.2.pth).

## Dependencies

* PyTorch 0.3
* Django 1.11
* Pillow 5.0.0

## How to run this project
* Install the dependencies by `pip install -r requirements.txt`
* run the server with `python manage.py runserver`

## The Team "Bhaukali"
* [Hemanth Sai](https://github.com/Hemanth73)
* [Srimukha Paturi](https://github.com/sm-iitbhu)
* Myself :)

*Feel free to raise an issue to know more about this project.*
