import nltk
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
factory = StemmerFactory()
stemmer = factory.create_stemmer()

import numpy
import tflearn
import tensorflow as tf
import random
import json
import pickle

scan = 0

with open("07 - intents.json") as file:
    data = json.load(file)


if scan == 0:
    # Diperbanyak Intentsnya Bukan Patternsnya
    # Dipercanggih Responses
    # Tag Diperbanyak + Dipercanggih

    with open("07 - data.pickle","rb") as f:
        words, labels, training, output = pickle.load(f)
elif scan == 1: 
    words = []
    labels = []
    docs_x = []
    docs_y = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds) # menambah nilai array dengan ciri khas extend (urutan, nilai)
            docs_x.append(wrds) # menambah nilai array dengan ciri khas append (ditaruh urutan paling belakang)
            docs_y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?" and w != "!"] # menhilangkan imbuhan
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = [] 
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)
        
        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = numpy.array(training)
    output = numpy.array(output)

    with  open("07 - data.pickle","wb") as f:
        pickle.dump((words, labels, training, output),f)


tf.compat.v1.get_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

if scan == 0:
    model.load("model.tflearn")
elif scan == 1:
    model.fit(training, output, n_epoch=10000, batch_size=8, show_metric=True)
    model.save("model.tflearn")


def bag_of_word(s,words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s) # membagi text mirip split tetap ada bedanya
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for x in s_words:
        for i, w in enumerate(words): # enumerate = memakai words tapi menggunakan w
            if w == x:
                bag[i] = 1
    
    return numpy.array(bag)

def chat():
    print("\nngobrol bareng comp ('quit' untuk keluar).")
    while True:
        inp = input("\tSaya: ")
        if inp.lower() == "quit":
            break

        result = model.predict([bag_of_word(inp,words)])[0]
        result_index = numpy.argmax(result)
        tag = labels[result_index]
        
        if result[result_index] > 0.5:    
            for tg in data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']
            
            print("\tComp:",random.choice(responses),"\n")
        else:
            print("\tComp: Maaf saya belum paham, saya masih butuh banyak belajar.\n")

chat()