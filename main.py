#Entry point for the program

import os

def main():
    pass


# Checks if the file is a valid one (C or C++)
def validate_input_file(file_path):
  file_exists = os.path.isfile(file_path)
  if not file_exists:
      print(f"File does not exist: {file_path}")
      return False
  valid_extensions = ['.c', '.cpp']
  file_extension = os.path.splitext(file_path)[1]
  if file_extension not in valid_extensions:
      print(f"Invalid file extension: {file_extension}")
      return False
  return True



if __name__ == "__main__":
  main()