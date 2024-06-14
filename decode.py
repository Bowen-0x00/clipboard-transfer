import base64
import argparse

def save_base64_as_file(base64_content, file_path):
    with open(file_path, 'wb') as file:
        decoded_content = base64.b64decode(base64_content)
        file.write(decoded_content)

parser = argparse.ArgumentParser(description='recover Base64 file to origin file')
parser.add_argument('base64_path', type=str, help='Base64 content file path')
parser.add_argument('save_path', type=str, help='save file path')

args = parser.parse_args()

with open(args.base64_path, 'r') as f:
    save_base64_as_file(f.read(), args.save_path)

