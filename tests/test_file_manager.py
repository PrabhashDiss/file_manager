import os
import unittest
from file_manager import create_file_structure

class TestFileManager(unittest.TestCase):
    def test_create_file_structure(self):
        file_structure = """
        test_dir/
        test_dir/file1.txt
        test_dir/subdir1/
        test_dir/subdir1/file2.txt
        """
        create_file_structure(file_structure, base_dir='test')
        
        self.assertTrue(os.path.exists('test/test_dir'))
        self.assertTrue(os.path.exists('test/test_dir/file1.txt'))
        self.assertTrue(os.path.exists('test/test_dir/subdir1'))
        self.assertTrue(os.path.exists('test/test_dir/subdir1/file2.txt'))

if __name__ == "__main__":
    unittest.main()
