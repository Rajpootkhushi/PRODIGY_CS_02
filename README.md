# Simple Image Encryption Tool

This is a simple Python program that allows users to encrypt and decrypt images using pixel manipulation techniques. The program applies a basic mathematical operation to each pixel and allows for the swapping of pixel values.

## Features

- Encrypts images by adding a constant value to each pixel.
- Decrypts previously encrypted images by subtracting the constant value.
- User-friendly interface for inputting image paths and keys.

## Requirements

- Python 3.x
- Pillow library (install using `pip install Pillow`)

## How to Use

1. Clone the repository or download the source code.
   ```bash
   cd image-encryption-tool

2. Run the program.
   python image_encryption_tool.py

3. Follow the prompts to:  
- **Choose whether to encrypt or decrypt an image.**  
- **Input the path of the image you want to process.**  
- **Provide a path to save the output image.**  
- **Enter a key (an integer value for pixel manipulation).**

4. The program will display a message indicating whether the image was encrypted or decrypted successfully.

5. Example  
- **Do you want to (E)ncrypt or (D)ecrypt an image? E**  
- **Enter the path of the image: C:\path\to\your\image.png**  
- **Enter the path to save the output image: C:\path\to\your\encrypted_image.png**  
- **Enter a key (integer value for pixel manipulation): 50**  
- **Image encrypted and saved as C:\path\to\your\encrypted_image.png**

6. Input Image:
   **![Screenshot 2025-02-21 205538](https://github.com/user-attachments/assets/4e7700a7-dd91-4fe6-a824-96d35f169782)**

7. Output Image:
  **![Screenshot1](https://github.com/user-attachments/assets/3b563c50-cc8a-48dd-8672-e60ea7b9c199)**  


   
