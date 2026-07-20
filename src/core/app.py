from fastapi import FastAPI
from src.features.face_recognition.api.router import router as face_recognition_router

app = FastAPI(title="face_recognition_api")

app.include_router(face_recognition_router)