from enum import Enum

class DocFormat(Enum):
    PDF = 1
    TXT = 2
    MD = 3
    HTML = 4

def convert_format(content, from_format, to_format):
    if from_format == DocFormat.MD and to_format == DocFormat.HTML:
        return content.replace("# ", "<h1>") + "</h1>"
    elif from_format == DocFormat.TXT and to_format == DocFormat.PDF:
        return "[PDF] " + content + " [PDF]"
    elif from_format == DocFormat.HTML and to_format == DocFormat.MD:
        return content.replace("<h1>", "# ").replace("</h1>", "")
    else:
        raise Exception("Invalid type")