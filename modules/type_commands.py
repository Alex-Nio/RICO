# Печать *************************************

# coding: utf-8
from __future__ import division

from punctuation import models
from punctuation import data
from punctuation import main

import sys
import codecs

import tensorflow as tf
import numpy as np

import keyboard
import config
from modules import tts


MAX_SUBSEQUENCE_LEN = 200
# model_file = r'/punctuation/model_ru_punctuator_h256_lr0.02.pcl'


def to_array(arr, dtype=np.int32):
    # minibatch of 1 sequence as column
    return np.array([arr], dtype=dtype).T


def convert_punctuation_to_readable(punct_token):
    if punct_token == data.SPACE:
        return " "
    else:
        return punct_token[0]


def restore(text, word_vocabulary, reverse_punctuation_vocabulary, model):
    i = 0
    while True:
        string_to_punct = ''
        subsequence = text[i:i+MAX_SUBSEQUENCE_LEN]

        if len(subsequence) == 0:
            break

        converted_subsequence = [word_vocabulary.get(
            w, word_vocabulary[data.UNK]) for w in subsequence]

        y = predict(to_array(converted_subsequence), model)

        string_to_punct += subsequence[0]

        last_eos_idx = 0
        punctuations = []
        for y_t in y:

            p_i = np.argmax(tf.reshape(y_t, [-1]))
            punctuation = reverse_punctuation_vocabulary[p_i]

            punctuations.append(punctuation)

            if punctuation in data.EOS_TOKENS:
                # we intentionally want the index of next element
                last_eos_idx = len(punctuations)

        if subsequence[-1] == data.END:
            step = len(subsequence) - 1
        elif last_eos_idx != 0:
            step = last_eos_idx
        else:
            step = len(subsequence) - 1

        for j in range(step):
            string_to_punct += (punctuations[j] +
                                " " if punctuations[j] != data.SPACE else " ")
            if j < step - 1:
                string_to_punct += subsequence[1+j]

        if subsequence[-1] == data.END:
            break

        i += step
    return(string_to_punct)


def predict(x, model):
    return tf.nn.softmax(net(x))


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
vocab_len = len(data.read_vocabulary(data.WORD_VOCAB_FILE))
x_len = vocab_len if vocab_len < data.MAX_WORD_VOCABULARY_SIZE else data.MAX_WORD_VOCABULARY_SIZE + \
    data.MIN_WORD_COUNT_IN_VOCAB
x = np.ones((x_len, main.MINIBATCH_SIZE)).astype(int)

print("Loading model parameters...")
net, _ = models.load(
    'punctuation\model_ru_punctuator_h256_lr0.02.pcl', x)

print("Building model...")

word_vocabulary = net.x_vocabulary
punctuation_vocabulary = net.y_vocabulary

reverse_word_vocabulary = {
    v: k for k, v in word_vocabulary.items()}
reverse_punctuation_vocabulary = {
    v: k for k, v in punctuation_vocabulary.items()}
for key, value in reverse_punctuation_vocabulary.items():
    if value == '.PERIOD':
        reverse_punctuation_vocabulary[key] = '.'
    if value == ',COMMA':
        reverse_punctuation_vocabulary[key] = ','
    if value == '?QUESTIONMARK':
        reverse_punctuation_vocabulary[key] = '?'


def execute_type_cmd(cmd: str, voice: str, new_data, counter):
    try:
        # ? ПЕЧАТЬ с команды "Напиши"
        if cmd == "type_cmd":
            print(f'"Команда:" {voice}')
            test = voice.split()
            test = [
                x for x in test if x not in config.VA_ALIAS]
            test = [
                x for x in test if x not in config.VA_TYPE['type_cmd']]
            test = " ".join(test)

            print(f'Строка для ввода:  {test}')

            input_text = test

            if len(input_text) == 0:
                sys.exit("Input file empty.")

            text = [w for w in input_text.split(
            ) if w not in punctuation_vocabulary and w not in data.PUNCTUATION_MAPPING and not w.startswith(data.PAUSE_PREFIX)] + [data.END]
            pauses = [float(s.replace(data.PAUSE_PREFIX, "").replace(">", ""))
                      for s in input_text.split() if s.startswith(data.PAUSE_PREFIX)]

            text_with_punct = restore(
                text, word_vocabulary, reverse_punctuation_vocabulary, net)
            import nltk.data
            punkt_tokenizer = nltk.data.load(
                'tokenizers/punkt/russian.pickle')
            sentences = punkt_tokenizer.tokenize(text_with_punct)
            sentences = [sent.capitalize() for sent in sentences]
            uppercase_text = ' '.join(sentences)
            print("Текст успешно откорректирован:", uppercase_text)

            keyboard.write(uppercase_text, delay=0)

    # ? Обработка ошибки если не выполнен запуск программы по ключевым словам
    except NameError:
        tts.va_speak("Произошла ошибка во время выполнения команды")
