from pathlib import Path

import yaml


def load_yaml(relative_path: str):
    project_root = Path(__file__).resolve().parents[1]
    with open(project_root / relative_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)
