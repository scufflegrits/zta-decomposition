"""Put the numbered tool directory on the import path; a numeric prefix cannot be a package name."""
from pathlib import Path
import sys

TOOLS = Path(__file__).resolve().parents[1] / '110_tools'
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))
