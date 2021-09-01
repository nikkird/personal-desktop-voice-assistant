import nltk
from nltk.stem import WordNetLemmatizer
import pickle
import numpy as np
from keras.models import load_model
import json
import random

from backend import commands, stt
from backend.tts import Speak

lemmatizer = WordNetLemmatizer()
model = load_model('res/model/pva_model.h5')
intents = json.loads(open('res/data/intents.json').read())
words = pickle.load(open('res/data/words.pkl', 'rb'))
classes = pickle.load(open('res/data/classes.pkl', 'rb'))


def clean_up_sentence(sentence):
    # tokenize the pattern - array
    # sentence_words = nltk.wordpunct_tokenize(sentence)
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    # lemmatizer - links words with similar meaning to one word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


# return 0 or 1 bag of words array
def bow(sentence, wrds, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0] * len(wrds)
    for s in sentence_words:
        for i, w in enumerate(wrds):
            if w == s:
                # assign 1 if current word is in the vocabulary
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return np.array(bag)


def class_predictor(sentence, model_):
    # filter out predictions below a threshold
    p = bow(sentence, words, show_details=False)
    res = model_.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


def match_response(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    va_res = "okay"
    for response in list_of_intents:
        if response['tag'] == tag:
            if response['responses'] != "" or response['responses'] is not None:
                va_res = random.choice(response['responses'])
            break
    return va_res, tag


def fetch_response(msg):
    # print("got here")
    ints = class_predictor(msg, model)
    res, tag = match_response(ints, intents)
    return res, tag


def assistant_response(command):
    response, tag = fetch_response(command)
    Speak(response)
    if 'sleep' == tag:
        sleep_cmd = stt.sleep_command()
        return sleep_cmd
    else:
        commands.get_commands(tag, command)

"""
def run_assistant():
    while True:
        # command = wake_listener()
        command = input("ask >>")
        if command != '':
            res, tag = find_response(command)
            # print("Kara >" + res)
            commands.get_commands(tag, command)
"""