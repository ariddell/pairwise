from __future__ import unicode_literals

import itertools
import random


def collect_votes(choices):
    """Gather votes for alternatives using pairwise comparisons

    Parameters
    ----------
    choices : iterable of str

    Returns
    -------
    ranking : tuple of int
    """
    choices = list(choices)
    num_choices = len(choices)

    pairwise_mat = [[0] * num_choices for _ in range(num_choices)]
    for i, j in itertools.combinations(range(num_choices), 2):
        # randomly choose which choice to display first
        first = random.randint(0, 1)
        if first == 1:
            i, j = j, i
        print("Which do you prefer?")
        print("1: {}".format(choices[i]))
        print("2: {}".format(choices[j]))
        response = input("Enter 1 or 2: ")
        choice = i if int(response) == 1 else j
        if choice == i:
            pairwise_mat[i][j] += 1
        else:
            pairwise_mat[j][i] += 1
    votes = [sum(row) for row in pairwise_mat]
    return votes
