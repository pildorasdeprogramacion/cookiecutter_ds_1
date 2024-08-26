from {{ cookiecutter.module_name }}.config import MODELS_DIR, PROCESSED_DATA_DIR

features_path = PROCESSED_DATA_DIR / "features.csv",
labels_path = PROCESSED_DATA_DIR / "labels.csv",
model_path = MODELS_DIR / "model.pkl",