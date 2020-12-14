from utils.bio import unambiguous_dna_letters, fasta_to_dictionary, restriction_enzymes
from utils.tm import Tm_staluc


def test_unambiguous_dna_letters():
    results = unambiguous_dna_letters()
    assert results == "GATC"


def test_fasta_to_dictionary():
    import os
    from pathlib import Path
    from typing import Mapping

    input_file = os.path.join(
        Path(os.path.abspath(__file__)).parent, "io/two_sequences.fa"
    )
    results = fasta_to_dictionary(input_file)
    assert len(results) == 2
    for result in results:
        assert isinstance(result, Mapping) == True


def test_calculate_melting_temperature():
    sequence = "CAGTCAGTACGTACGTGTACTGCCGTA"
    result = Tm_staluc(sequence)
    assert round(result, 2) == 59.87
