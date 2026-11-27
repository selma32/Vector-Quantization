"""
Conventions (shared by everyone):
- blocks   : NumPy array of shape (N, bh*bw), each row is one flattened block
- codebook : NumPy array of shape (k, bh*bw)
- indices  : NumPy array of shape (N,), integers from 0 to k-1
"""
import numpy as np


def distance(block, codeword):
    block = np.asarray(block, dtype=np.float64)
    codeword = np.asarray(codeword, dtype=np.float64)

    return np.abs(block - codeword).sum()

  
def nearest_index(blocks, codebook):
    blocks = np.asarray(blocks, dtype=np.float64)
    codebook = np.asarray(codebook, dtype=np.float64)

    d = np.abs(blocks[:, None, :] - codebook[None, :, :]).sum(axis=2)
    return d.argmin(axis=1)



def recompute_centroids(blocks, indices, codebook):
    new_codebook = codebook.copy()

    for j in range(len(codebook)):
        members = blocks[indices == j]
        if len(members) > 0:
            new_codebook[j] = members.mean(axis=0)

    return new_codebook


def split_codeword(codeword):
    return codeword - 1, codeword + 1


def build_codebook(blocks, k):
    blocks = np.asarray(blocks, dtype=np.float64)
    k = min(k, len(blocks))

    # 1- One codeword = average of all blocks.
    codebook = blocks.mean(axis=0, keepdims=True)


    while len(codebook) < k:
        # 2- Split every codeword into two.
        new = []
        for c in codebook:
            a, b = split_codeword(c)
            new.append(a)
            new.append(b)
        codebook = np.array(new)

        # 3- Assign blocks to nearest codeword, recompute centroids,
        last = None
        while True:
            indices = nearest_index(blocks, codebook)

            if last is not None and np.array_equal(indices, last):
                break

            last = indices
            codebook = recompute_centroids(blocks, indices, codebook)
            
            if len(codebook) < k:
                break

    codebook = codebook[:k]
    return np.round(codebook).astype(np.uint8)
