from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
from tensorflow.keras.models import load_model
from pydantic import BaseModel
import numpy as np
import io
from PIL import Image
from typing import List

app = FastAPI()

class PredictionResponse(BaseModel):
    predictions: List[float]

@app.get("/")
def greet():
    return {"message": "bonjour"}


def load():
    model_path = "best_model.h5"
    model = load_model(model_path, compile=False)
    return model

# Chargement du model
model = load()

def preprocess(img):
    img = img.resize((224, 224))
    img = np.asarray(img)
    img = np.expand_dims(img, axis=0)
    return img


@app.post("/predict")
async def predict(file: UploadFile):
    image_data = await file.read()

    # ouvrir l'image
    img = Image.open(io.BytesIO(image_data))

    # preprocessing
    img_processed = preprocess(img)

    # prediction

    predictions = model.predict(img_processed)
    rec = predictions[0][0].tolist()

    return PredictionResponse(predictions=[rec])