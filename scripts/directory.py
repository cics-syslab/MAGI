import sys
from pathlib import Path

magi_path = Path(__file__).resolve().parent.parent

if magi_path not in sys.path:
    sys.path.append(str(magi_path))
