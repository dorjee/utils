# Utils package

This package is a wrapper for some frequently used text parsing, i/o related
tasks, and common Bioinformatics functions. Currently, it includes two main modules:

* common - for all common parsing and file handling stuffs
* bio - for common Bioinformatics tasks

**This will continueously be updated with new updates**


### To install ```utils``` package, simply:
```bash
pip install git+https://gitlab.com/emaildorjee/utils
```

### How to use:

To import the modules:
```python
from utils import common, bio

unambiguous_dna = bio.unambiguous_dna_letters()
```

To import specific function within a module:
```python
# import from common
from utils.common import filename_by_extension

# import from bio
from utils.bio import unambiguous_dna_letters, fasta_to_dictionary, restriction_enzymes
```

To import the function that calculates melting temperature (Tm) of a sequence:
```python
from utils.tm import Tm_staluc

tm = Tm_staluc("CAGTCAGTACGTACGTGTACTGCCGTA")
```
