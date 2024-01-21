import re

def insert_Z_between_same_letters(text):
    return re.sub(r"(.)\1", r"\1Z\1", text)

# Example usage
input_string = "hello"
modified_string = insert_Z_between_same_letters(input_string)
print(modified_string)
