"""
app.py  --  OWNER: Member C
Entry point for the TA:  python app.py
"""
from codec import compress, decompress


def main():
    """TODO: menu (or Tkinter GUI) with: 1) Compress  2) Decompress  3) Exit
    Compress   : ask for image path, block size, k, output folder -> call compress(), print ratio
    Decompress : ask for codebook file, compressed file, output image path -> call decompress()
    - Validate inputs (bad path, block size <= 0, k < 1)."""
    raise NotImplementedError


if __name__ == "__main__":
    main()
