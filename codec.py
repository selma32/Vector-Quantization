
import numpy as np
import struct
from blocks import pad_image, to_blocks, from_blocks, crop_image
from lbg import build_codebook, nearest_index
from metrics import bits_per_index, compression_ratio, mse
import os
import math
from PIL import Image












def pack_indices(indices, bits_per_index):
    
    if len(indices) == 0: return b""
  
    stream=""


    for i in indices:
        stream+=f"{i:0{bits_per_index}b}"

    padding =-len(stream)%8

    stream=stream+'0'*padding

    num_bytes = len(stream) // 8

    result = int(stream, 2).to_bytes(num_bytes, byteorder="big")




    return result





def unpack_indices(data, bits_per_index, count):
    
    stream=""

    for b in data:
        stream += f"{b:08b}"

    indices=[]

    for i in range(0,count*bits_per_index,bits_per_index):
        s=stream[i:i+bits_per_index]
        indices.append(int(s,2))

    return np.array(indices, dtype=int)


    
def save_codebook(path, codebook, bh, bw):
   
    k=codebook.shape[0]

    with open(path, "wb") as f:
        np.savez(f, codebook=codebook, bh=bh, bw=bw,k=k)











def load_codebook(path):
    
    with open(path, "rb") as f:
        data = np.load(f)
        codebook=data["codebook"]
        bh=int(data["bh"])
        bw=int(data["bw"])
        k=data["k"]


    return codebook, bh, bw



    























def save_compressed(path, indices, orig_shape, bits_per_index):
  
    orig_h,orig_w=orig_shape

    with open(path, "wb") as f:
        f.write(struct.pack(">IIII", orig_h, orig_w,bits_per_index,len(indices)))
        f.write(pack_indices(indices,bits_per_index))
       
        


   
   
   
   
   
   
   
   
   
   
   
    












def load_compressed(path):
  
    with open(path, "rb") as f:
        header_bytes=f.read(16)
        orig_h, orig_w,bits_per_index,count=struct.unpack(">IIII", header_bytes)
        packed_data = f.read()
        indices=unpack_indices(packed_data, bits_per_index, count)
        return indices, (orig_h, orig_w)
    
      



















def compress(image_path, bh, bw, k, out_dir):
  
    img = np.array(Image.open(image_path).convert("L"), dtype=np.uint8)
    padded_img=pad_image(img,bh,bw)
    blocks=to_blocks(padded_img,bh,bw)

    orig_shape = img.shape 
    bits_per_index=math.ceil(math.log2(k))

    codebook=build_codebook(blocks,k)
    indices=nearest_index(blocks,codebook)
    os.makedirs(out_dir, exist_ok=True)
    cb_path = os.path.join(out_dir, "codebook.npz")
    comp_path = os.path.join(out_dir, "compressed.bin")
    save_codebook(cb_path, codebook, bh, bw)
    save_compressed(comp_path, indices, orig_shape, bits_per_index)


    h=orig_shape[0]
    w=orig_shape[1]
    recon_blocks = codebook[indices].astype(img.dtype)
    recon_padded = from_blocks(recon_blocks, padded_img.shape, bh, bw)

    recon_img = crop_image(recon_padded, orig_shape)

    
    ratio, original_bits, compressed_bits = compression_ratio(h, w, bh, bw, k)
    err = mse(img, recon_img)

    return {
        "ratio": ratio,
        "mse": err,
        "original_bits": original_bits,
        "compressed_bits": compressed_bits,
    }











  





def decompress(codebook_path, compressed_path, out_image_path):
  
    
    codebook, bh, bw = load_codebook(codebook_path)
    indices, orig_shape = load_compressed(compressed_path)

   
    recon_blocks = np.clip(codebook[indices], 0, 255).astype(np.uint8)

   
    orig_h, orig_w = orig_shape
    padded_shape = (orig_h + (-orig_h % bh), orig_w + (-orig_w % bw))
    recon_padded = from_blocks(recon_blocks, padded_shape, bh, bw)

    
    recon_img = crop_image(recon_padded, orig_shape)
    Image.fromarray(recon_img).save(out_image_path)

    return recon_img
