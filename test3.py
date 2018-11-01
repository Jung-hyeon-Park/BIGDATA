import test2 as game
import sys, os
from PIL import Image
import numpy as np

if len(sys.argv) <= 1:
    print("game-checker.py(<파일이름>)")
    quit()


image_size = 50
categories = ["PS4 본체", "PSVita 본체", "PS4 라스트 오브 어스", "PS4 철권7", "XBOXONE 철권7"]


# 입력 이미지 numpy로 변환
X = []
files = []

for fname in sys.argv[1:]:
    img = Image.open(fname)
    img = img.convert("RGB")
    img = img.resize((image_size, image_size))

    in_data = np.asarray(img)

    X.append(in_data)
    files.append(fname)

X = np.array(X)

#CNN 모델 구축
model = game.build_model(X.shape[1:])
model.load_weights("./image/game-model.hdf5")

#데이터 예측
html = ""
pre = model.predict(X)
for i, p in enumerate(pre):
    y = p.argmax()
    print("+입력 : ", files[i])
    print("|게임 이름 : ", categories[y])
