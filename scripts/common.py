import pathlib


def relativePath(fullPath: str):
    path = pathlib.Path(fullPath)
    return pathlib.Path(*path.parts[2:])


def getFilename(entry):
    try:
        return relativePath(entry['locations'][0]['caret']['file'])
    except:
        return None


def getMessage(entry):
    try:
        return entry['message']
    except:
        raise UserWarning(
            'Could not find a message. Recommend looking at the log files.')


def getLineNumber(entry):
    try:
        return entry['locations'][0]['caret']['line']
    except:
        return None
