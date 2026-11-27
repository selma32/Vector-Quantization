import numpy as np

def bits_per_index(k):
    k = int(k)
    if k < 1:
        raise ValueError("k must be more than one")
    #bits/label = ceil(log2(k));
    return (k - 1).bit_length()          


def compression_ratio(h, w, bh, bw, k):
    if min(h, w, bh, bw) < 1:
        raise ValueError("sizes must be more than one")
    # Padded grid using ceil division
    n_blocks = -(-h // bh) * -(-w // bw)             
    original_bits = h * w * 8
    codebook_bits = k * bh * bw * 8
    labels_bits = n_blocks * bits_per_index(k)
    compressed_bits = codebook_bits + labels_bits
    return original_bits / compressed_bits, original_bits, compressed_bits


def mse(original, reconstructed):
    a = np.asarray(original, dtype=np.float64)
    b = np.asarray(reconstructed, dtype=np.float64)
    if a.shape != b.shape:
        raise ValueError(f"shape mismatch: {a.shape} vs {b.shape}")
    return float(np.mean((a - b) ** 2))