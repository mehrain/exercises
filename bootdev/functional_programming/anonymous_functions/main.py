def categorize_file(filename):
    file_dict = {
        ".txt": "Text",
        ".docx": "Document",
        ".py": "Code",
    }

    get_category = lambda extension: file_dict.get(extension, "Unknown")
    

    return get_category(filename[filename.rfind(".") :])