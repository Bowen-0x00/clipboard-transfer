# clipboard-transfer

clipboard-transfer is a tool designed to transfer data in VNC server environments where copy-paste functionality is not supported. It allows encoding the text content or files from the clipboard into Base64 format and outputting the encoded data to the target device using a configured hotkey.

It provides an alternative method for users to upload text or files to VNC servers that do not support direct copy-paste functionality. clipboard-transfer offers a convenient solution for data transfer, eliminating the need for manual encoding.

## Key Features:
- Supports outputting text from the clipboard
- Supports encoding files from the clipboard into Base64
- Outputs the encoded data to the target device using a hotkey
- Provides a decoding script to restore Base64 data to files

## Usage

```bash
python keyInput.py
```
to start listening.

When the registered hotkey `ctrl+alt+[` is pressed, the tool checks the content of the clipboard. If it's text, it is directly outputted. If it's a file path, the tool reads the file, encodes it in Base64, and then outputs it.

For the latter case, you need to run the following command on the server:
```bash
python decode.py [base64_file_path] [output_file_path]
```
to restore the Base64 data to its original file format.