from typing import List
from file import File


class Directory:
    """Describe a directory and its contents."""
    def __init__(self, name: str, root: 'Directory', files: List[File], sub_directories: List['Directory']) -> None:
        """Initialize the attributes of the Directory object."""
        self.name = name
        self.root = root
        self.files = files
        self.sub_directories = sub_directories

    def add_sub_directory(self, directory: 'Directory') -> None:
        self.sub_directories.append(directory)

    def remove_sub_directory(self, directory: 'Directory') -> None:
        if directory in self.sub_directories:
            self.sub_directories.remove(directory)
        else:
            print('Directory does not exist')

    def add_file(self, file: File) -> None:
        self.files.append(file)
        file.directory = self.root

    def remove_file(self, file: File) -> None:
        file.directory = None
        self.files.remove(file)
