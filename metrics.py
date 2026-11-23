"""
metrics.py  --  OWNER: Member C
Compression ratio and error measurement (same method as Lecture 8).
"""
import numpy as np


def bits_per_index(k):
    """TODO: return ceil(log2(k))."""
    raise NotImplementedError


def compression_ratio(h, w, bh, bw, k):
    """TODO: return (ratio, original_bits, compressed_bits).
    - original   = h * w * 8
    - compressed = codebook bits + (number of blocks * bits per index)
    - ratio      = original / compressed
    - Decide whether padded size and header bytes are counted; document it."""
    raise NotImplementedError


def mse(original, reconstructed):
    """TODO: return the mean squared error between the two images."""
    raise NotImplementedError
