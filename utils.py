"""
Various utilities
"""
def get_text_from_file(filename: str) -> str:
    with open(filename, 'r') as f:
        return f.read()