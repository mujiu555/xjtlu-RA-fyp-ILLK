import os
import json


def find_files_in_directory(directory):
    """Return a list of file paths in the given directory (non-recursive)."""
    return [
        os.path.join(directory, f)
        for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f))
    ]


def translate_from(file_path):
    """Read and parse JSON data from the specified file."""
    try:
        with open(file_path, "r") as file:
            sample = json.load(file)
            idx = sample["idx"]
            file_name = sample["file_name"]
            cwe = sample["cwe"]
            code = sample["issue_code"]["source"]
            to = {"idx": idx, "file_name": file_name, "cwe": cwe, "code": code}
            return to

    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    except json.JSONDecodeError:
        raise ValueError(f"The file {file_path} does not contain valid JSON.")


def main():
    i = []
    for f in find_files_in_directory("/root/workspace/xjtlu-RA-fyp-ILLK/test_graphson"):
        i += translate_from(f)
    f = open("/root/workspace/workspace/translated.json", "w")
    f.write(json.dumps(i))


if __name__ == "__main__":
    main()
