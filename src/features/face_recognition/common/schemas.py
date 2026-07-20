"""Request/response models for the face recognition API."""
from pydantic import BaseModel
from typing import List


class DetectResponse(BaseModel):
    face_count: int


class EmbeddingResponse(BaseModel):
    embeddings: List[float]