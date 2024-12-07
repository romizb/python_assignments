import sys
from collections import Counter

#if len(sys.argv) < 2: #makes sure what we enter into the terminal more than 2 values (one the program, one the file)
 #       exit(f"to use this program write: python {sys.argv[0]} <filename> <filename> ...") #how to input

def statistics_NTP(sequence):
    sequence = sequence.upper() #so that it is not case sensative 
    counts = Counter(sequence)
    total = sum(counts.values())
    stats = {
        "A": counts.get("A", 0),
        "C": counts.get("C", 0),
        "G": counts.get("G", 0),
        "T": counts.get("T", 0),
        "Unknown": total - (counts.get("A", 0) + counts.get("C", 0) + counts.get("G", 0) + counts.get("T", 0)),
        "Total": total
    }
    print(f"{stats}")
    return stats


def display_statistics(stats, label):
    print(label)
    for base in ["A", "C", "G", "T", "Unknown"]:
        count = stats[base]
        percentage = (count / stats["Total"]) * 100 if stats["Total"] > 0 else 0
        print(f"{base}: {count:>8} {percentage:5.1f}%")
    print(f"Total: {stats['Total']:>6}\n")

def main(files):
    overall_counts = Counter()
    for file in files:
        with open(file, 'r') as f:
            sequence = f.read().strip()
        stats = statistics_NTP(sequence)
        display_statistics(stats, f"{file}")
        overall_counts.update(Counter(sequence.upper())) #so not case sensative
    
    overall_stats = statistics_NTP(overall_counts.elements())
    display_statistics(overall_stats, "All")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python seq.py <file1> <file2> ...")
        sys.exit(1)
    main(sys.argv[1:])
