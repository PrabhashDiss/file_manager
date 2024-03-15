import os

def create_file_structure(file_structure_str, base_dir='.'):
    """
    Create file structure from the given string representation.
    
    Arguments:
    file_structure_str : str
        String representation of the file structure.
    base_dir : str, optional
        Base directory where the file structure will be created. Defaults to current directory.
    """
    # Split the file structure string by lines
    lines = file_structure_str.strip().split('\n')
    
    for line in lines:
        # Split each line by '/'
        parts = line.split('/')
        path = os.path.join(base_dir, *parts)
        
        # If it ends with '/', create directory, else create file
        if line.endswith('/'):
            os.makedirs(path, exist_ok=True)
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w'):
                pass

if __name__ == "__main__":
    # Example usage
    file_structure = """
    dir1/
    dir1/file1.txt
    dir1/subdir1/
    dir1/subdir1/file2.txt
    dir2/
    """

    create_file_structure(file_structure)
    print("File structure created successfully.")
