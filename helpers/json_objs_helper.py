import json


# read json file
def load_json(json_file_path):
    try:
        with open(json_file_path, "r") as fh:
            json_str = fh.read()
            return json_loads_objs(json_str)
    except FileNotFoundError:
        raise FileNotFoundError("file " + json_file_path + " not found")


# write output to file
def write_json(json_file_path, content):
    try:
        with open(json_file_path, "w") as fh:
            json.dump(content, fh)
    except:
        print("error write file")


def json_loads_objs(json_str):
    try:
        json.loads(json_str)
    except json.decoder.JSONDecodeError:
        raise json.decoder.JSONDecodeError("corrupted json file " + json_str)