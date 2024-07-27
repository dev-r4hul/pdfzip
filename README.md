# pdfzip

A simple and efficient PDF compressor using Ghostscript. This tool allows you to compress PDF files with various levels of compression, making it ideal for reducing file sizes for storage or sharing.

## Features

- **Multiple Compression Levels:** Choose from five different levels of compression to suit your needs.
- **Improved Error Handling:** Provides detailed error messages to help diagnose issues.
- **Batch Processing:** Compress all PDF files in a folder with ease.
- **Cross-Platform Support:** Works on Windows, macOS, and Linux.
- **Optional Progress Display:** View compression progress and results directly in the console.
- **Different Output Formats:** Choose between PDF and PS (PostScript) formats for output files.
- **Backup Options:** Automatically create backups of original files if desired.

## Installation

You can install `pdfzip` using one of the following methods:

### Option 1: Install via pip

To install `pdfzip` from PyPI using pip, run the following command:

```bash
pip install pdfzip
```

### Option 2: Install via Git Clone

If you prefer to clone the repository and install manually, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/dev-r4hul/pdfzip.git
   cd pdfzip
   ```

2. **Install the package:**

   ```bash
   pip install .
   ```

3. **(Optional) Add the script to your PATH:**

   Make sure the installation directory is in your system’s PATH, or create a symbolic link to `pdfzip` for easy access.

### Ghostscript Installation

Ensure that Ghostscript is installed on your system and available in your system's PATH. You can download it from the official [Ghostscript website](https://ghostscript.com/releases/index.html).

## Usage

`pdfzip` can be used from the command line to compress individual PDF files or entire directories of PDF files.

### Command-Line Arguments

Here are the available command-line arguments and their descriptions:

- **`input`** (required):  
  Path to the input PDF file or directory containing PDF files.
  
  ```bash
  pdfzip input.pdf
  pdfzip /path/to/pdf/directory
  ```

- **`-o, --out`** (optional):  
  Path to the output PDF file or directory for compressed PDFs. If not specified, the original file will be replaced (unless `--backup` is used).
  
  ```bash
  pdfzip input.pdf -o compressed_output.pdf
  pdfzip /path/to/pdf/directory -o /path/to/output/directory
  ```

- **`-c, --compress`** (optional, default=2):  
  Compression level from 0 to 4. Choose the appropriate level based on your needs:
  - `0`: Default compression
  - `1`: Prepress (high quality, larger size)
  - `2`: Printer (good quality, suitable for print)
  - `3`: eBook (medium quality, smaller size)
  - `4`: Screen (low quality, smallest size)

  ```bash
  pdfzip input.pdf -c 3
  ```

- **`-b, --backup`** (optional):  
  Create a backup of the original PDF file(s) before compression, appending `_BACKUP` to the filename.
  
  ```bash
  pdfzip input.pdf -b
  ```

- **`--open`** (optional, default=False):  
  Open the PDF file after compression using the default PDF viewer for your system.
  
  ```bash
  pdfzip input.pdf --open
  ```

- **`--format`** (optional, default=pdf):  
  Specify the output format (`pdf` or `ps`). The default format is `pdf`.

  ```bash
  pdfzip input.pdf --format ps
  ```

### Examples

#### Compress a Single PDF File

Compress `document.pdf` with the default settings and replace the original file:

```bash
pdfzip document.pdf
```

Compress `document.pdf` with high compression for screen display and save as `compressed_document.pdf`:

```bash
pdfzip document.pdf -o compressed_document.pdf -c 4
```

#### Compress Multiple PDF Files in a Folder

Compress all PDFs in a folder with the printer setting and save in a separate output folder:

```bash
pdfzip /path/to/folder -o /path/to/output/folder -c 2
```

Backup original files before compressing:

```bash
pdfzip /path/to/folder -b
```

#### Open PDF After Compression

Compress `report.pdf` and open it with the default PDF viewer:

```bash
pdfzip report.pdf --open
```

### Error Handling

The script will provide detailed error messages if something goes wrong, such as:

- Invalid input path
- Unsupported file format
- Missing Ghostscript installation

### Troubleshooting

If you encounter any issues, ensure that Ghostscript is installed correctly and available in your system's PATH. If you need further assistance, please refer to the [Ghostscript documentation]((https://ghostscript.readthedocs.io/en/latest/current/Use.htm)).