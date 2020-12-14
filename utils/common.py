"""Functions for all common tasks.
"""
import os
import sys
import time
from subprocess import check_output, CalledProcessError

from typing import List, Set, Dict, Tuple, Optional, Union, Iterable


def speed_test(func):
    """Decorator that prints to STDIO the total time taken for a method execution"""

    def wrapper(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        print(f"'{func.__name__}' took {time.time() - t1} sec.")


def compress_file(file_: str) -> None:
    """Compresses file using gzip"""
    try:
        check_output(["gzip", "-f", file_])
    except CalledProcessError as e:
        msg = f"Failed to gzip: {e.output.decode()}."
        print(msg)
    else:
        msg = f"Failed to execute 'gzip'."
        raise OSError(msg)
    finally:
        print(f"{file_} has been gzipped.")


def filename_by_extension(input_: str, extension: str) -> List[str]:
    """Returns a list of file(s) with the matching extension"""
    files = []
    if os.path.isdir(input_):
        files.extend(
            [
                os.path.join(input_, file_)
                for file_ in os.listdir(input_)
                if file_.endswith(extension)
            ]
        )
    elif os.path.isfile(input_):
        if input_.endswith(extension):
            files.append(input_)
    else:
        raise ValueError(f"No such input found: {input_}")

    if not files:
        msg = f"Input must be either a '{extension}'' file or a directory containing multiple '{extension}' files."
        raise FileNotFoundError(msg)

    return files


def extract_filename(path: str) -> Tuple[str, str]:
    """Returns the file name from the file path"""
    return os.path.splitext(os.path.split(path)[1])
