"""
blocks.py  --  OWNER: Member B
Padding, splitting an image into blocks, and rebuilding it.

Conventions:
  - img          : grayscale NumPy array (H, W), dtype uint8
  - blocks       : NumPy array (N, bh*bw), each row is one flattened block
  - orig_shape   : (H, W) of the ORIGINAL image (before padding)
  - padded_shape : (H_p, W_p) of the padded image
"""
import numpy as np


def pad_image(img, bh, bw):
    """TODO: return padded_img whose height/width are divisible by bh/bw.
    - Decide the padding value and document it."""
    raise NotImplementedError


def to_blocks(padded_img, bh, bw):
    """TODO: return blocks (N, bh*bw) in a fixed scan order (row by row)."""
    raise NotImplementedError


def from_blocks(blocks, padded_shape, bh, bw):
    """TODO: return padded_img rebuilt from blocks.
    - Must be the exact inverse of to_blocks (test this)."""
    raise NotImplementedError


def crop_image(padded_img, orig_shape):
    """TODO: return img with the padding removed, using orig_shape."""
    raise NotImplementedError
