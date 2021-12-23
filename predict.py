from PIL import Image
from keras.preprocessing.image import load_img, img_to_array
import numpy as np
from keras.models import load_model

model = load_model('./pd_model.hdf5', compile=False)
kelas = {0:'Panik', 1:'Tidak Panik'}
def process_image(img_path):
    img = load_img(img_path, target_size=(150,150))
    img = img_to_array(img)
    img = np.expand_dims(img, [0])
    prediction = model.predict(img)
    y_class = prediction.argmax(axis=-1)
    y = " ".join(str(x) for x in y_class)
    y = int(y)
    res = kelas[y]
    return res