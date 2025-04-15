import base64
import os

def png_to_base64(file_path):
    try:
        with open(file_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        return encoded_string
    except FileNotFoundError:
        return f"Error: The file {file_path} was not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Caminho para o arquivo PNG
base_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(base_dir, 'icon', 'amarelo.png')
file_path = icon_path  # Substitua pelo caminho do seu arquivo PNG
base64_string = png_to_base64(file_path)

print(base64_string)  # Imprime a string base64

