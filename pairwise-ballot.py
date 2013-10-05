#!/usr/bin/env python
from __future__ import unicode_literals, print_function

import argparse
import io

import pairwise

if __name__ == "__main__":
    description = """Rank a list of alternatives"""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('filename', type=str,
                        help='file with alternatives (one per line)')
    args = parser.parse_args()

    # read in alternatives
    filename = args.filename
    choices = []
    with io.open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            choices.append(line.strip())

    # ranking is from least to most popular
    votes = pairwise.collect_votes(choices)
    print("-------")
    print("Ranking")
    print("-------")
    last = None
    for i, (votes, choice) in enumerate(sorted(zip(votes, choices))[::-1]):
        rank = i + 1  # 1-index
        if last == votes:
            rank -= 1
        print("{}, {} votes (rank {})".format(choice, votes, rank))
        last = votes
