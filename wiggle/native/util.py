from ctypes.util import find_library
from pathlib import Path
from typing import Optional, Type

from wiggle.codec import Codec


def find_native(codec: Type[Codec], path_arg: Optional[str]) -> Optional[str]:
    if path_arg:
        path: Path = Path(path_arg)
        path: Path = path / codec.get_libname()
        if path.is_file():
            return str(path)

    return find_library(codec.get_libname())
