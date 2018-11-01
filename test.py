from flask import Flask, request
from flask_restful import Resource, Api
import random, math
from PIL import Image
import os, glob
import numpy as np



def add_sample(cat, fname, is_train):
    img = Image.open(fname)
    print("img = " + str(img))
    img = img.convert("RGB")
    img = img.resize((image_size, image_size))

    data = np.asarray(img)

    X.append(data)
    Y.append(cat)

    if not is_train: return

    for ang in range(-20, 20, 5):
        img2 = img.rotate(ang)
        data = np.asarray(img2)

        X.append(data)
        Y.append(cat)

        img2 = img2.transpose(Image.FLIP_LEFT_RIGHT)
        data = np.asarray(img2)

        X.append(data)
        Y.append(cat)

def make_sample(files, is_train):
    global X, Y

    X = []
    Y = []

    for cat, fname in files:
        add_sample(cat, fname, is_train)

    return np.array(X), np.array(Y)


#시작
root_dir = "./image/"
categories = ["PS4 본체", "PSVita 본체", "PS4 라스트 오브 어스", "PS4 철권7", "XBOXONE 철권7"]
nb_classes = len(categories)
image_size = 50

X = []
Y = []

allfiles = []
for idx, cat in enumerate(categories):
    image_dir = root_dir+"/"+cat
    files = glob.glob(image_dir+"/*.jpg")

    for f in files:
        allfiles.append((idx, f))

random.shuffle(allfiles)
th = math.floor(len(allfiles) * 0.6)

train = allfiles[0:th]
test = allfiles[th:]

X_train, Y_train = make_sample(train, True)
X_test, Y_test = make_sample(test, False)

xy = (X_train, X_test, Y_train, Y_test)
np.save("./image/game.npy", xy)
print("oK, ", len(Y_train))