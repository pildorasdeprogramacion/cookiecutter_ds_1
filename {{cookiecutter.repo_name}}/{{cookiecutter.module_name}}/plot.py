from {{ cookiecutter.module_name }}.config import FIGURES_DIR, PROCESSED_DATA_DIR

input_path = PROCESSED_DATA_DIR / "dataset.csv",
output_path = FIGURES_DIR / "plot.png",