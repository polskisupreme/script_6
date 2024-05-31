from Bio.Align import PairwiseAligner


def find_alignments(seq_a, seq_b):
    aligner = PairwiseAligner()
    aligner.mode = 'local'
    aligner.match_score = 1
    aligner.mismatch_score = -1
    aligner.open_gap_score = -1
    aligner.extend_gap_score = -1

    alignments = aligner.align(seq_a, seq_b)

    for alignment in alignments:
        if '.' in alignment.format().split('\n')[1]:
            print(alignment.format())


# Przykładowe sekwencje
seq_a = "AACCTTGGAA"
seq_b = "AAACCCTGG"

# Wywołanie funkcji znajdowania dopasowań
find_alignments(seq_a, seq_b)
