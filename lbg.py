"""
lbg.py  --  OWNER: Member A
Codebook generation using the LBG algorithm with splitting (Lecture 8).

Conventions (shared by everyone):
  - blocks   : NumPy array of shape (N, bh*bw), each row is one flattened block
  - codebook : NumPy array of shape (k, bh*bw)
  - indices  : NumPy array of shape (N,), integers from 0 to k-1
"""
import numpy as np


def distance(block, codeword):
    """TODO: return the distance between one block and one codeword.
    - Decide on the measure and document it (the lecture example uses
      the sum of absolute differences)."""
    raise NotImplementedError


def nearest_index(blocks, codebook):
    """TODO: return indices (N,) = index of the closest codeword for every block.
    - On a tie, pick the first codeword (as in the lecture)."""
    raise NotImplementedError


def recompute_centroids(blocks, indices, codebook):
    """TODO: return new_codebook = average of the blocks assigned to each codeword.
    - Decide what to do with an EMPTY cluster (no blocks assigned) and
      document it."""
    raise NotImplementedError


def split_codeword(codeword):
    """TODO: return (codeword_low, codeword_high) from one codeword.
    - Use the lecture rule (rounded average, +/- 1 offset)."""
    raise NotImplementedError


def build_codebook(blocks, k):
    """TODO: return codebook (k, bh*bw).
    Steps:
      1. Start with one codeword = average of all blocks.
      2. Split every codeword into two.
      3. Assign blocks to nearest codeword, recompute centroids,
         repeat until the assignments stop changing.
      4. Repeat from step 2 until the codebook has k codewords.
    Edge cases to handle:
      - k that is not a power of 2
      - k larger than the number of blocks
    """
    raise NotImplementedError
