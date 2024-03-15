# File Manager Package

This package provides a set of utilities for managing files in Python.

## Installation

You can install this package directly from GitHub using `pip`. Make sure you have Git and `pip` installed on your system.

```
pip install git+https://github.com/PrabhashDiss/file_manager.git
```

If you need to install a specific branch or tag, you can specify it by appending `@branch_or_tag_name` to the URL:

```
pip install git+https://github.com/PrabhashDiss/file_manager.git@branch_or_tag_name
```

## Usage
Once the package is installed, you can import and use its functionality in your Python scripts:

```
import file_manager as fm

# Example usage
file_structure = """
dir1/
dir1/file1.txt
dir1/subdir1/
dir1/subdir1/file2.txt
dir2/
"""

fm.create_file_structure(file_structure)
print("File structure created successfully.")
```

For detailed usage instructions, refer to the documentation or docstrings within the package.
