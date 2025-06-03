from importlib import resources
from pathlib import Path
import os
import sys


def main() -> None:
    ext = '.exe' if os.name == 'nt' else ''
    exe_path: Path = resources.files(__package__).joinpath('bin', 'mytool' + ext)
    os.execv(exe_path, [str(exe_path), *sys.argv[1:]])
