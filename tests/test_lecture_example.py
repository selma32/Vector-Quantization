import os
import sys
import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from metrics import compression_ratio, mse
from blocks import pad_image, to_blocks, from_blocks, crop_image
from lbg import build_codebook


orig = np.array([
    [1, 2, 7, 9, 4, 11],
    [3, 4, 6, 6, 12, 12],
    [4, 9, 15, 14, 9, 9],
    [10, 10, 20, 18, 8, 8],
    [4, 3, 17, 16, 1, 4],
    [4, 5, 18, 18, 5, 6]
], dtype=np.uint8)

recon = np.array([
    [2, 3, 8, 9, 4, 10],
    [4, 5, 7, 7, 11, 11],
    [4, 10, 16, 15, 8, 9],
    [11, 11, 19, 18, 7, 7],
    [2, 3, 16, 15, 2, 3],
    [4, 5, 19, 18, 4, 5]
], dtype=np.uint8)


expected_codebook = np.array([
    [2, 3, 4, 5],
    [8, 9, 7, 7],
    [4, 10, 11, 11],
    [16, 15, 19, 18]
])


def test_codebook():
    blocks = to_blocks(orig, 2, 2)
    codebook = build_codebook(blocks, 4)

    assert codebook.shape == (4, 4)
    np.testing.assert_allclose(codebook, expected_codebook)

def test_mse():
    """Expected MSE = 30/36 = 0.833."""
    assert mse(orig, recon) == pytest.approx(30 / 36)

def test_ratio_6x6():
    """Expected compression ratio = 288/146 = 1.97."""
    ratio, original_bits, compressed_bits = compression_ratio(6, 6, 2, 2, 4)
    assert original_bits == 288
    assert compressed_bits == 146
    assert ratio == pytest.approx(288 / 146)


def test_ratio_600x600():
    """Expected compression ratio is approximately 16:1."""
    ratio, original_bits, compressed_bits = compression_ratio(600, 600, 2, 2, 4)
    assert original_bits == 2_880_000
    assert compressed_bits == 180_128
    assert ratio == pytest.approx(2_880_000 / 180_128)


def test_padding_roundtrip():
    """Check that padding is removed and original dimensions are restored."""
    img = np.arange(35, dtype=np.uint8).reshape(5, 7)
    padded = pad_image(img, 2, 2)
    blocks = to_blocks(padded, 2, 2)
    rebuilt = from_blocks(blocks, padded.shape, 2, 2)
    restored = crop_image(rebuilt, img.shape)

    assert restored.shape == img.shape
    np.testing.assert_array_equal(restored, img)

def test_blocks_roundtrip():
    """Check that splitting and rebuilding preserve the image."""
    img = np.arange(36, dtype=np.uint8).reshape(6, 6)

    blocks = to_blocks(img, 2, 2)
    rebuilt = from_blocks(blocks, img.shape, 2, 2)
    np.testing.assert_array_equal(rebuilt, img)