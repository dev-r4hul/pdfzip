import argparse
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
import shutil
import subprocess
import sys

class PDFCompressor:
    def __init__(self, compress_level=2):
        self.compress_level = compress_level
        self.quality = {
            0: "/default",
            1: "/prepress",
            2: "/printer",
            3: "/ebook",
            4: "/screen"
        }

    def compress(self, input_file_path, output_file_path):
        """Function to compress PDF via Ghostscript command line interface"""
        if not input_file_path.is_file():
            print(f"Error: Invalid path for input PDF file: {input_file_path}")
            return

        if self.compress_level < 0 or self.compress_level > len(self.quality) - 1:
            print(f"Error: Invalid compression level: {self.compress_level}. Run pdfc -h for options.")
            return

        if input_file_path.suffix.lower() != '.pdf':
            print(f"Error: Input file is not a PDF: {input_file_path}")
            return

        gs = self.get_ghostscript_path()

        try:
            print(f"Compressing {input_file_path}...")
            initial_size = input_file_path.stat().st_size
            subprocess.check_call(
                [
                    gs,
                    "-sDEVICE=pdfwrite",
                    "-dCompatibilityLevel=1.4",
                    f"-dPDFSETTINGS={self.quality[self.compress_level]}",
                    "-dNOPAUSE",
                    "-dQUIET",
                    "-dBATCH",
                    f"-sOutputFile={output_file_path}",
                    str(input_file_path),
                ]
            )
            final_size = output_file_path.stat().st_size
            ratio = 1 - (final_size / initial_size)
            print(f"Compression of {input_file_path} by {ratio:.0%}. Final file size is {final_size / 1000000:.5f}MB")
        except subprocess.CalledProcessError as e:
            print(f"Ghostscript failed to compress the PDF {input_file_path}.")
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred while compressing {input_file_path}.")
            print(e)

    @staticmethod
    def get_ghostscript_path():
        gs_names = ["gs", "gswin32", "gswin64"]
        for name in gs_names:
            path = shutil.which(name)
            if path:
                return path
        print(f"No GhostScript executable was found on path ({'/'.join(gs_names)})")
        sys.exit(1)

    def compress_file(self, input_path, output_path):
        output_path = output_path if output_path else "temp.pdf"
        self.compress(input_path, Path(output_path))

        if output_path == "temp.pdf":
            shutil.copyfile("temp.pdf", input_path)
            Path("temp.pdf").unlink()

    def compress_folder(self, input_folder, output_folder):
        pdf_files = list(input_folder.glob("*.pdf"))

        if not pdf_files:
            print(f"No PDF files found in the directory: {input_folder}")
            return

        output_folder = output_folder if output_folder else input_folder

        tasks = [(pdf, output_folder / pdf.name) for pdf in pdf_files]
        with ProcessPoolExecutor() as executor:
            executor.map(lambda p: self.compress_file(*p), tasks)

    def open_file(self, file_path):
        try:
            if sys.platform == "win32":
                os.startfile(file_path)
            elif sys.platform == "darwin":
                subprocess.call(["open", file_path])
            else:
                subprocess.call(["xdg-open", file_path])
        except Exception as e:
            print(f"Failed to open file: {file_path}")
            print(e)

def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("input", help="Path to the input PDF file or directory containing PDF files")
    parser.add_argument("-o", "--out", help="Path to the output PDF file or directory for compressed PDFs")
    parser.add_argument("-c", "--compress", type=int, default=2, help="Compression level from 0 to 4")
    parser.add_argument("-b", "--backup", action="store_true", help="Backup the original PDF file(s)")
    parser.add_argument("--open", action="store_true", default=False, help="Open PDF after compression")
    parser.add_argument("--format", choices=["pdf", "ps"], default="pdf", help="Output format (default: pdf)")

    args = parser.parse_args()

    compressor = PDFCompressor(compress_level=args.compress)
    input_path = Path(args.input)
    output_path = Path(args.out) if args.out else None

    if input_path.is_file():
        compressor.compress_file(input_path, output_path)

        if args.backup:
            shutil.copyfile(input_path, input_path.with_suffix("_BACKUP.pdf"))

        if args.open:
            compressor.open_file(output_path if output_path else input_path)

    elif input_path.is_dir():
        compressor.compress_folder(input_path, output_path)

        if args.open:
            for pdf in input_path.glob("*.pdf"):
                compressor.open_file(output_path / pdf.name if output_path else pdf)

    else:
        print(f"Error: The specified input path is neither a file nor a directory: {input_path}")
        sys.exit(1)

if __name__ == "__main__":
    main()
