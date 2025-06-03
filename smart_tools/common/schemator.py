import json


def collect_keys_from_json_string(data, parent_path='', id=''):
    mylst = []

    def process(data, parent_path):
        if isinstance(data, dict):
            for key, value in data.items():
                current_path = f"{parent_path}\\{key}" if parent_path else key
                # print({"key": key, "path": current_path})
                if {"id": id, "key": key, "path": current_path} not in mylst:
                    mylst.append({"id": id, "key": key, "path": current_path})
                process(value, current_path)
        elif isinstance(data, list):
            for item in data:
                process(item, parent_path)

        return mylst

    return process(data, parent_path)


def collect_keys_from_json_files(files):
    all_elements = []
    for file in files:
        # Load JSON data from the file
        with open(file, 'r') as fp:
            data = json.load(fp)

        # Collect elements and their paths from the JSON data
        elements = collect_keys_from_json_string(data, id=file)

        # all_elements.append({"id": file, "dat": elements})
        all_elements.extend(elements)
