import insightface

_face_app = None


def get_face_app():
    """Singleton loader"""
    global _face_app
    if _face_app is None:
        _face_app = insightface.app.FaceAnalysis(name="buffalo_l")
        _face_app.prepare(ctx_id=0, det_size=(640, 640))
    return _face_app