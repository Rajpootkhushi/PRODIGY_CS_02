from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path, key):
    img = Image.open(input_image_path)
    img_array = np.array(img)

    encrypted_array = (img_array + key) % 256  
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_image.save(output_image_path)
    print(f"Image encrypted and saved as {output_image_path}")

def decrypt_image(input_image_path, output_image_path, key):
    img = Image.open(input_image_path)
    img_array = np.array(img)

    decrypted_array = (img_array - key) % 256  
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_image.save(output_image_path)
    print(f"Image decrypted and saved as {output_image_path}")

def main():
    operation = input("Do you want to (E)ncrypt or (D)ecrypt an image? ").strip().upper()
    input_image_path = input("Enter the path of the image: ").strip()  
    output_image_path = input("Enter the path to save the output image: ").strip()  

    if not output_image_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        print("Error: Please provide a valid output filename with an image extension (e.g., .png, .jpg).")
        return

    key = int(input("Enter a key (integer value for pixel manipulation): "))

    if operation == 'E':
        encrypt_image(input_image_path, output_image_path, key)
    elif operation == 'D':
        decrypt_image(input_image_path, output_image_path, key)
    else:
        print("Invalid operation! Please select 'E' for encrypt or 'D' for decrypt.")
if __name__ == "__main__":
    main()