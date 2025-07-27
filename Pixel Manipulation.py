from PIL import Image
import os

def encrypt_image(image_path, key, output_path):
    img = Image.open(image_path)
    pixels = img.load()

    for i in range(img.size[0]):  # width
        for j in range(img.size[1]):  # height
            r, g, b = pixels[i, j]
            pixels[i, j] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )
    img.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, key, output_path):
    img = Image.open(image_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )
    img.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

def main():
    print("=== Image Encryption Tool ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt an image? ").strip().upper()

    if choice not in ['E', 'D']:
        print("Invalid option. Please choose E or D.")
        return

    image_path = input("Enter the path to the image: ").strip()
    if not os.path.exists(image_path):
        print("Image file not found.")
        return

    try:
        key = int(input("Enter numeric key for encryption/decryption: "))
    except ValueError:
        print("Invalid key. Enter an integer.")
        return

    output_path = input("Enter the output file path (e.g., output.png): ").strip()

    if choice == 'E':
        encrypt_image(image_path, key, output_path)
    else:
        decrypt_image(image_path, key, output_path)

if __name__ == "__main__":
    main()