"""
tests/test_lecture_example.py  --  OWNER: Member C
Checks against the Lecture 8 worked example.

Image (6x6), block size 2x2, k = 4:
    1  2  7  9  4  11
    3  4  6  6  12 12
    4  9  15 14 9  9
    10 10 20 18 8  8
    4  3  17 16 1  4
    4  5  18 18 5  6
"""


def test_codebook():
    """TODO: expected codewords [2 3 4 5], [8 9 7 7], [4 10 11 11], [16 15 19 18]."""
    raise NotImplementedError


def test_mse():
    """TODO: expected MSE = 30/36 = 0.833."""
    raise NotImplementedError


def test_ratio_6x6():
    """TODO: expected ratio = 288/146 = 1.97."""
    raise NotImplementedError


def test_ratio_600x600():
    """TODO: same settings on a 600x600 image, expected ratio about 16:1."""
    raise NotImplementedError


def test_padding_roundtrip():
    """TODO: image size not divisible by block size; decompressed size == original size."""
    raise NotImplementedError


def test_blocks_roundtrip():
    """TODO: from_blocks(to_blocks(img)) == img."""
    raise NotImplementedError
