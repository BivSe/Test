import io
import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.applications import EfficientNetB1
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input, decode_predictions


@st.cache(allow_output_mutation=True)
def load_model():
    return [EfficientNetB0(weights='imagenet'), EfficientNetB1(weights='imagenet')]


def preprocess_image(img0):
    img = img0.resize((224, 224))
    img1 = img0.resize((240, 240))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    x1 = image.img_to_array(img1)
    x1 = np.expand_dims(x1, axis=0)
    x1 = preprocess_input(x1)
    return [x, x1]


def load_image():
    uploaded_file = st.file_uploader(label='Выберите изображение для распознавания')
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        st.image(image_data)
        return Image.open(io.BytesIO(image_data))
    else:
        return None


def print_predictions(preds):
    classes = decode_predictions(preds, top=3)[0]
    for cl in classes:
        st.write(cl[1], cl[2])


[model, model1] = load_model()


st.title('Тест классификации изображений в облаке Streamlit')
img = load_image()
result = st.button('Распознать изображение')
if result:
    [x, x1] = preprocess_image(img)
    preds = model.predict(x)
    preds1 = model1.predict(x1)
    st.write('**Результаты распознавания для EfficientNetB0:**')
    print_predictions(preds)
    st.write('**Результаты распознавания для EfficientNetB1:**')
    print_predictions(preds1)
