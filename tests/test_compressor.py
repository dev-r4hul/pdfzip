import unittest
from pathlib import Path
from pdfzip.compressor import PDFCompressor

class TestPDFCompressor(unittest.TestCase):

    def setUp(self):
        # Set up a compressor instance with a default compression level
        self.compressor = PDFCompressor(compress_level=2)

        # Create sample file paths for input and output
        self.input_file = Path("sample.pdf")
        self.output_file = Path("sample_compressed.pdf")
        self.input_folder = Path("sample_folder")
        self.output_folder = Path("output_folder")

        # Ensure output files are removed before each test
        if self.output_file.exists():
            self.output_file.unlink()

    def test_compress_single_file(self):
        # Test compression of a single PDF file
        self.compressor.compress_file(self.input_file, self.output_file)
        self.assertTrue(self.output_file.exists())

    def test_compress_folder(self):
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
        # Test handling of a non-PDF file
        non_pdf_file = Path("not_a_pdf.txt")
        self.compressor.compress_file(non_pdf_file, self.output_file)
        self.assertFalse(self.output_file.exists())

    def tearDown(self):
        # Clean up output files after tests
        if self.output_file.exists():
            self.output_file.unlink()

if __name__ == "__main__":
    unittest.main()
