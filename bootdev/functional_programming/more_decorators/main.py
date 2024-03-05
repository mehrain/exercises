def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        args = [convert_md_to_txt(arg) for arg in args]
        kwargs = {k: convert_md_to_txt(v) for k, v in kwargs.items()}
        return func(*args, **kwargs)
    return wrapper

def convert_md_to_txt(doc):
    lines = doc.split("\n")
    text_lines = [line.lstrip("# ") for line in lines]
    return "\n".join(text_lines)


# Don't edit below this line


@markdown_to_text_decorator
def concat(first_doc, second_doc):
    return f"""First: {first_doc}
Second: {second_doc}
"""


@markdown_to_text_decorator
def format_as_essay(title, body, conclusion):
    return f"""Title: {title}
Body: {body}
Conclusion: {conclusion}
"""
