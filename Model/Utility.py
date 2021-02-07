
def openFile(json_path : str) -> str:
    contents : str = str()
    try:
        with open(json_path, 'rb') as f:
            contents = f.read()
    except Exception as err:
        print("Failed to open {0}: {1}".format(json_path, err))
    return contents

def writeFile(path : str, contents : str):
    try:
        with open(path, 'w') as f:
            f.write(contents)
    except Exception as err:
        print("Failed to open {0}: {1}".format(path, err))
