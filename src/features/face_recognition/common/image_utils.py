import numpy as np
import cv2
from fastapi import HTTPException

MAX_SIZE = 5 * 1024 * 1024  # 5MB


def read_image_from_upload(file_bytes: bytes) -> np.ndarray:
    if len(file_bytes) > MAX_SIZE:
        raise HTTPException(status_code=413, detail="Image too large")
    
    np_arr = np.frombuffer(file_bytes, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    
    if img is None:
        raise HTTPException(status_code=400, detail="Invalid image file")
    return img