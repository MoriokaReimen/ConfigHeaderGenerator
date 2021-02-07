
def openFile(toml_path : str) -> str:
    contents : str = str()
    try:
        with open(toml_path, 'r') as f:
            contents = f.read()
    except Exception as err:
        print("Failed to open {0}: {1}".format(toml_path, err))
    return contents

def writeFile(path : str, contents : str):
    try:
        with open(path, 'w') as f:
            f.write(contents)
    except Exception as err:
        print("Failed to open {0}: {1}".format(path, err))
