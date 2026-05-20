# Temp Cleaner

A small Python tool to clean temporary files on Windows.

This project removes files from:

- `C:\Windows\Temp`
- User `%TEMP%` folder (`AppData\Local\Temp`)

Useful for clearing leftover temporary files and freeing some storage.

## Features

- Cleans Windows Temp folder
- Cleans User `%TEMP%` folder
- Skips files currently in use
- Simple and lightweight

## Usage

### Run from source

```bash
python cleaner.py
```

### Run executable

Download `cleaner.exe` from the Releases section and run it.

## Note

Some files may not be deleted because Windows or other applications are using them.

For best results, run as Administrator.

## Author

Made by Suganth S
