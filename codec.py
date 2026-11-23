"""
codec.py  --  OWNER: Member B
Bit packing, file I/O, and the compress / decompress pipelines.

Files written by compress() and read by decompress():
  - codebook file   : block height, block width, k, codeword values
  - compressed file : header (original height and width) + packed indices
Decompress must work using ONLY these two files.
"""
import numpy as np
from blocks import pad_image, to_blocks, from_blocks, crop_image
from lbg import build_codebook, nearest_index
from metrics import bits_per_index, compression_ratio, mse


def pack_indices(indices, bits_per_index):
    """TODO: return bytes with every index written using bits_per_index bits.
    - Handle the last partial byte."""
    raise NotImplementedError


def unpack_indices(data, bits_per_index, count):
    """TODO: return indices (count,) read back from the packed bytes.
    - Ignore the padding bits in the last byte."""
    raise NotImplementedError


def save_codebook(path, codebook, bh, bw):
    """TODO: write the codebook file (bh, bw, k, codeword values)."""
    raise NotImplementedError


def load_codebook(path):
    """TODO: return (codebook, bh, bw) read from the codebook file."""
    raise NotImplementedError


def save_compressed(path, indices, orig_shape, bits_per_index):
    """TODO: write the compressed file: header (orig height, width) + packed indices."""
    raise NotImplementedError


def load_compressed(path):
    """TODO: return (indices, orig_shape) read from the compressed file."""
    raise NotImplementedError


def compress(image_path, bh, bw, k, out_dir):
    """TODO: full compression pipeline.
    1. Load image as grayscale, pad it, split into blocks
    2. build_codebook, then nearest_index
    3. save_codebook and save_compressed into out_dir
    Return a stats dict with keys: ratio, mse, original_bits, compressed_bits."""
    raise NotImplementedError


def decompress(codebook_path, compressed_path, out_image_path):
    """TODO: full decompression pipeline.
    1. load_codebook and load_compressed
    2. Replace every index by its codeword, from_blocks, crop_image
    3. Save the image to out_image_path and return it."""
    raise NotImplementedError
