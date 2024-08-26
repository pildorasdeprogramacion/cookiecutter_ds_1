from {{ cookiecutter.module_name }}.config import MODELS_DIR, PROCESSED_DATA_DIR

features_path = PROCESSED_DATA_DIR / "test_features.csv",
model_path = MODELS_DIR / "model.pkl",
predictions_path = PROCESSED_DATA_DIR / "test_predictions.csv",