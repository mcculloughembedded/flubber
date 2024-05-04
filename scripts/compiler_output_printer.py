import sys
import json
from pretty_printer import *
from common import *
import re


def printCompilerOutput(component):
    clearErrorsBuffer()
    clearRemarksBuffer()

    try:
        file = open(f'{component}/logs/build-errors')
    except:
        return

    data = []
    linker_data = []
    for line in file:
        try:
            # Read in the compiler diagnostics
            data.append(json.loads(line))
        except:
            # Parse the linker diagnostics

            # Slight hack. Only match if a project source file
            if line.startswith("/project/"):
                # Oh no. Regex
                # Matches something like this:
                # <filename>:<linenumber>: <message>
                # eg. /project/unit-tests/haptic-driver/waveform-loader.cpp:20: undefined reference to `some_func()'
                msg = re.search("\/([^:^\n]+):(\d+):\s.*", line)
                if msg:
                    linker_data.append(relativePath(msg.string))

    # Remove empty json entries from GCC output
    data = list(filter(None, data))

    if data:
        INFO(displayText='Treating all warnings as errors')
        for entry in data[0]:
            if entry['kind'] == 'error' or entry['kind'] == 'fatal error':
                ERROR(displayText=getMessage(entry), filename=getFilename(
                    entry), line=getLineNumber(entry))
            elif entry['kind'] == 'note':
                REMARK(displayText=getMessage(entry), filename=getFilename(
                    entry), line=getLineNumber(entry))

    for line in linker_data:
        line = str(line)
        text = "".join(item for item in line.split(':', 2)[2:])
        ERROR(displayText=text, filename=line.split(
            ':')[0], line=line.split(':')[1])

    if errors():
        print()
        showErrorsBuffer()
    if remarks():
        print()
        showRemarksBuffer()
