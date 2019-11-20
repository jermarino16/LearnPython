# Implement your is_all_strings function below:
def is_all_strings(iterable):
    return all([type(char) == str for char in iterable])
    