"""Training entrypoint for the face recognition model."""
from src.features.face_recognition.training import config
from src.features.face_recognition.training.dataset import load_dataset


def main():
    dataset = load_dataset(config.DATA_DIR)
    # TODO: build model (src/features/face_recognition/common/model_def.py),
    # train it, and save checkpoints to config.OUTPUT_DIR
    _ = dataset


if __name__ == "__main__":
    main()
