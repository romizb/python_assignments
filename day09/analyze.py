import re
import argparse
from Bio import SeqIO

def find_longest_repeated_subsequence(sequence):
    """
    Finds the longest subsequence that repeats itself in the given sequence using regular expressions.
    """
    n = len(sequence)
    longest = ""
    for length in range(1, n // 2 + 1):
        for i in range(n - length + 1):
            subseq = sequence[i:i + length]
            pattern = re.compile(subseq)
            if len(pattern.findall(sequence)) > 1 and len(subseq) > len(longest):
                longest = subseq
    return longest

def calculate_gc_content(sequence):
    """
    Calculates the GC content of a DNA sequence.
    """
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    return (g_count + c_count) / len(sequence) * 100 if len(sequence) > 0 else 0

def main():
    parser = argparse.ArgumentParser(description="Analyze DNA sequences.")
    parser.add_argument("file", help="Path to the file in Fasta or GeneBank format.")
    parser.add_argument("--duplicate", action="store_true", help="Find the longest repeated subsequence.")
    parser.add_argument("--gc-content", action="store_true", help="Calculate GC content of the sequence.")
    
    args = parser.parse_args()

    # Read sequence from the file
    try:
        record = next(SeqIO.parse(args.file, "fasta"))  # Assumes FASTA format
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    sequence = str(record.seq)
    
    if args.duplicate:
        longest_subsequence = find_longest_repeated_subsequence(sequence)
        print(f"Longest repeated subsequence: {longest_subsequence}")
    
    if args.gc_content:
        gc_content = calculate_gc_content(sequence)
        print(f"GC content: {gc_content:.2f}%")

if __name__ == "__main__":
    main()
