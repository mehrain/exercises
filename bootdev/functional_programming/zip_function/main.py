valid_formats = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]

def pair_document_with_format(doc_names, doc_formats):
    formatted_names = list(zip(doc_names, doc_formats))
    return filter(lambda x: x[1] in valid_formats, formatted_names)