import nltk 
nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
import numpy as np
import torch 
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

stemmer=PorterStemmer()


def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    sentence_words = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag