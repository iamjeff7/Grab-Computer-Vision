# Grab-Computer-Vision
Classify car model and make

#### Steps:<br>
1. Download car dataset from Stanford.<br>
2. Data Exploration.
    2.1 Get the labels.
    2.2 Match labels with index.
    2.3 Import train dataset.
    2.4 Visualize data.
    2.5 Take image just only in the bbox to reduce background noise.
    2.6 Save the images in folder corresponding to their label.
3. Import Efficientnet B0 image classifier.
4. Split data into train and test dataset.
5. Remove the original classes of Efficientnet and add 196 classes.
6. Set the model to be trainable.
7. Train the model.
8. Visualize result.
    8.1 ![alt text](http://url/to/img.png)
    8.2 Keras accuracy: 0.793333<br>
    8.3 Accuracy: 0.008881<br>
    8.4 Precision: 0.008881<br>
    8.5 Recall: 0.008929<br>
    8.6 F1: 0.007560<br>
