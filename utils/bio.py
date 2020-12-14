"""Commonly used Bio related functions. 

"""

from typing import List, Set, Dict, Tuple, Optional, Union, Iterable, Any


def unambiguous_dna_letters() -> str:
    """Uppercase IUPAC unambiguous DNA (letters GATC only)."""
    return "GATC"


def ambiguous_dna_letters() -> str:
    """Uppercase IUPAC ambiguous DNA."""
    return "GATCRYWSMKHBVDN"


def extended_dna_letters() -> str:
    """Extended IUPAC DNA alphabet.
    In addition to the standard letter codes GATC, this includes:
    - ``B`` = 5-bromouridine
    - ``D`` = 5,6-dihydrouridine
    - ``S`` = thiouridine
    - ``W`` = wyosine
    """
    return "GATCBDSW"


def protein_letters() -> str:
    """IUPAC protein alphabet of the 20 standard amino acids."""
    return "ACDEFGHIKLMNPQRSTVWY"


def is_valid_dna(sequence: str) -> bool:
    """Returns `True` if sequence is DNA otherwise `False`"""
    valid_bases = ["A", "T", "G", "C"]
    for base in sequence:
        if base not in valid_bases:
            return False
    return True


def extended_protein_letters() -> str:
    """Extended uppercase IUPAC protein single letter alphabet including X etc.
    In addition to the standard 20 single letter protein codes, this includes:
    - ``B`` = "Asx";  Aspartic acid (R) or Asparagine (N)
    - ``X`` = "Xxx";  Unknown or 'other' amino acid
    - ``Z`` = "Glx";  Glutamic acid (E) or Glutamine (Q)
    - ``J`` = "Xle";  Leucine (L) or Isoleucine (I), used in mass-spec (NMR)
    - ``U`` = "Sec";  Selenocysteine
    - ``O`` = "Pyl";  Pyrrolysine
    This alphabet is not intended to be used with ``X`` for Selenocysteine
    (an ad-hoc standard prior to the IUPAC adoption of ``U`` instead).
    """
    return "ACDEFGHIKLMNPQRSTVWYBXZJUO"


def reverse(sequence: str) -> str:
    """Returns a reversed string."""
    return sequence[::-1]


def complement(sequence: str) -> str:
    """Returns a complement of a DNA sequence."""
    complement_dict = {"A": "T", "C": "G", "T": "A", "G": "C"}
    sequences = list(sequence)
    sequences = [complement_dict[base] for base in sequences]
    return "".join(sequences)


def reverse_complement(sequence: str) -> str:
    """"Returns a reverse complement of a DNA sequence."""
    sequence = reverse(sequence)
    sequence = complement(sequence)
    return sequence


def gc_content(sequence: str) -> float:
    """Returns percent of 'Gs' and 'Cs' in the nucleotide sequence."""
    sequence = sequence.upper()
    gc_count = sequence.count("G") + sequence.count("C")
    gc_fraction = float(gc_count) / len(sequence)
    return 100 * gc_fraction


def restriction_enzymes() -> List[str]:
    import os
    from pathlib import Path

    re_file = os.path.join(
        Path(os.path.abspath(__file__)).parent, "restriction_enzymes.txt"
    )
    if not os.path.exists(re_file):
        msg = "You must include the file containing restriction enzymes"
        raise ValueError(msg)

    with open(re_file, "r") as fh:
        restriction_enzymes = [re_.strip() for re_ in fh.readlines()]
    return restriction_enzymes


# aka: parse_fasta_file
# aka: format_sequence_dictionary
def fasta_to_dictionary(f: str) -> List[Dict[str, str]]:
    """Converts a file containing sequence(s) in FASTA format into a list of dictionary.
    Eg: 
    - ">desc\nAGTAGTAGGATAA\n"  => [{'id': 'desc'; 'sequence': 'AGTAGTAGGATAA'}]
    - ">desc1\nAGTAGTAGGATAA\n>desc2\nAACGTAGTGGCAG\n" => [{'id': 'desc1'; 'sequence': 'AGTAGTAGGATAA}, {'id': 'desc2'; 'sequence': 'AACGTAGTGGCAG'}]
    """

    from pathlib import Path

    if not Path(f).is_file():
        print(f"File {f} does not exist.")

    sequences = []
    try:
        with open(f, "r") as fh:
            sequence_text = fh.read()

        if ">" in sequence_text:
            input_sequences = sequence_text.split(">")
            for i in input_sequences[1:]:

                if len(i) > 0:
                    description = i.split("\n")[0]
                    end_of_description = i.find("\n")

                sequence = i[end_of_description:].split()
                sequences.append({"id": description, "sequence": "".join(sequence)})
        else:
            sequences.append(
                {"id": "unknown_id", "sequence": "".join(sequence_text.split("\n"))}
            )
    except:
        raise IOError(f"Input file '{f}' is not accessible.")

    return sequences


def write_to_file(
    data: List[Dict[Any, Any]], filename: str, format: str = "fasta"
) -> None:
    """Writes the content of the `data` into a file of specific `format`"""
    from collections import abc

    if not data:
        raise ValueError("Requires a content/data to write to the file.")

    if not filename:
        raise ValueError("'filename' is required.")

    try:
        if isinstance(data, abc.Sequence):
            with open(filename, "w") as fh:
                for record_ in data:
                    dictionary_ = isinstance(record_, abc.Mapping)
                    if dictionary_:
                        header_ = record_["id"]
                        sequence_ = record_["sequence"]
                        if format == "fasta":
                            fh.write(f">{header_}\n{sequence_}\n")
                        else:
                            raise ValueError(f"{format} format is not available yet.")
                    else:
                        raise ValueError("dictionary-like object required!")
    except:
        msg = "Only input 'data' must be a list of dictionary-like object."
        raise TypeError(msg)


def generate_hash(input_: str) -> str:
    """Generates hash value for an input string."""

    import hashlib

    hash_map = {}

    hash_id = hashlib.sha224(input_.encode("utf-8")).hexdigest()
    hash_map[hash_id] = input_
    return hash_id


def generate_sequence_info(sequence: str, description: str = None) -> dict:
    """Converts a raw sequence into a dictionary
    containing randomly generate sequence_id, hash_id and description.
    """

    import random
    import string

    # NOTE: generate a random alphanumeric string of length 32 as `sequence id`
    sequence_id = "".join(
        [random.choice(string.ascii_letters + string.digits) for n in range(32)]
    )

    # NOTE: `description` is set to None by default
    # TODO: fasta header would replace the None value?
    description = None
    sequence = "".join(sequence.split())

    hash_id = generate_hash(sequence_id)

    # TODO: write a simple validation for
    # Protein - check against valid amino acid residues
    # DNA - check agains ATGC
    # `sequence_id` doesn't seem to be important here...
    # print(f"TODO: misssing validation for: {sequence_id}")

    data = {
        "hash_id": hash_id,
        "sequence_id": sequence_id,
        "description": description,
        "sequence": sequence,
    }
    return data
