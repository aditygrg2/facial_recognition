# Facial Recoginition using Siamese Neural Networks 

I always thought that do one shot networks really work? They take really less data as compared to other CNNs and still give awesome results. So I tried to implement [Siamese Neural Networks for One-shot Image Recognition](https://www.cs.cmu.edu/~rsalakhu/papers/oneshot1.pdf) by G. Koch, R. Zemel, and R. Salakhutdinov. A really brilliant paper to detect similarity between two entities. Though, the implementation is not exact same, because of lack of good computing resources, but the core idea is to divide the input into two, predicting probability score to depict their similarity.

<img width="948" alt="Siamese Neural Networks for One-shot Image Recognition" src="https://github.com/aditygrg2/facial_recoginition/assets/98523623/ee109059-fdc3-4cfb-aa90-17a681c5b185">

[Source](https://www.cs.cmu.edu/~rsalakhu/papers/oneshot1.pdf)

## Model

The model looks like this - 

![model](https://github.com/aditygrg2/facial_recoginition/assets/98523623/173cd541-0e38-41ef-baf1-2bed8326b666)

Though in the real paper, more deep model with more trainable parameters is used. But still it gives much good results. 

** Loss Metric Used ** : Binary Crossentropy

## Data Sources

Three types of data is needed to train SNNs. 

1. Anchor Samples
2. Positive Samples
3. Negative Samples

To train, Anchor Samples and Positive Samples are inputted with class label as 1. Similarly, Anchor Samples and Negative Samples are inputted with class labels as 0.

For Anchor Samples and Positive Samples I used my own images using webcam, using CV2. The code for generating the data can be found in img_generator.ipynb
For Negative Samples I used one of the famous face dataset [Labeled Faces in the Wild](http://vis-www.cs.umass.edu/lfw/) to get some negative images.

## Folder Structure

The faces of any image is generated using haar-like features. I used a pre-trained haar on frontal face provided by CV2 (Thanks to OpenCV)

To use this, please create 6 folders namely - 
- anchor_grayed
- anchor_real
- negative_grayed
- negative_real
- positive_grayed
- positive_real

To generate negative images, download the [Labeled Faces in the Wild](http://vis-www.cs.umass.edu/lfw/) dataset and provide the path of the folder in the get_lfw_data.py file. It will transfer all the files from the subdirectories to the negative_real folder. Make sure that the get_lfw_data.py file is in the same folder as the folders.

To generate positive and anchor samples, just use img_generator.ipynb if you want to use your own images, else you can also use images from any other source.

Loss Analysis:

![output](https://github.com/aditygrg2/facial_recoginition/assets/98523623/8030a01b-9786-4ee2-a3de-a64a9c49655e)

Final Results:

https://github.com/aditygrg2/facial_recoginition/assets/98523623/f42e1bd9-3e69-42d9-ba8c-800f270dec9b
