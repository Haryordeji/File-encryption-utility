# File Encryption Utility
A simple, user-friendly desktop application for encrypting, decrypting, and securely deleting files using Python and Tkinter.

## Features

- File encryption using AES
- File decryption
- Secure file deletion
- Sandbox environment for safe file operations
- Simple graphical user interface

### Coming
- stronger unit testing

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/file-encryption-utility.git
cd file-encryption-utility
```
2. Install the required packages:
```bash
pip install -r requirements.txt
```

### Setup
To generate some testfiles in `sandbox/input`, run
```bash
python create_test_files.py
```

## Usage
Run the main script from the project root directory:
```bash
python run.py
```

This will open the graphical user interface.

1. Click "Select File" to choose a file for encryption, decryption, or secure deletion.
2. Enter a password for encryption or decryption (not needed for secure deletion).
3. Click the appropriate button for the desired operation.

## Running Tests

To run the unit tests:
```bash
python -m unittest discover tests
```

## How It Works

### Encryption Process

1. A random salt is generated for each encryption.
2. The encryption key is derived from the user's password using PBKDF2 (Password-Based Key Derivation Function 2).
3. The file is encrypted using the Fernet symmetric encryption scheme, which is built on top of AES (Advanced Encryption Standard).
4. The salt is prepended to the encrypted data and saved as a new file with a ".encrypted" extension.

### Decryption Process

1. The salt is read from the beginning of the encrypted file.
2. The decryption key is derived using the salt and the provided password.
3. The file is decrypted using the Fernet scheme.
4. The decrypted content is saved as a new file with a "decrypted_" prefix.

### Secure Deletion

Files are securely deleted by overwriting their contents with random data multiple times before being removed from the file system.

## Sandbox Environment

The utility operates within a sandbox environment to ensure safe file operations:

- `sandbox/input`: Place your original files here for encryption.
- `sandbox/output`: Encrypted and decrypted files are saved here.

This separation helps prevent accidental modification or deletion of important files outside the designated directories.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
