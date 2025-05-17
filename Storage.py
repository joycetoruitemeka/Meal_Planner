"""
Storage.py

Utility to persist dictionaries or lists in plain-text files.
"""

#Making a function to save the output to files.
def save_to_file(filename, data):
    """
    Writes data (dict or list) to filename.

    Dictionaries are saved as:
        key: value1, value2, ...

    Lists are saved one item per line.
    """
    
    with open(filename, "w") as f:
        if isinstance(data, dict):
            for key, value in data.items():
                f.write(f"{key}: {', '.join(value)}\n")
        elif isinstance(data, list):
            for item in data:
                f.write(f"{item}\n")