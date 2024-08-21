from django.shortcuts import render
from django.http.response import HttpResponse
import pandas as pd
import numpy as np
import pickle
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
import os
from django.conf import settings
import pickle
filepath = os.path.join(settings.BASE_DIR, 'news', 'real_news.pkl')
print(filepath)
if os.path.exists(filepath):
    with open(filepath, 'rb') as f:
        model = pickle.load(f)
else:
    print('File not present at desired path')
# with open('D://fakenews//fakenews//fakenews//news//news. pkl', 'rb') as f:
#     model = pickle.load(f)

def home(request):
    prediction = None
    accuracy = None

    if request.method == 'POST':
        news = request.POST['news']
        tokenizer = Tokenizer(num_words=10000)
        tokenizer.fit_on_texts([news])
        maxlen = 1000
        test_tokenized = tokenizer.texts_to_sequences([news])
        test_tokenized = pad_sequences(test_tokenized, maxlen=maxlen)
        pred = model.predict(test_tokenized)
        pred = pred[0]

        if pred >= 0.5:
            prediction = 'Real News'
            accuracy = f"{pred * 100}%"
        else:
            prediction = 'Fake News'
            accuracy = f"{(1 - pred) * 100}%"

        return render(request, 'display.html', {'prediction': prediction, 'accuracy': accuracy, 'news': news})
    else:
        return render(request, 'home.html')

def display(request):
    return render(request, 'display.html')