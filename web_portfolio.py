from flask import Flask, request
import numpy as np
import test2 as game
from PIL import Image
#import tensorflow as tf

app = Flask(__name__)

@app.route('/user', methods=['POST', 'GET'])
def get():
    name3 = request.args.get('fullName', type=str)
    #print("name3 = " + name3)

    names = 'C:/image_file/upload'+name3

    #print("names = " + names)

    image_size = 50
    categories = ["PS4 본체", "PSVita 본체", "PS4 라스트 오브 어스", "PS4 철권7", "XBOXONE 철권7"]

    # 입력 이미지 numpy로 변환
    X = []

    img = Image.open(names)
    img = img.convert("RGB")
    img = img.resize((image_size, image_size))

    in_data = np.asarray(img)

    X.append(in_data)
    files = names

    X = np.array(X)

    # CNN 모델 구축
    model = game.build_model(X.shape[1:])
    model.load_weights("./image/game-model.hdf5")

    # 데이터 예측
    pre = model.predict(X)

    for i, p in enumerate(pre):
        y = p.argmax()
        print("+입력 : ", files)
        print("|게임 이름 : ", categories[y])

        abc = str(categories[y])

    return abc

if __name__ == '__main__':
    app.run(debug=True)


