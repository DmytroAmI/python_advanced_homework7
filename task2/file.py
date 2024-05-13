from directory import Directory


class File:
    """Describe class File."""
    def __init__(self, name: str, directory: Directory) -> None:
        """Initialize the attributes of the File object."""
        self.name = name
        self.directory = directory
