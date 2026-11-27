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
    """Pad the bottom and right edges of img with 0 so its height and width are divisible by bh and bw."""


    x=-img.shape[0]%bh

    y=-img.shape[1]%bw

   



    return np.pad(img,((0,x),(0,y)),mode='constant',constant_values=0)


def to_blocks(padded_img, bh, bw):
   

    H=padded_img.shape[0]
    W=padded_img.shape[1]

    a=[]

   

    for r in range(0,H,bh):
        for c in range(0,W,bw):

            a.append(padded_img[r:r+bh,c:c+bw].flatten())
            

    

    return np.array(a)


def from_blocks(blocks, padded_shape, bh, bw):

    """TODO: return padded_img rebuilt from blocks.
    - Must be the exact inverse of to_blocks (test this)."""

    H,W=padded_shape
    

    img=np.zeros((H,W),dtype=blocks.dtype)

   

    i=0
    for r in range(0,H,bh):
        for c in range(0,W,bw):
            square=blocks[i].reshape((bh,bw))
            img[r : r + bh, c : c + bw] = square
            i+=1
        

    return img


def crop_image(padded_img, orig_shape):
    """TODO: return img with the padding removed, using orig_shape."""


    orig_H,orig_W=orig_shape

    cropped = padded_img[:orig_H, :orig_W]

    return cropped







