# src/common/paths.py
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_RAW = os.path.join(PROJECT_ROOT, "data", "raw")
DATA_PROCESSED = os.path.join(PROJECT_ROOT, "data", "processed")
BORDER_CSV = os.path.join(DATA_RAW, "us-border-crossings", "border-crossings.csv")
