import os
from pathlib import Path

from utils.common import filename_by_extension, extract_filename


def test_filename_by_extension():
    file_path = os.path.join(Path(os.path.abspath(__file__)).parent, "io")
    results = filename_by_extension(file_path, "fa")
    assert len(results), 2


def test_extract_filename():
    file_path = os.path.join(
        Path(os.path.abspath(__file__)).parent, "io/one_sequence.fa"
    )
    results = extract_filename(file_path)
    assert ("one_sequence", ".fa") == results
