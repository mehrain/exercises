#my code
def markdown_to_text(doc_content):
    split_document = doc_content.split("\n")
    new_document = []
    for line in split_document:
        if line.startswith("#"):
            line = line.lstrip("#")
        new_document.append(line)
    joined_string = "\n".join(new_document)
    return astrix_remover(joined_string)

def astrix_remover(doc_content):
    split_document = doc_content.split("\n")
    new_document = []
    for line in split_document:
        split_line = line.split()
        new_line = []
        for word in split_line:
            new_line.append(word.strip("*"))
        new_document.append(" ".join(new_line))
    return "\n".join(new_document)
return "\n".join(new_document)

#correct answer
'''
def markdown_to_text(doc_content):
    lines = doc_content.split("\n")

    new_lines = []
    for line in lines:
        header_removed = line.lstrip("#")
        emphasis_removed = remove_asterisks_from_words(header_removed)
        new_lines.append(emphasis_removed)

    return "\n".join(new_lines)


def remove_asterisks_from_words(line):
    words = line.split()
    new_words = []
    for word in words:
        if len(word) > 1:
            word = word.strip("*")
        if len(word) == 0:
            continue
        new_words.append(word)
    return " ".join(new_words)
    '''