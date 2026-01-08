# PyFIM
FIM: File Integrity Monitor
FIM is a lightweight Python-based command-line utility designed for monitoring file integrity. It creates "snapshots" (cryptographic hashes) of files or entire directories, stores them in a JSON database, and later verifies them 
to detect unauthorized modifications.

🚀 Key Features:

- Chunk-based Hashing: Efficiently processes large files by reading them in small chunks (4096 bytes), preventing high memory consumption.
  
- Algorithm Flexibility: Supports any hashing algorithm provided by Python's hashlib (SHA256, MD5, SHA512, etc.).
  
- Recursive Scanning: Deeply scans directories while maintaining relative path structures.

- Command Line Interface (CLI): Fully integrated with argparse for easy automation and terminal usage.

🛠 Technologies

- Python 3.x

- Hashlib (for cryptographic operations)

- Argparse (for CLI handling)

- JSON (for data persistence)

📦 Installation:

1. Clone the repository:
     git clone https://github.com/your-username/PyFIM.git
   
2. cd PyFIM

3. Ensure you have Python 3 installed. No external dependencies are required.

💻 Usage

The script supports 4 main operation modes (-m):

1. Hash a Single File
   
Generates a hash and creates/overwrites a JSON database with that single entry:
    python main.py -m hash_file -f path/to/file.txt -j base.json

2. Multi-Hash Directory
   
Scans a directory recursively and saves all file hashes into a JSON database:
    python main.py -m multi_hash -d ./my_folder -j database.json

3. Check Single File Integrity

Compares a specific file's current hash against the one stored in the database:
    python main.py -m check_hash -f path/to/file.txt -j database.json -n key_name

4. Multi-Check Directory

Automatically verifies all files in a folder against the provided database:
    python main.py -m multi_check -d ./my_folder -j database.json

5. Help

You can use -h or --help that see help information:
    python main.py -h

🛡 How it Works

The monitor works by comparing the "digital fingerprint" of your files.

1. Initial State: You generate hashes for your clean files.

2. Detection: If a single character is changed in a file (by a user or malware), the hash changes entirely.

3. Verification: The script identifies the mismatch and alerts you.

🤝 Contact

Created by [Ghostroot] – [rootg727@gmail.com].
