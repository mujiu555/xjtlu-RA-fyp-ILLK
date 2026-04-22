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
            idx = sample.get("idx")
            file_name = sample.get("file_name")
            cwe = sample.get("cwe")
            code = sample.get("issue_code", {}).get("source")

            if None in (idx, file_name, cwe, code):
                raise ValueError(f"Missing required fields in the file: {file_path}")

            return {"idx": idx, "file_name": file_name, "cwe": cwe, "code": code}

    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    except json.JSONDecodeError:
        raise ValueError(f"The file {file_path} does not contain valid JSON.")

def main():
    input_directory = "/root/workspace/xjtlu-RA-fyp-ILLK/test_graphson"
    output_file = "/root/workspace/workspace/translated.json"

    results = []

    try:
        for file_path in find_files_in_directory(input_directory):
            try:
                translation = translate_from(file_path)
                results.append(translation)
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

        with open(output_file, "w") as f:
            json.dump(results, f, indent=4)
        print(f"Translation completed successfully. Output written to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
