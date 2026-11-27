import os
import numpy as np
from PIL import Image

from codec import compress, decompress
from metrics import compression_ratio, mse


def main():

    base_dir = os.path.dirname(os.path.abspath(__file__))

    while True:
        print("\n=== Vector Quantization (LBG) ===")
        print("1) Compress")
        print("2) Decompress")
        print("3) Exit")

        choice = input("Choose: ").strip()

        #Compression
        if choice == "1":

            filename = input("Image filename: ").strip()
            original_dir = os.path.join(base_dir, "original_image")
            path = os.path.join(original_dir, filename)

            if not os.path.isfile(path):
                print("Image not found in original_image folder.")
                continue

            # Read original image dimensions
            try:
                with Image.open(path) as img:
                    w, h = img.size

            except Exception:
                print("Invalid or unreadable image.")
                continue

            try:
                bh = int(input("Block height: "))
                bw = int(input("Block width: "))
                k = int(input("Codebook size k: "))

            except ValueError:
                print("Please enter whole numbers.")
                continue

            if bh < 1 or bw < 1 or k < 1:
                print("Block dimensions and k must be at least 1.")
                continue

            out_dir = os.path.join(base_dir, "out")
            os.makedirs(out_dir, exist_ok=True)

            try:
                stats = compress(path, bh, bw, k, out_dir)
                ratio = stats["ratio"]
                original_bits = stats["original_bits"]
                compressed_bits = stats["compressed_bits"]

                print("\n--- Compression done ---")
                print(f"Original size    : {original_bits} bits")
                print(f"Compressed size  : {compressed_bits} bits")
                print(f"Compression ratio: {ratio:.2f} : 1")
                print(f"Files saved in   : {out_dir}")
                

            except Exception as e:
                print(f"Compression failed: {e}")

        #Decompression
        elif choice == "2":

            codebook_name = input("Codebook filename: ").strip()
            compressed_name = input("Compressed filename: ").strip()
            out_dir = os.path.join(base_dir, "out")

            codebook = os.path.join(out_dir, codebook_name)
            compressed = os.path.join(out_dir, compressed_name)

            if not os.path.isfile(codebook) or not os.path.isfile(compressed):
                print("Codebook or compressed file not found in out folder.")
                continue

            # Ask for original image to calculate MSE
            original_name = input("Original image filename: ").strip()
            original_dir = os.path.join(base_dir, "original_image")
            original_path = os.path.join(original_dir, original_name)

            if not os.path.isfile(original_path):
                print("Original image not found in original_image folder.")
                continue

            # Get output image filename
            out_name = input("Output image filename (press Enter for default): ").strip()

            if not out_name:
                out_name = "reconstructed.png"
            reconstructed_dir = os.path.join(base_dir, "reconstructed")
            os.makedirs(reconstructed_dir, exist_ok=True)
            out_path = os.path.join(reconstructed_dir, out_name)

            try:
                decompress(codebook, compressed, out_path)

                print(f"\nReconstructed image saved to {out_path}")

                with Image.open(original_path) as img:
                original_array = np.array(img.convert("L"))

                with Image.open(out_path) as img:
                    reconstructed_array = np.array(img)

                # Calculate MSE
                error = mse(original_array, reconstructed_array)

                print(f"MSE: {error:.3f}")

            except ValueError as e:
                print(f"Cannot calculate MSE: {e}")

            except Exception as e:
                print(f"Decompression failed: {e}")

        elif choice == "3":

            print("Program closed successfully.")
            break
        else:
            print("Invalid choice. Enter 1, 2 or 3.")

if __name__ == "__main__":
    main()