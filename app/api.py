from fastapi import FastAPI, UploadFile, File
import tempfile
import shutil

from pipeline.detector import Detector

app = FastAPI(title="ExoDetect-AI")

detector = Detector()


@app.get("/")
def home():
    return {"message": "ExoDetect-AI API Running"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".fits"
    ) as temp:

        shutil.copyfileobj(file.file, temp)

        path = temp.name

    result = detector.detect(path)

    return result