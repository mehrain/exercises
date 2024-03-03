def markdown_to_text(doc_content):
    split_document = doc_content.split("\n")
    new_document = []
    for line in split_document:
        if line.startswith("#"):
            line = line.lstrip("#")
        new_document.append(line)
    return astrix_remover(new_document)

def astrix_remover(doc_content):
    new_document = []
    for line in doc_content:
        split_line = line.split(" ")
        new_line = []
        for word in split_line:
            new_line.append(word.strip("*"))
        new_document.append(" ".join(new_line))
    return "\n".join(new_document)

