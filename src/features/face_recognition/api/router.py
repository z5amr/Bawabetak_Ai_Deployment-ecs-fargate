"""FastAPI routes for the face recognition feature."""
from fastapi import APIRouter, UploadFile, File, HTTPException

from src.features.face_recognition.common.model_loader import get_face_app
from src.features.face_recognition.common.image_utils import read_image_from_upload
from src.features.face_recognition.common.schemas import DetectResponse, EmbeddingResponse

router = APIRouter(prefix="/face-recognition", tags=["Face Recognition"])


@router.post("/detect-faces", response_model=DetectResponse)
async def detect_faces(image: UploadFile = File(...)):
    contents = await image.read()
    img = read_image_from_upload(contents)
    face_app = get_face_app()

    bboxes, _ = face_app.det_model.detect(img, max_num=0, metric="default")
    return DetectResponse(face_count=len(bboxes))


@router.post("/get-embedding", response_model=EmbeddingResponse)
async def get_embedding(image: UploadFile = File(...)):
    contents = await image.read()
    img = read_image_from_upload(contents)
    face_app = get_face_app()

    faces = face_app.get(img)

    if len(faces) == 0:
        raise HTTPException(status_code=422, detail="No face detected")
    if len(faces) > 1:
        raise HTTPException(status_code=422, detail="Multiple faces detected, expected exactly one")

    return EmbeddingResponse(embeddings=faces[0].embedding.tolist())
