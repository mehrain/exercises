#Revisit this topic, took forever to understand the problem
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
