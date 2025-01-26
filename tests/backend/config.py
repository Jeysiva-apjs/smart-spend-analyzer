from pathlib import Path
import sys

parent_dir = str(Path(__file__).resolve().parent.parent.parent)
print("test - " + parent_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)