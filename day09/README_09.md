# Sequence Analysis Tool

This tool analyzes DNA sequences for specific features. It currently supports:

1. Finding the longest repeated subsequence in the DNA sequence that appears twice.
2. Calculating the GC content of the DNA sequence.

## Installation

1. Clone the program (analyze.py).
2. Install dependencies:
```
 pip install -r requirements.txt
```


## Usage

Run the program with the desired options (either or both):
```
python analyze.py FILE [--duplicate] [--gc-content]
```
•	FILE: Path to the file containing DNA sequences in Fasta or GenBank format.

•	--duplicate: Finds and prints the longest repeated subsequence.

•	--gc-content: Calculates and prints the GC content of the sequence.


## Dependencies

•	biopython: Used for parsing Fasta and GenBank files.

Install it using pip:
```
pip install biopython
```


