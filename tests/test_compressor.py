import unittest
from pathlib import Path
from pdfzip.compressor import PDFCompressor
import tempfile
import shutil

class TestPDFCompressor(unittest.TestCase):

    def setUp(self):
        # Set up a compressor instance with a default compression level
        self.compressor = PDFCompressor(compress_level=2)

        # Create temporary files and folders
        self.temp_dir = tempfile.mkdtemp()
        self.input_file = Path(self.temp_dir) / "sample.pdf"
        self.output_file = Path(self.temp_dir) / "sample_compressed.pdf"
        self.input_folder = Path(self.temp_dir) / "sample_folder"
        self.output_folder = Path(self.temp_dir) / "output_folder"

        # Create input folder
        self.input_folder.mkdir(parents=True, exist_ok=True)

        # Create a sample PDF file for testing
        with open(self.input_file, 'wb') as f:
            f.write(b'%PDF-1.4\n%...')  # Minimal PDF header for testing

        # Ensure output files are removed before each test
        if self.output_file.exists():
            self.output_file.unlink()

    def test_compress_single_file(self):
        # Test compression of a single PDF file
        self.compressor.compress_file(self.input_file, self.output_file)
        self.assertTrue(self.output_file.exists())

    def test_compress_folder(self):
        # Create a sample PDF file in the input folder
        (self.input_folder / "test1.pdf").write_text('%PDF-1.4\n%...')
        (self.input_folder / "test2.pdf").write_text('%PDF-1.4\n%...')
        
        # Test compression of all PDF files in a folder
        self.compressor.compress_folder(self.input_folder, self.output_folder)
        for pdf in self.input_folder.glob("*.pdf"):
            compressed_pdf = self.output_folder / pdf.name
            self.assertTrue(compressed_pdf.exists())

    def test_invalid_file(self):
        # Test handling of an invalid file path
        invalid_file = Path("invalid.pdf")
        self.compressor.compress_file(invalid_file, self.output_file)
        self.assertFalse(self.output_file.exists())

    def test_non_pdf_file(self):
        # Create a non-PDF file
        non_pdf_file = Path(self.temp_dir) / "not_a_pdf.txt"
        non_pdf_file.write_text("This is not a PDF.")
        try:
            self.compressor.compress_file(non_pdf_file, self.output_file)
        except ValueError:
            self.assertTrue(not self.output_file.exists())
        else:
            self.assertFalse(self.output_file.exists())

    def tearDown(self):
        # Clean up temporary files and directories after tests
        shutil.rmtree(self.temp_dir)

if __name__ == "__main__":
    unittest.main()