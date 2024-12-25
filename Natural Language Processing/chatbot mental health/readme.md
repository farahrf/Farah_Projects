# Chatbot for Mental Health

This project involves developing a chatbot designed to assist with mental health queries and provide supportive responses. The project files include various scripts and data files required for building and training the chatbot.

## Project Files

### chat.py
This script handles the interaction with the user. It loads the trained model and uses it to generate responses based on user input.

### data.pth
This file contains the saved model weights. It is used to load the trained model for generating responses.

### intents.json
This JSON file contains the predefined intents that the chatbot can recognize. Each intent includes a set of patterns, responses, and tags.

### model.py
This script defines the architecture of the neural network used for the chatbot. It includes the model definition and necessary functions for building the model.

### nltk_utils.py
This script includes utility functions for natural language processing tasks, such as tokenization, stemming, and bag-of-words conversion.

### train.py
This script is used to train the chatbot's neural network. It processes the data, builds the model, and saves the trained model weights.

## Tools and Libraries

The following tools and libraries are used in this project:

- **NumPy**: For numerical operations.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib**: For data visualization.
- **Seaborn**: For statistical data visualization.
- **NLTK**: For natural language processing tasks such as tokenization and stemming.
- **PyTorch**: For building and training the neural network model.
- **JSON**: For handling the intents data.
- **Sklearn**: For machine learning preprocessing and evaluation metrics.
- **Yellowbrick**: For visualizing machine learning model performance.

## Workflow

1. **Data Preparation**: 
   - The `intents.json` file is used to define the intents, patterns, and responses. 
   - The data is preprocessed using NLTK utilities to convert text into numerical data that can be fed into the model.

    ```python
    import json
    from nltk_utils import tokenize, stem, bag_of_words
    import numpy as np
    ```

2. **Model Training**:
    - The `train.py` script processes the data, builds the neural network model defined in `model.py`, and trains it using the patterns and tags from `intents.json`.
    - The trained model is then saved to `data.pth`.

    ```python
    import torch 
    import torch.nn as nn
    from torch.utils.data import Dataset, DataLoader
    from model import NeuralNet
    ```

3. **Chatbot Interaction**:
    - The `chat.py` Flask script loads the trained model and uses it to interact with users.
    - It processes user input, predicts the intent using the model, and generates a response based on the predicted intent.

4. **Utility Functions**:
    - The `nltk_utils.py` script provides utility functions for text preprocessing, including tokenization, stemming, and bag-of-words conversion.

5. **Model Implementation**:
    - The `model.py` script contains the neural network architecture and necessary functions for building the model.

6. **Training the Model**:
    - The `train.py` script is used to train the model with the prepared data and save the trained weights.

## Conclusion

The chatbot for mental health is designed to provide supportive responses based on predefined intents and patterns. It utilizes natural language processing and machine learning techniques to understand user input and generate appropriate responses. This project aims to assist individuals seeking mental health support by providing an accessible and responsive tool for initial queries and support.
