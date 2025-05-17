
#Making a function to save the output to files.
def save_to_file(filename, data):
    with open(filename, "w") as f:
        if isinstance(data, dict):
            for key, value in data.items():
                f.write(f"{key}: {', '.join(value)}\n")
        elif isinstance(data, list):
            for item in data:
                f.write(f"{item}\n")