from {{ cookiecutter.module_name }}.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

input_path = RAW_DATA_DIR / "dataset.csv",
output_path = PROCESSED_DATA_DIR / "dataset.csv",