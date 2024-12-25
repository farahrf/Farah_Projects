# Cable Detection Projects

This repository contains projects focused on cable detection using computer vision techniques. The projects are divided into two main sections: **RCNN** and **YOLOv8**.

## RCNN

The RCNN section focuses on using Region-based Convolutional Neural Networks (RCNN) for cable detection. This section includes three main Jupyter notebooks:

1. **Making_masks.ipynb**
2. **base_model.ipynb**
3. **model_building.ipynb**

### Making_masks.ipynb

In this notebook, masks are created for the dataset using COCO (Common Objects in Context) tools. The process involves loading COCO annotations, generating masks, and saving them in the appropriate format. The key libraries used include `pycocotools` and `PIL` (Python Imaging Library).

### base_model.ipynb

This notebook is dedicated to building the base model for RCNN using Keras and TensorFlow. It involves defining custom layers and blocks such as `EncoderBlock`, `DecoderBlock`, and `AttentionGate`. These components are then assembled to create a robust RCNN model capable of detecting cables in images.

### model_building.ipynb

Continuing from the base model, this notebook includes steps for training and evaluating the model. It covers data loading, preprocessing, defining custom callbacks for monitoring progress, and using metrics to assess the model's performance. Key tools used include `pandas`, `glob`, `tensorflow`, and `opencv`.

## YOLOv8

The YOLOv8 section focuses on using You Only Look Once version 8 (YOLOv8) for cable detection. This section includes four main Jupyter notebooks:

1. **convertToTflite.ipynb**
2. **realtime_detection.ipynb**
3. **test.ipynb**
4. **yolov8-detection-model.ipynb**

### convertToTflite.ipynb

This notebook involves converting the YOLOv8 model to TensorFlow Lite format for deployment on edge devices. The conversion process ensures that the model can run efficiently on devices with limited computational resources.

### realtime_detection.ipynb

This notebook focuses on real-time cable detection using the YOLOv8 model. It demonstrates how to set up real-time video capture and perform detection, displaying the results on the screen. This is achieved using OpenCV for video handling and TensorFlow Lite for inference.

### test.ipynb

In this notebook, the YOLOv8 model is tested on a dataset to evaluate its performance. It involves loading test images, performing detection, and calculating performance metrics to assess the accuracy and efficiency of the model.

### yolov8-detection-model.ipynb

This notebook involves building and training the YOLOv8 model for cable detection. It covers defining the YOLOv8 architecture, loading and preprocessing the training data, training the model, and saving the trained model for future use.

## Conclusion

This repository provides comprehensive solutions for cable detection using both RCNN and YOLOv8. The RCNN approach focuses on region-based detection, while YOLOv8 offers a more streamlined and efficient detection pipeline. Both methods leverage the power of Keras, TensorFlow, and OpenCV for building and deploying robust computer vision models.
